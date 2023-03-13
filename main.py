from skills.skill import Skill
from utils import logger
import settings
from utils import internet

if settings.online is None:
    settings.online = internet.conected()

logger.init()
Skill.init_all()

from engines import nlu, wwd, stt, tts, ttt

nlu.init()
ttt.init()
tts.init(settings.online)


def main():
    if wwd.detect():

        speech = stt.listen_speech()
        data = nlu.container.calc_intent(speech)
        # print(data.conf)

        if data.conf > 0.6:
            Skill.skill_out(intent=data.name, arg1=data.matches.get(
                Skill.skill_entity.get(data.name)))
            return


try:
    if __name__ == "__main__":
        while True:
            main()

finally:
    wwd.clear()
