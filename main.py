import os
import traceback

import mirai

from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost
from plugins.chat_voice.pkg.huggingface_session_hash import get_audio_wav
from plugins.chat_voice.pkg.wav2silk import convert_to_silk
from uuid import uuid4
from plugins.chat_voice.config.voice_config import voice_config


def _get_voice_wav(input_text):
    if voice_config['limitLength'] != 0 and len(input_text)>voice_config['limitLength']:
        input_text = input_text[0:voice_config['limitLength']] #超过限长截取
    hash_uuid = str(uuid4()).replace('-', '')[:9:]
    if not get_audio_wav(input_text, hash_uuid):
        logging.error("wav生成失败")
        return hash_uuid, ''
    return hash_uuid, _wav2silk(hash_uuid)


def _wav2silk(hash_uuid):
    wav_path = os.path.join(os.getcwd(), 'voice_tmp', 'voice_' + hash_uuid + '.wav')
    return mirai.Voice(path=convert_to_silk(wav_path))


def _remove_tmp(hash_uuid):
    try:
        os.remove(os.path.join(os.getcwd(), 'voice_tmp', 'voice_' + hash_uuid + '.wav'))
        os.remove(os.path.join(os.getcwd(), 'voice_tmp', 'voice_' + hash_uuid + '.pcm'))
    except FileNotFoundError:
        logging.warning("未找到wav,pcm与silk文件")
    except Exception:
        traceback.print_exc()


def _open_text_to_voice():
    voice_config["open"] = True


def _close_text_to_voice():
    voice_config["open"] = False


# 注册插件
@register(name="chat_voice", description="让机器人用语音输出", version="0.1", author="oliverkirk-sudo")
class ChatVoicePlugin(Plugin):

    def __init__(self, plugin_host: PluginHost):
        if not os.path.exists(os.path.join(os.getcwd(), 'voice_tmp')):
            os.mkdir(os.path.join(os.getcwd(), 'voice_tmp'))

    @on(NormalMessageResponded)
    def person_normal_message_received(self, event: EventContext, **kwargs):
        if voice_config['open']:
            uuid, msg = _get_voice_wav(kwargs['response_text'])
            if msg == '':
                event.add_return('reply', [kwargs['response_text']])
                event.prevent_default()
            else:
                event.add_return('reply', [msg])
                event.prevent_default()
            _remove_tmp(uuid)
        else:
            event.add_return('reply', [kwargs['response_text']])
            event.prevent_default()

    @on(PersonNormalMessageReceived)
    @on(GroupNormalMessageReceived)
    def self_text_to_voice(self, event: EventContext, **kwargs):
        msg = kwargs['text_message']
        if msg.strip().startswith('tovoice'):
            if not voice_config['open']:
                event.add_return('reply', ['输出转语音功能未开启'])
                event.prevent_default()
            else:
                text = msg.replace('tovoice', '').strip()
                uuid, voice = _get_voice_wav(text)
                if voice == '':
                    event.add_return('reply', [kwargs['response_text']])
                else:
                    event.add_return('reply', [voice])
                _remove_tmp(uuid)
                event.prevent_default()

    @on(PersonCommandSent)
    @on(GroupCommandSent)
    def open_text_to_voice(self, event: EventContext, **kwargs):
        command = kwargs['command']
        if command == 'voice' and kwargs['is_admin']:
            if kwargs['params'][0] == 'on':
                logging.debug("{}开启了文字转语音".format(kwargs['sender_id']))
                _open_text_to_voice()
                event.add_return('reply', ["开启语音输出"])
            elif kwargs['params'][0] == 'off':
                logging.debug("{}关闭了文字转语音".format(kwargs['sender_id']))
                _close_text_to_voice()
                event.add_return('reply', ["语音输出关闭"])
            else:
                logging.debug("{}输入了不正确的参数".format(kwargs['sender_id']))
                event.add_return('reply', ["不正确的参数，!voice on 为开，!voice off 为关"])
            event.prevent_default()

    # 插件卸载时触发
    def __del__(self):
        pass
