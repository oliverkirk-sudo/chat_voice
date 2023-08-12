# chat_voice
[QChatGPT](https://github.com/RockChinQ/QChatGPT)的插件,用于将输出内容转化为音频,适用于小内存服务器
- 新增支持本地模型部署
## 一些问题
- 关于私信语音音质差的原因：是因为[YiriMirai](https://github.com/YiriMiraiProject/YiriMirai)支持的mirai版本到2.5，尚不支持[Audio](https://github.com/mamoe/mirai/blob/dev/docs/Messages.md#%E6%B6%88%E6%81%AF%E5%85%83%E7%B4%A0),使音频被压缩为amr格式
- ~~与New Bing插件不兼容的原因是[QChatGPT](https://github.com/RockChinQ/QChatGPT)现在尚未支持消息在组件间传递。~~

## 1、前置工作
若启用sovits语音转换，请先安装[FFmpeg](https://www.ffmpeg.org/download.html)并加入环境变量
包内自动安装对FFmpeg的依赖
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
    
- 代码参考自[vits-uma-genshin-honkai](https://huggingface.co/spaces/ikechan8370/vits-uma-genshin-honkai)
- 模型依赖编译环境，请提前安装cmake（非pip安装），Ubuntu/Debian执行 `sudo apt-get install -y python3-dev build-essential libpython3.9-dev gcc g++`,Centos执行`sudo yum groupinstall "Development Tools"`
- 由于默认不使用本地模型，且依赖较多，要使用请到vits文件夹下执行`pip install -r requirements.txt`
- 由于编译环境造成的错误请自行百度
- 将模型(G_latest.pth)与配置文件(config.json)放入model/vits文件夹中,在Releases中下载测试模型model.zip，解压并将两个文件放在model/vits文件夹中，由于只包含纳西妲一个角色，所以请不要更改`speak_id`
- config.json应与模型对应，不可使用其他模型config
- config.json仅支持moegoe内容格式的config文件，具体参考[MoeGoe](https://github.com/CjangCjengh/MoeGoe)
- 未来会支持角色实时切换与角色预览，以及其他参数调节
- 未来会支持[vits-uma-genshin-honkai](https://huggingface.co/spaces/ikechan8370/vits-uma-genshin-honkai)以及提供修改方法[songwy/vits](https://huggingface.co/spaces/songwy/vits)

</details>

<details>
<summary>SoVits</summary>
    
- 代码参考自[so-vits-svc](https://github.com/svc-develop-team/so-vits-svc)
- SoVits占用的资源较多，请确保服务器内存与cpu性能足够
- 环境安装时间较久，请耐心等待
- 由于编译环境造成的错误请自行百度
- 将模型(必要)、配置文件(必要)、扩散模型(选要)、扩散模型配置文件(选要)，聚类模型(选要)放入model/vits文件夹中,解压并将两个文件放在model/sovits文件夹中，并正确配置配置文件
- pretrain中需要下载声音编码器模型，具体请参考[so-vits-svc](https://github.com/svc-develop-team/so-vits-svc)中的说明
- 使用扩散模型时需要修改yaml中的vocoder的ckpt项为`plugins/chat_voice/pkg/sovits/pretrain/nsf_hifigan/model`
    
</details>

<strong>其中Huggingface永久免费但每次限制150字，Azure每月50万字的额度，本地模型对CPU内存要求较高</strong>

## 2、修改配置文件
- 下载本插件`!plugin get https://github.com/oliverkirk-sudo/chat_voice.git`
- 进入插件目录执行`pip install -r requirements.txt`
- 若不想启用某功能，请将对应的open键值改为False
- 在config文件夹中将voice_config_temp.py修改为voice_config.py,格式如下：
```python
voice_config = {
    "open": True,  # 默认开关
    "limitLength": 256,  # 设置语音文字限长 0为无限制
    "voice_type": "azure",  # 默认合成类型"azure"|"huggingface"|"vits"
    # "proxy_host": "127.0.0.1", #代理ip
    # "proxy_port": 7890, #代理端口
    # "proxy_type": "http" #代理方式 http | socks5
}
azure_config = {
    "open": True,
    "region": "",  # azure区域
    "secret": "",  # 密钥
    "language": "zh-CN",  # 语言
    "language_person": "zh-CN-XiaoxuanNeural",  # 朗读人
    # 参考https://learn.microsoft.com/zh-cn/azure/cognitive-services/speech-service/language-support?tabs=tts#prebuilt-neural-voices
}
huggingface_config = {
    "open": True,
    "character": '0',  # 希望生成声音的角色,详情看mapper.py
    "language": '简体中文',  # 生成文本的语言['简体中文','日本語','English','Mix']
    "audio_speed": '1',  # 播放速度,可为保留一位小数点的小数[0.1 - 5]
    "download_url": '',  # 填入刚复制以https开头的链接
    "websocket": '',  # 填入以wss开头的websocket链接
}
vits_config = {
    "open": True,
    "device": "cpu",  # cpu or cuda,cuda需要NVIDIA显卡
    "ns": 0.2,  # noise_scale(控制感情变化程度),范围[0.1-1.0],调大了声音容易怪，除非模型好
    "nsw": 0.5,  # noise_scale_w(控制音素发音长度)，范围[0.1-1.0]
    "ls": 1.0,  # 语速调节，范围[0.1-2.0],越大越快
    "text_length": 300,  # 最大文本长度
    "lang": "zh",  # 语言，zh|ja|mix,mix时将中文用[ZH]包裹，日文用[JA]包裹
    "speak_id": 0,  # 朗读人id
}


class SoVitsConfig:
    def __init__(self):
        self.OPEN = True
        # 模型位置
        self.MODEL_PATH = ''
        # 模型配置文件位置
        self.CONFIG_PATH = ''
        # 说话人
        self.SID = 'nahida'
        # 扩散模型位置
        self.DIFF_MODEL_PATH = ''
        # 扩散模型配置文件
        self.DIFF_CONFIG_PATH = ''
        # 聚类模型位置
        self.CLUSTER_MODEL_PATH = ''
        # 设备
        self.DEVICE = 'cpu'
        # 是否使用NSF_HIFIGAN增强
        self.ENHANCE = False
        # 选择edgetts说话人
        self.LANG = 'Auto'
        # edgetts说话人性别
        self.GENDER = '女'
        # TTS语音变速（倍速相对值）
        self.RATE = 0
        # TTS语音音量（相对值）
        self.VOLUME = 0
        # 是否只使用扩散推理
        self.ONLY_DIFFUSION = False
        # 自动f0预测
        self.auto_f0 = True
        # 选择F0预测器,可选择crepe,pm,dio,harvest,rmvpe,默认为pm(注意：crepe为原F0使用均值滤波器)
        self.f0_predictor = "pm"
        # 变调（整数，可以正负，半音数量，升高八度就是12）
        self.vc_transform = 0
        # 聚类模型/特征检索混合比例，0-1之间，0即不启用聚类/特征检索。使用聚类/特征检索能提升音色相似度，但会导致咬字下降（如果使用建议0.5左右）
        self.cluster_ratio = 0.2
        # 切片阈值
        self.slice_db = -40
        # 音频输出格式
        self.output_format = "wav"
        # noise_scale 建议不要动，会影响音质，玄学参数
        self.noise_scale = 0.4
        # 浅扩散步数，只有使用了扩散模型才有效，步数越大越接近扩散模型的结果
        self.k_step = 100
        # 推理音频pad秒数，由于未知原因开头结尾会有异响，pad一小段静音段后就不会出现
        self.pad_seconds = 0.5
        # 音频自动切片，0为不切片，单位为秒(s)
        self.cl_num = 60
        # 两端音频切片的交叉淡入长度，如果自动切片后出现人声不连贯可调整该数值，如果连贯建议采用默认值0，注意，该设置会影响推理速度，单位为秒/s
        self.lg_num = 0
        # 自动音频切片后，需要舍弃每段切片的头尾。该参数设置交叉长度保留的比例，范围0-1,左开右闭
        self.lgr_num = 0.75
        # 使增强器适应更高的音域(单位为半音数)|默认为0
        self.enhancer_adaptive_key = 0
        # F0过滤阈值，只有启动crepe时有效. 数值范围从0-1. 降低该值可减少跑调概率，但会增加哑音
        self.cr_threshold = 0.05
        # 输入源响度包络替换输出响度包络融合比例，越靠近1越使用输出响度包络
        self.loudness_envelope_adjustment = 0
        # 二次编码，浅扩散前会对原始音频进行二次编码，玄学选项，效果时好时差，默认关闭
        self.second_encoding = False
        # 动态声线融合
        self.use_spk_mix = False

```
- 用`!relaod`重新加载插件
## 3、包含的指令
- `!voice on` 开启输出转语音
- `!voice off` 关闭输出转语音
- `!voice type azu`切换Azure语音合成
- `!voice type hgf`切换Huggingface语音合成
- `!voice type vist`切换VITS语音合成
- `!voice type sovist`切换VITS语音合成
- `tovoice 文本消息` 将指定文本转换为声音输出
