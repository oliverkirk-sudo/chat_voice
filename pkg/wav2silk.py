import os, pilk
from pydub import AudioSegment


def convert_to_silk(media_path: str) -> str:
    media = AudioSegment.from_file(media_path)
    name = os.path.basename(media_path).split('.')[0]
    pcm_path = os.path.dirname(media_path)
    silk_path = os.path.join(pcm_path, (name + '.silk'))
    pcm_path = os.path.join(pcm_path, (name + '.pcm'))
    media.export(pcm_path, 's16le', parameters=['-ar', str(32000), '-ac', '1']).close()
    pilk.encode(pcm_path, silk_path, pcm_rate=32000, tencent=True)
    print('silk生成成功')
    return silk_path
