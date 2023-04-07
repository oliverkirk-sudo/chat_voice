voice_config = {
    "open": True,  # 默认开关
    "limitLength": 256,  # 设置语音文字限长 0为无限制
    "voice_type": "azure",  # 默认合成类型"azure"|"huggingface"|"vits"
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
    "character": '0',  # 希望生成声音的角色,详情看mapper.py
    "language": '简体中文',  # 生成文本的语言['简体中文','日本語','English','Mix']
    "audio_speed": '1',  # 播放速度,可为保留一位小数点的小数[0.1 - 5]
    "download_url": '',  # 填入刚复制以https开头的链接
    "websocket": '',  # 填入以wss开头的websocket链接
}
vits_config = {
    "device": "cpu",  # cpu or cuda,cuda需要NVIDIA显卡
    "ns": 0.1,  # noise_scale(控制感情变化程度),范围[0.1-1.0],调大了声音容易怪，除非模型好
    "nsw": 0.5,  # noise_scale_w(控制音素发音长度)，范围[0.1-1.0]
    "ls": 1.2,  # 语速调节，范围[0.1-2.0],越大越快
    "text_length": 300,  # 最大文本长度
    "lang": "zh",  # 语言，zh|ja|mix,mix时将中文用[ZH]包裹，日文用[JA]包裹
    "speak_id": 0,  # 朗读人id
}
