# chat_voice
QChatGPT的插件，用于将输出内容转化为音频

## 1、前置工作
- 首先注册一个[Huggingface](https://huggingface.co/)的账户
- 在[Plachta](https://huggingface.co/spaces/Plachta/VITS-Umamusume-voice-synthesizer)仓库右上角三点选择(Duplicate this Space)复制空间
- 等待空间创建完毕
- 打开控制台(F12)随便生成一个音频
- 观察控制台有一个join的websocket链接以wss开头，复制下来
- 将生成的音频点击播放一下
- 观察控制台有一个wav文件的链接复制下来，并去掉file=后面的参数，例如:`/tmp/tmp44z9i9_p/tmp82dtww6.wav`，留下的链接形式应该是这样的：
`https://plachta-vits-umamusume-voice-synthesizer.hf.space/file=`
## 2、修改配置文件
- 下载本插件`!plugin https://github.com/oliverkirk-sudo/chat_voice.git`
- 在config文件夹中修改voice_config.py,格式如下：
```python
voice_config = {
    "open": True, #默认开关
    "character": '派蒙 Paimon (Genshin Impact)',  #希望生成声音的角色
    "language": '简体中文', #生成文本的语言
    "audio_speed": '1', #播放速度,可为保留一位小数点的小数[0.1 - 5]
    "download_url":'', #填入刚复制以https开头的链接
    "websocket":'' #填入以wss开头的websocket链接
}
```
- 用`!relaod`重新加载插件
- <strong>注意</strong>：修改character配置项需要注意与网页上character中的文本一字不差，包括空格
## 3、包含的指令
- `!voice on` 开启输出转语音
- `!voice off` 关闭输出转语音
