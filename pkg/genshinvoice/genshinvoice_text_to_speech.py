# coding=utf-8
import os
import logging
import requests
import base64
import plugins.chat_voice.config.voice_config as voice_conf

config = voice_conf.GenShinVoice()


def get_voice_binary(
    text: str,
):
    api = "https://v2.genshinvoice.top"
    data = {
        "data": [
            text,
            config.character,
            config.sdp_radio,
            config.ns,
            config.nsw,
            config.audio_speed,
            config.character.split("_")[1],
            None,
            config.emotion,
            "Text prompt",
            "",
            config.weight
        ],
        "event_data": 'null',
        "fn_index": 0,
        "session_hash": str(uuid4()).lower().split("-")[0]
    }
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,fa;q=0.6",
        "Content-Type": "application/json",
        "Origin": "https://v2.genshinvoice.top",
        "Pragma": "no-cache",
        "Referer": "https://v2.genshinvoice.top/?",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        resp = requests.post(url + "/run/predict", json=data, headers=headers)
        data = resp.json()
        if data["data"][0] == "Success":
            file_name = data["data"][1]["name"]
            file_url = url + f"/file={file_name}"
            audio = requests.get(file_url)
            logging.info(f"genshinvoice生成状态码:{audio.status_code}")
            return audio
        else:
            raise Exception
    except Exception as e:
        logging.error(f"genshinvoice生成错误:{str(e)}")
        return ""
    return ""


def save_genshinvoice_wav(text: str, hash_uuid: str):
    try:
        file_path = os.getcwd()
        voice_content = get_voice_binary(text)
        if voice_content.status_code != 200:
            logging.error(f"genshinvoice生成错误")
            return False
        with open(
            os.path.join(file_path, "voice_tmp", "voice_" + hash_uuid + ".wav"), "wb"
        ) as f:
            f.write(voice_content.content)
        logging.info(f"genshinvoice生成完成")
        return True
    except Exception as e:
        logging.error(f"genshinvoice生成错误:{str(e)}")
        return False


if __name__ == "__main__":
    print(get_voice_binary("测试"))
