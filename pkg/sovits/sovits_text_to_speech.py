import logging
import os
import subprocess
import sys
import time
import traceback
import librosa
import soundfile
import torch
from plugins.chat_voice.pkg.sovits.inference.infer_tool import Svc
from plugins.chat_voice.config.voice_config import SoVitsConfig

sovits_config = SoVitsConfig()

model = ''


def vc_fn2(hash_uuid, _text, _lang, _gender, _rate, _volume, sid, output_format, vc_transform, auto_f0, cluster_ratio, slice_db, noise_scale, pad_seconds, cl_num, lg_num, lgr_num, f0_predictor, enhancer_adaptive_key, cr_threshold, k_step, use_spk_mix, second_encoding, loudness_envelope_adjustment):
    global model
    try:
        if model is None:
            logging.error("You need to upload an model")
            return "You need to upload an model", None
        if getattr(model, 'cluster_model', None) is None and model.feature_retrieval is False:
            if cluster_ratio != 0:
                return "You need to upload an cluster model or feature retrieval model before assigning cluster ratio!", None
        _rate = f"+{int(_rate * 100)}%" if _rate >= 0 else f"{int(_rate * 100)}%"
        _volume = f"+{int(_volume * 100)}%" if _volume >= 0 else f"{int(_volume * 100)}%"
        if _lang == "Auto":
            _gender = "Male" if _gender == "男" else "Female"
            subprocess.run([sys.executable, os.path.join(os.getcwd(), "plugins/chat_voice/pkg/sovits/edgetts/tts.py"), _text, _lang, _rate, _volume, _gender])
        else:
            subprocess.run([sys.executable, os.path.join(os.getcwd(), "plugins/chat_voice/pkg/sovits/edgetts/tts.py"), _text, _lang, _rate, _volume])
        target_sr = 44100
        y, sr = librosa.load(os.path.join(os.getcwd(), 'voice_tmp', 'tts.wav'))
        resampled_y = librosa.resample(y, orig_sr=sr, target_sr=target_sr)
        soundfile.write(os.path.join(os.getcwd(), 'voice_tmp', 'tts.wav'), resampled_y, target_sr, subtype="PCM_16")
        input_audio = os.path.join(os.getcwd(), 'voice_tmp', 'tts.wav')
        # audio, _ = soundfile.read(input_audio)
        output_file_path = vc_infer(hash_uuid, output_format, sid, input_audio, "tts", vc_transform, auto_f0, cluster_ratio, slice_db, noise_scale, pad_seconds, cl_num, lg_num, lgr_num, f0_predictor, enhancer_adaptive_key, cr_threshold, k_step, use_spk_mix, second_encoding, loudness_envelope_adjustment)
        os.remove(os.path.join(os.getcwd(), 'voice_tmp', 'tts.wav'))
        return output_file_path
    except Exception as e:
        traceback.print_exc()  # noqa: E701


def vc_infer(hash_uuid, output_format, sid, audio_path, truncated_basename, vc_transform, auto_f0, cluster_ratio, slice_db, noise_scale, pad_seconds, cl_num, lg_num, lgr_num, f0_predictor, enhancer_adaptive_key, cr_threshold, k_step, use_spk_mix, second_encoding, loudness_envelope_adjustment):
    global model
    _audio = model.slice_inference(
        audio_path,
        sid,
        vc_transform,
        slice_db,
        cluster_ratio,
        auto_f0,
        noise_scale,
        pad_seconds,
        cl_num,
        lg_num,
        lgr_num,
        f0_predictor,
        enhancer_adaptive_key,
        cr_threshold,
        k_step,
        use_spk_mix,
        second_encoding,
        loudness_envelope_adjustment
    )
    model.clear_empty()
    # 构建保存文件的路径，并保存到results文件夹内
    str(int(time.time()))
    if not os.path.exists("results"):
        os.makedirs("results")
    # key = "auto" if auto_f0 else f"{int(vc_transform)}key"
    # cluster = "_" if cluster_ratio == 0 else f"_{cluster_ratio}_"
    # isdiffusion = "sovits"
    # if model.shallow_diffusion:
    #     isdiffusion = "sovdiff"
    #
    # if model.only_diffusion:
    #     isdiffusion = "diff"

    # output_file_name = 'result_' + truncated_basename + f'_{sid}_{key}{cluster}{isdiffusion}.{output_format}'
    # output_file_name = 'voice_' + hash_uuid + '.wav'
    output_file = os.path.join(os.getcwd(), 'voice_tmp', 'voice_' + hash_uuid + '.wav')
    print(output_file)
    # output_file = os.path.join("results", output_file_name)
    soundfile.write(output_file, _audio, model.target_sample, format=output_format)
    return output_file


def modelAnalysis(model_path, config_path, cluster_model_path, enhance, diff_model_path, diff_config_path, only_diffusion):
    global model
    try:
        cluster_filepath = os.path.split(cluster_model_path) if cluster_model_path is not None else "no_cluster"
        model_path = model_path
        config_path = config_path
        fr = ".pkl" in cluster_filepath[1]
        model = Svc(model_path,
                    config_path,
                    device=sovits_config.DEVICE,
                    cluster_model_path=cluster_model_path if cluster_model_path is not '' else "",
                    nsf_hifigan_enhance=enhance,
                    diffusion_model_path=diff_model_path if diff_model_path is not '' else "",
                    diffusion_config_path=diff_config_path if diff_config_path is not '' else "",
                    shallow_diffusion=True if diff_model_path is not '' else False,
                    only_diffusion=only_diffusion,
                    spk_mix_enable=False,
                    feature_retrieval=fr
                    )
        spks = list(model.spk2id.keys())
        device_name = torch.cuda.get_device_properties(model.dev).name if "cuda" in str(model.dev) else str(model.dev)
        logging.debug(f"成功加载模型到设备{device_name}上")
        if cluster_model_path == '':
            logging.debug("未加载聚类模型或特征检索模型")
        elif fr:
            logging.debug(f"特征检索模型{cluster_filepath}加载成功")
        else:
            logging.debug(f"聚类模型{cluster_filepath}加载成功")
        if diff_model_path == '':
            logging.debug("未加载扩散模型")
        else:
            logging.debug(f"扩散模型{diff_model_path}加载成功")
        spk_info = ''
        for i in spks:
            spk_info += i + " "
        logging.debug(f"讲话人列表：{spk_info}")
        return model
    except Exception as e:
        traceback.print_exc()


def modelUnload():
    global model
    if not model is None:
        model.unload_model()
        model = None
        torch.cuda.empty_cache()
        logging.debug("模型卸载成功")


def save_sovits_wav(text, hash_uuid):
    from plugins.chat_voice.config.mapper import sovits_model
    global model
    if sovits_model != '':
        model=sovits_model
    else:
        return False
    print(model)
    path = vc_fn2(hash_uuid, text, sovits_config.LANG, sovits_config.GENDER, sovits_config.RATE, sovits_config.VOLUME, sovits_config.SID, sovits_config.output_format, sovits_config.vc_transform, sovits_config.auto_f0, sovits_config.cluster_ratio, sovits_config.slice_db, sovits_config.noise_scale, sovits_config.pad_seconds, sovits_config.cl_num, sovits_config.lg_num, sovits_config.lgr_num,
                  sovits_config.f0_predictor, sovits_config.enhancer_adaptive_key, sovits_config.cr_threshold, sovits_config.k_step, sovits_config.use_spk_mix, sovits_config.second_encoding, sovits_config.loudness_envelope_adjustment)
    logging.debug(f'sovits生成{path}')
    if os.path.exists(path):
        return True
    else:
        return False


if __name__ == '__main__':
    if os.path.exists(save_sovits_wav('测试测试测试测试', '432hufe8dwa')):
        print('1111')
