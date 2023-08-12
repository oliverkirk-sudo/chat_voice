# coding=utf-8
import os
import traceback
import logging

try:
    from plugins.chat_voice.config.voice_config import vits_config
except Exception:
    logging.error("请先配置voice_config.py")
    traceback.print_exc()

load_model = True
model_path = os.path.join(os.getcwd(), "plugins/chat_voice/model/vits/G_latest.pth")
config_path = os.path.join(os.getcwd(), "plugins/chat_voice/model/vits/config.json")
if not os.path.exists(model_path) or not os.path.exists(config_path):
    load_model = False
    logging.warning("model文件夹中没有模型或配置文件，vits不会启动")


def save_vits_wav(text, hash_uuid):
    if load_model:
        import numpy as np
        from scipy.io.wavfile import write
        vits = Vits()
        status, voice = vits.get_vits_voice_tuple(text)
        if not status:
            logging.error("vits音频文件生成失败，请检查配置文件参数")
            return False
        try:
            scaled = np.int16(voice[1] / np.max(np.abs(voice[1])) * 32767)
            file_path = os.path.join(os.getcwd(), 'voice_tmp', 'voice_' + hash_uuid + '.wav')
            write(file_path, 22050, scaled)
            return True
        except Exception:
            traceback.print_exc()
            return False
    return False


def get_text(text, hps):
    import plugins.chat_voice.pkg.vits.commons as commons
    from torch import LongTensor
    from plugins.chat_voice.pkg.vits.text import text_to_sequence
    text_norm, clean_text = text_to_sequence(text, hps.symbols, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = LongTensor(text_norm)
    return text_norm, clean_text


def change_lang(language):
    if language == 0:
        return 0.6, 0.668, 1.2
    else:
        return 0.6, 0.668, 1.1


def check_config():
    if vits_config['device'] and 0.1 <= vits_config['ns'] <= 1.0 and 0.1 <= vits_config['nsw'] <= 1.0 and 0.1 <= \
            vits_config['ls'] <= 2.0:
        return True
    else:
        return False


class Vits:
    def __init__(self):
        self.speakers = None
        self.model = None
        self.optimizer = None
        self.learning_rate = None
        self.epochs = None
        self.hps_ms = None
        self.net_g_ms = None
        self.device = None
        self.device_text = vits_config['device']
        self.ns = vits_config['ns']
        self.nsw = vits_config['nsw']
        self.ls = vits_config['ls']
        self.lang = vits_config['lang']
        self.speak_id = vits_config['speak_id']


    def vits(self, text, language, speaker_id, noise_scale, noise_scale_w, length_scale):
        if not len(text):
            logging.warning("文本长度不能为0")
            return False, None
        from torch import no_grad, LongTensor
        text = text.replace('\n', ' ').replace('\r', '').replace(" ", "")
        if language == 'zh':
            text = f"[ZH]{text}[ZH]"
        elif language == 'ja':
            text = f"[JA]{text}[JA]"
        elif language == 'mix':
            text = f"{text}"
        else:
            logging.error('vits：错误的语言，请检查配置文件')
            return False, None
        stn_tst, clean_text = get_text(text, self.hps_ms)
        with no_grad():
            x_tst = stn_tst.unsqueeze(0).to(self.device)
            x_tst_lengths = LongTensor([stn_tst.size(0)]).to(self.device)
            speaker_id = LongTensor([speaker_id]).to(self.device)
            audio = \
                self.net_g_ms.infer(x_tst, x_tst_lengths, sid=speaker_id, noise_scale=noise_scale,
                                    noise_scale_w=noise_scale_w,
                                    length_scale=length_scale)[0][0, 0].data.cpu().float().numpy()

        return True, (22050, audio)

    def search_speaker(self, search_value):
        for s in self.speakers:
            if search_value == s:
                return s
        for s in self.speakers:
            if search_value in s:
                return s

    def get_vits_voice_tuple(self, text_to_voice):
        if not check_config():
            logging.error("voice_config.py中的vits_config字段有不合法数据")
            return
        from plugins.chat_voice.pkg.vits.models import SynthesizerTrn
        import plugins.chat_voice.pkg.vits.utils as utils
        import torch
        self.device = torch.device(self.device_text)
        self.hps_ms = utils.get_hparams_from_file(config_path)
        self.net_g_ms = SynthesizerTrn(
            len(self.hps_ms.symbols),
            self.hps_ms.data.filter_length // 2 + 1,
            self.hps_ms.train.segment_size // self.hps_ms.data.hop_length,
            n_speakers=self.hps_ms.data.n_speakers,
            **self.hps_ms.model)
        _ = self.net_g_ms.eval().to(self.device)
        self.speakers = self.hps_ms.speakers
        self.model, self.optimizer, self.learning_rate, self.epochs = utils.load_checkpoint(model_path, self.net_g_ms,
                                                                                            None)
        return self.vits(text_to_voice, self.lang, self.speak_id, self.ns, self.nsw, self.ls)
