# coding=utf-8
import os

import requests
import base64
import plugins.chat_voice.config.voice_config as voice_conf

session = requests.session()
config = voice_conf.GenShinVoice()


def get_voice_binary(
    text: str,
):
    api = "https://genshinvoice.top/api"
    data = {
        "speaker": config.character,
        "text": text,
        "format": "wav",
        "length": config.audio_speed,
        "noise": config.ns,
        "noisew": config.nsw,
        "sdp_ratio": config.sdp_radio,
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1788.0",
        "Referer": "https://genshinvoice.top/v2/",
    }
    try:
        voice_res = session.get(api, params=data, headers=headers,timeout=config.timeout)
    except Exception:
        return ""
    sesion.close()
    return voice_res


def save_genshinvoice_wav(text: str, hash_uuid: str):
    file_path = os.getcwd()
    try:
        voice_content = get_voice_binary(text)
        if voice_content=="" or voice_content.status_code != 200:
            return False
        with open(
            os.path.join(file_path, "voice_tmp", "voice_" + hash_uuid + ".wav"), "wb"
        ) as f:
            f.write(voice_content.content)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    print(get_voice_binary("测试"))