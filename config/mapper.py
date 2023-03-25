from plugins.chat_voice.pkg.huggingface.huggingface_session_hash import get_audio_wav
from plugins.chat_voice.pkg.azure.azure_text_to_speech import save_azure_wav
from plugins.chat_voice.pkg.vits.vits_text_to_speech import save_vits_wav
voice_type_mapping = {
    'azu': 'azure',
    'hgf': 'huggingface'
}
method_mapping = {
    'azure': save_azure_wav,
    'huggingface': get_audio_wav,
    'vits': save_vits_wav
}
