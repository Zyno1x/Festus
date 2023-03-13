import os
import asyncio
import edge_tts
import playsound
from utils import logger
import settings


def init(online):
    global online_connected
    online_connected = online


async def edge_speak(text):
    communicate = edge_tts.Communicate(text=text, voice="en-US-EricNeural")
    await communicate.save("output.mp3")
    playsound.playsound("output.mp3")


def mimic_speak(text):
    os.system(
        f"lib/mimic1/./mimic --setf duration_stretch=1.2 -t \"{text}\"")


def speak(text, relay=None):
    logger.info(f"{settings.name}: {text}")

    if relay:
        print(f"{settings.name}: {relay}")
    else:
        print(f"{settings.name}: {text}")

    if online_connected:
        asyncio.get_event_loop().run_until_complete(edge_speak(text))
    else:
        try:
            mimic_speak(text=text)
        except Exception:
            logger.error(
                "Internet Not Connected. Using Mimic1 - Mimic1 not found")
