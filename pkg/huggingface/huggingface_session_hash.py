import logging
import os
import random
import string
import traceback
import websocket
import json
import requests
from plugins.chat_voice.config.character_list import character_list

try:
    from plugins.chat_voice.config.voice_config import huggingface_config, voice_config
except Exception:
    logging.error("请先配置voice_config.py")
    traceback.print_exc()

rand_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=11))
character = character_list[huggingface_config['character']]
language = huggingface_config['language']
audio_speed = huggingface_config['audio_speed']
hash_session = '{"session_hash":"' + rand_str + '","fn_index":2}'
audio_data = ''
audio_url = ''
base_url = huggingface_config['download_url']
ws_url = huggingface_config['websocket']
host = voice_config['proxy_host'] if 'proxy_host' in voice_config.keys() else None
port = voice_config['proxy_port'] if 'proxy_port' in voice_config.keys() else None
proxy_type = voice_config['proxy_type'] if 'proxy_type' in voice_config.keys() else None

def _get_audio_url():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(ws_url, on_message=on_message)
    if host and port and proxy_type:
        ws.run_forever(ping_timeout=30, http_proxy_host=host,
                       http_proxy_port=port, proxy_type=proxy_type)
    else:
        ws.run_forever(ping_timeout=30)
    return base_url + audio_url

def on_message(ws, message):
    global audio_url
    try:
        if json.loads(message)['msg'] == 'send_hash':
            ws.send(hash_session)
        if json.loads(message)['msg'] == 'send_data':
            ws.send(audio_data)
        if json.loads(message)['msg'] == 'process_completed':
            audio_url = json.loads(message)['output']['data'][1]['name']
    except Exception:
        traceback.print_exc()
        return ''

def get_audio_wav(text: str, hash_uuid):
    global audio_data
    audio_data = '{"fn_index":2,"data":["' + text.replace('"',"'") + '","' + character + '","' + language + '",' + audio_speed + ',false],"session_hash":"' + rand_str + '"}'
    file_path = os.getcwd()
    try:
        voice_content = requests.get(_get_audio_url())
        if voice_content.status_code == 200:
            with open(os.path.join(file_path, 'voice_tmp', 'voice_' + hash_uuid + '.wav'), 'wb') as f:
                f.write(voice_content.content)
            return True
        else:
            return False
    except Exception:
        traceback.print_exc()
        return False
