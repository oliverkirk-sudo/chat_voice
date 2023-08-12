import logging
import traceback
from plugins.chat_voice.config.voice_config import SoVitsConfig
method_mapping = {
#    'azure': save_azure_wav,
#    'huggingface': get_audio_wav,
#    'vits': save_vits_wav,
#    'sovits': save_sovits_wav
}

voice_type_mapping = {
#    'azu': 'azure',
#    'hgf': 'huggingface',
#    'vits': 'vits',
#    'sovits': 'sovits'
}

sovits_model=''

try:
    from plugins.chat_voice.config.voice_config import voice_config,azure_config,huggingface_config,vits_config,SoVitsConfig
except Exception:
    logging.error("请正确配置voice_config.py")
    traceback.print_exc()
try:
    if huggingface_config['open']:
        from plugins.chat_voice.pkg.huggingface.huggingface_session_hash import get_audio_wav
        method_mapping['huggingface'] = get_audio_wav
        voice_type_mapping['hgf'] = 'huggingface'
    if azure_config['open']:
        from plugins.chat_voice.pkg.azure.azure_text_to_speech import save_azure_wav
        method_mapping['azure'] = save_azure_wav
        voice_type_mapping['azu'] = 'azure'
    if vits_config['open']:
        from plugins.chat_voice.pkg.vits.vits_text_to_speech import save_vits_wav
        method_mapping['vits'] = save_vits_wav
        voice_type_mapping['vits'] = 'vits'
    if SoVitsConfig().OPEN:
        sovits_config=SoVitsConfig()
        from plugins.chat_voice.pkg.sovits.sovits_text_to_speech import save_sovits_wav,modelAnalysis
        method_mapping['sovits'] = save_sovits_wav
        voice_type_mapping['sovits'] = 'sovits'
        sovits_model=modelAnalysis(sovits_config.MODEL_PATH, sovits_config.CONFIG_PATH, sovits_config.CLUSTER_MODEL_PATH, sovits_config.ENHANCE, sovits_config.DIFF_MODEL_PATH,sovits_config.DIFF_CONFIG_PATH, sovits_config.ONLY_DIFFUSION)
except Exception:
    logging.error("包加载错误")
    traceback.print_exc()


