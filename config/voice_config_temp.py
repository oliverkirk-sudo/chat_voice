voice_config = {
    "open": True,  # 默认开关
    "limitLength": 256,  # 设置语音文字限长 0为无限制
    "voice_type": "azure"  # 默认合成类型"azure"或"huggingface"
    # "proxy_host": "127.0.0.1", #代理ip
    # "proxy_port": 7890, #代理端口
    # "proxy_type": "http" #代理方式 http | socks5
}
azure_config = {
    "region": "",  # azure区域
    "secret": "",  # 密钥
    "language": "zh-CN",  # 语言
    "language_person": "zh-CN-XiaoxuanNeural",  # 朗读人
    # 参考https://learn.microsoft.com/zh-cn/azure/cognitive-services/speech-service/language-support?tabs=tts#prebuilt-neural-voices
}
huggingface_config = {
    "character": '派蒙 Paimon (Genshin Impact)',  # 希望生成声音的角色
    "language": '简体中文',  # 生成文本的语言['简体中文','日本語','English','Mix']
    "audio_speed": '1',  # 播放速度,可为保留一位小数点的小数[0.1 - 5]
    "download_url": '',  # 填入刚复制以https开头的链接
    "websocket": '',  # 填入以wss开头的websocket链接
}
