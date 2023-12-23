voice_config = {
    "open": True,  # 默认开关
    "limitLength": 256,  # 设置语音文字限长 0为无限制
    "voice_type": "mhyvoice",  # 默认合成类型"azure"|"huggingface"|"vits"|"sovits"|"mhyvoice"
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
    "open": False,
    "device": "cpu",  # cpu or cuda,cuda需要NVIDIA显卡
    "ns": 0.2,  # noise_scale(控制感情变化程度),范围[0.1-1.0],调大了声音容易怪，除非模型好
    "nsw": 0.5,  # noise_scale_w(控制音素发音长度)，范围[0.1-1.0]
    "ls": 1.0,  # 语速调节，范围[0.1-2.0],越大越快
    "text_length": 300,  # 最大文本长度
    "lang": "zh",  # 语言，zh|ja|mix,mix时将中文用[ZH]包裹，日文用[JA]包裹
    "speak_id": 0,  # 朗读人id
}

class GenShinVoice:
    def __init__(self):
        self.open = True
        self.character = "派蒙_ZH"
        self.audio_speed = 1
        self.ns = 0.5
        self.nsw = 0.9
        self.sdp_radio = 0.2
        self.timeout=30
        self.emotion="Happy"
        self.weight=0.7
        


class SoVitsConfig:
    def __init__(self):
        self.OPEN = False
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
