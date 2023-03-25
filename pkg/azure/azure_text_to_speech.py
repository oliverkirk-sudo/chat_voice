import os
import logging
import traceback
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import SpeechSynthesizer, AudioDataStream
try:
    from plugins.chat_voice.config.voice_config import azure_config
except Exception:
    logging.error("请先配置voice_config.py")
    traceback.print_exc()

class Azure:

    def __init__(self):
        self.speech: SpeechSynthesizer = None
        self.speech_key: str = azure_config["secret"]
        self.service_region: str = azure_config["region"]
        self.hash_uuid = ''

    def set_config(self):
        speech_config = speechsdk.SpeechConfig(subscription=self.speech_key, region=self.service_region)
        audio_config = speechsdk.audio.AudioOutputConfig(filename=os.path.join(os.getcwd(), 'voice_tmp', 'voice_' + self.hash_uuid + '.wav'))
        speech_config.speech_synthesis_language = azure_config["language"]
        speech_config.speech_synthesis_voice_name = azure_config["language_person"]
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        self.speech = speech_synthesizer

    def get_voice(self, text):
        voice_res = self.speech.speak_text_async(text).get()
        print(voice_res)
        if voice_res.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            stream = AudioDataStream(voice_res)
            stream.save_to_wav_file(os.path.join(os.getcwd(), 'voice_tmp', 'voice_' + self.hash_uuid + '.wav'))
            logging.info("auzre语音生成完成")
            return True
        elif voice_res.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = voice_res.cancellation_details
            logging.warning(cancellation_details.reason)
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    logging.error(cancellation_details.error_details)
                    logging.warning("Did you update the subscription info?")
            return False

    def azure_voice(self, text, hash_uuid):
        self.hash_uuid = hash_uuid
        self.set_config()
        return self.get_voice(text)


def save_azure_wav(text, hash_uuid):
    azure = Azure()
    try:
        azure.azure_voice(text, hash_uuid)
        return True
    except Exception:
        traceback.print_exc()
        return False
