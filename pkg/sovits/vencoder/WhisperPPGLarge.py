import torch
import os
from plugins.chat_voice.pkg.sovits.vencoder.encoder import SpeechEncoder
from plugins.chat_voice.pkg.sovits.vencoder.whisper.audio import log_mel_spectrogram, pad_or_trim
from plugins.chat_voice.pkg.sovits.vencoder.whisper.model import ModelDimensions, Whisper


class WhisperPPGLarge(SpeechEncoder):
    def __init__(self, vec_path=os.path.join(os.getcwd(), "plugins/chat_voice/pkg/sovits/pretrain/large-v2.pt"), device=None):
        super().__init__()
        if device is None:
            self.dev = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        else:
            self.dev = torch.device(device)
        checkpoint = torch.load(vec_path, map_location=device)
        dims = ModelDimensions(**checkpoint["dims"])
        model = Whisper(dims)
        model.load_state_dict(checkpoint["model_state_dict"])
        self.hidden_dim = dims
        self.model = model.to(self.dev)

    def encoder(self, wav):
        audio = wav
        audln = audio.shape[0]
        ppgln = audln // 320
        audio = pad_or_trim(audio)
        mel = log_mel_spectrogram(audio).to(self.dev)
        with torch.no_grad():
            ppg = self.model.encoder(mel.unsqueeze(0)).squeeze().data.cpu().float().numpy()
            ppg = torch.FloatTensor(ppg[:ppgln, ]).to(self.dev)
            return ppg[None, :, :].transpose(1, 2)
