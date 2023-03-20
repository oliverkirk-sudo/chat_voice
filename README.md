# chat_voice
[QChatGPT](https://github.com/RockChinQ/QChatGPT)的插件,用于将输出内容转化为音频,适用于小内存服务器

## 1、前置工作
使用前请先安装[FFmpeg](https://www.ffmpeg.org/download.html)并加入环境变量
<details>
<summary>Huggingface</summary>
    
- 首先注册一个[Huggingface](https://huggingface.co/)的账户
- 在[Plachta](https://huggingface.co/spaces/Plachta/VITS-Umamusume-voice-synthesizer)仓库右上角三点选择(Duplicate this Space)复制空间（选择公有库Public,私有库会导致连不上）
- 等待空间创建完毕
- 打开开发者工具(F12)，在工具栏中选择网络，并随便生成一个音频
- 观察网络控制台有一个join包，点击后会出现的websocket链接（以wss开头），复制下来
- 将生成的音频点击播放一下
- 观察网络控制台有一个wav文件，将链接复制下来，并去掉file=后面的参数，例如:`/tmp/tmp44z9i9_p/tmp82dtww6.wav`，留下的链接形式应该是这样的：
`https://plachta-vits-umamusume-voice-synthesizer.hf.space/file=`
    
</details>

<details>
<summary>Azure</summary>
    
- 首先在[Azure](https://azure.microsoft.com/zh-cn/)注册账号
- 创建[语音服务](https://portal.azure.com/#view/Microsoft_Azure_Marketplace/GalleryItemDetailsBladeNopdl/id/Microsoft.CognitiveServicesSpeechServices)
- 在面板中找到密钥与区域填入配置文件
    
</details>

<strong>其中Huggingface永久免费，Azure每月50万字的额度</strong>

## 2、修改配置文件
- 下载本插件`!plugin https://github.com/oliverkirk-sudo/chat_voice.git`
- 进入插件目录执行`pip install -r requirements.txt`
- 在config文件夹中将voice_config-temp.py修改为voice_config.py,格式如下：
```python
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
    "character": '0',  # 希望生成声音的角色,详情看mapper.py
    "language": '简体中文',  # 生成文本的语言['简体中文','日本語','English','Mix']
    "audio_speed": '1',  # 播放速度,可为保留一位小数点的小数[0.1 - 5]
    "download_url": '',  # 填入刚复制以https开头的链接
    "websocket": '',  # 填入以wss开头的websocket链接
}

```
- 用`!relaod`重新加载插件
- <strong>注意</strong>：修改character配置项需要注意与网页上character中的文本一字不差，包括空格
## 3、包含的指令
- `!voice on` 开启输出转语音
- `!voice off` 关闭输出转语音
- `!voice type azu`切换Azure语音合成
- `!voice type hgf`切换Huggingface语音合成
- `tovoice 文本消息` 将指定文本转换为声音输出
