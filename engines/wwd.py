import struct
import pyaudio
import pvporcupine

porcupine = None
pa = None
audio_stream = None

try:
  porcupine = pvporcupine.create(access_key='wc2loO2+wQFfHyzgIV0Pc0NECYrt3hMUYKw4yxVitZUfIMs4e9brEw==',
                                 keyword_paths=["lib/Felix_en_linux_v2_1_0.ppn"])

  pa = pyaudio.PyAudio()

  audio_stream = pa.open(
      rate=porcupine.sample_rate,
      channels=1,
      format=pyaudio.paInt16,
      input=True,
      frames_per_buffer=porcupine.frame_length)

  def detect():
    pcm = audio_stream.read(porcupine.frame_length)
    pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

    keyword_index = porcupine.process(pcm)

    if keyword_index >= 0:
      print("Wake Word Detected")
      return True

  def clear():
    if porcupine is not None:
      porcupine.delete()

    if audio_stream is not None:
      audio_stream.close()

    if pa is not None:
      pa.terminate()

except:
  pass
