# chat_voice
[QChatGPT](https://github.com/RockChinQ/QChatGPT)的插件,用于将输出内容转化为音频,适用于小内存服务器
新增支持本地模型部署
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

<details>
<summary>本地模型</summary>
- 代码参考自[FirKyle/vits](https://huggingface.co/spaces/FirKyle/vits)
- 模型依赖编译环境，请提前安装cmake（非pip安装），Ubuntu/Debian执行 `sudo apt-get install build-essential`,Centos执行`sudo yum groupinstall "Development Tools"`
- 由于默认不使用本地模型，且依赖较多，要使用请到vits文件夹下执行`pip install -r requirements.txt`
- 由于编译环境造成的错误请自行百度
- 将模型(G_latest.pth)与配置文件(config.json)放入model文件夹中,在Releases中下载测试模型model.zip，解压并将两个文件放在model文件夹中，由于只包含纳西妲一个角色，所以请不要更改`speak_id`
- config.json应与模型对应，不可使用其他模型config
- config.json仅支持moegoe内容格式的config文件，具体参考[MoeGoe](https://github.com/CjangCjengh/MoeGoe)
- 未来会支持角色实时切换与角色预览，以及其他参数调节
- 未来会支持[FirKyle/vits](https://huggingface.co/spaces/FirKyle/vits)以及提供修改方法[songwy/vits](https://huggingface.co/spaces/songwy/vits)

</details>

<strong>其中Huggingface永久免费但每次限制150字，Azure每月50万字的额度，本地模型对CPU内存要求较高</strong>

## 2、修改配置文件
- 下载本插件`!plugin https://github.com/oliverkirk-sudo/chat_voice.git`
- 进入插件目录执行`pip install -r requirements.txt`
- 在config文件夹中将voice_config-temp.py修改为voice_config.py,格式如下：
```python
voice_config = {
    "open": True,  # 默认开关
    "limitLength": 256,  # 设置语音文字限长 0为无限制，长度过长易导致生成时间长
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
vits_config = {
    "device": "cpu",  # cpu or cuda,cuda需要NVIDIA显卡
    "ns": 0.1,  # noise_scale(控制感情变化程度),范围[0.1-1.0],调大了声音容易怪，除非模型好
    "nsw": 0.5,  # noise_scale_w(控制音素发音长度)，范围[0.1-1.0]
    "ls": 1.2,  # 语速调节，范围[0.1-2.0],越大越快
    "text_length": 300,  # 最大文本长度
    "lang": "zh",  # 语言，zh|ja|mix,mix时将中文用[ZH]包裹，日文用[JA]包裹
    "speak_id": 0,  # 朗读人id
}
```
- 用`!relaod`重新加载插件
- <strong>注意</strong>：修改character配置项需要注意与网页上character中的文本一字不差，包括空格
## 3、包含的指令
- `!voice on` 开启输出转语音
- `!voice off` 关闭输出转语音
- `!voice type azu`切换Azure语音合成
- `!voice type hgf`切换Huggingface语音合成
- `!voice type vist`切换VITS语音合成
- `tovoice 文本消息` 将指定文本转换为声音输出
