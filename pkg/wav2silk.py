import os
import logging
import av
import pilk

def to_pcm(in_path: str) -> tuple[str, int]:
    out_path = os.path.splitext(in_path)[0] + '.pcm'
    with av.open(in_path) as in_container:
        in_stream = in_container.streams.audio[0]
        sample_rate = 24000
        with av.open(out_path, 'w', 's16le') as out_container:
            out_stream = out_container.add_stream(
                'pcm_s16le',
                rate=sample_rate,
                layout='mono'
            )
            try:
                for frame in in_container.decode(in_stream):
                    frame.pts = None
                    for packet in out_stream.encode(frame):
                        out_container.mux(packet)
            except:
                pass
    return out_path, sample_rate

def convert_to_silk(media_path: str) -> str:
    pcm_path, sample_rate = to_pcm(media_path)
    silk_path = os.path.splitext(pcm_path)[0] + '.silk'
    print(pcm_path, silk_path)
    pilk.encode(pcm_path, silk_path, pcm_rate=24000, tencent=True)
    logging.debug('silk生成成功')
    return silk_path
