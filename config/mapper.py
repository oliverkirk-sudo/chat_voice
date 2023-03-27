import logging
import traceback
from plugins.chat_voice.config.voice_config import voice_config
try:
    if voice_config['voice_type']=='huggingface':
        from plugins.chat_voice.pkg.huggingface.huggingface_session_hash import get_audio_wav
    elif voice_config['voice_type']=='azure':
        from plugins.chat_voice.pkg.azure.azure_text_to_speech import save_azure_wav
    elif voice_config['voice_type']=='vits':
        from plugins.chat_voice.pkg.vits.vits_text_to_speech import save_vits_wav
except Exception:
    logging.error("包加载错误")
    traceback.print_exc()
try:
    from plugins.chat_voice.config.voice_config import voice_config
except Exception:
    logging.error("请正确配置voice_config.py")
    traceback.print_exc()
voice_type_mapping = {
    'azu': 'azure',
    'hgf': 'huggingface',
    'vits': 'vits'
}
method_mapping = {
    'azure': save_azure_wav,
    'huggingface': get_audio_wav,
    'vits': save_vits_wav
}
