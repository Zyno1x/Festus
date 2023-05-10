import struct
import pyaudio
import pvporcupine
from pvrecorder import PvRecorder

porcupine = None
#recorder = None
pa = None
audio_stream = None

try:

  porcupine = pvporcupine.create(access_key='wc2loO2+wQFfHyzgIV0Pc0NECYrt3hMUYKw4yxVitZUfIMs4e9brEw==',
                                 keyword_paths=["../lib/Felix_en_linux_v2_1_0.ppn"])

  #recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
  # recorder.start()

  pa = pyaudio.PyAudio()

  audio_stream = pa.open(
      rate=porcupine.sample_rate,
      channels=1,
      format=pyaudio.paInt16,
      input=True,
      frames_per_buffer=porcupine.frame_length)

  while True:
    pcm = audio_stream.read(porcupine.frame_length)
    pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
    #pcm = recorder.read()

    keyword_index = porcupine.process(pcm)

    if keyword_index >= 0:
      print("Wake Word Detected")
      print("whaugw")

finally:
  if porcupine is not None:
    porcupine.delete()

    # if recorder is not None:
    #  recorder.delete()

  if audio_stream is not None:
    audio_stream.close()

  if pa is not None:
    pa.terminate()

except pvporcupine.PorcupineInvalidArgumentError as e:
  print("One or more arguments provided to Procupine is invalid!")
  raise e
except pvporcupine.PorcupineActivationError as e:
  print("Accesskey denied.")
  raise e
except pvporcupine.PorcupineActivationLimitError as e:
  print("Accesskey has reached it's temporary device limit.")
  raise e
except pvporcupine.PorcupineActivationRefusedError as e:
  print("Accesskey refused.")
  raise e
except pvporcupine.PorcupineActivationThrottledError as e:
  print("Accesskey has been throttled.")
  raise e
except pvporcupine.PorcupineError as e:
  print("Failed to initialize Porcupine.")
  raise e
except KeyboardInterrupt:
  print("Stopping")
