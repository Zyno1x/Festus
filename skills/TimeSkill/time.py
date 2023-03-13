from skills.skill import Skill
from lingua_franca.format import nice_time
import datetime


class Time(Skill):
    @classmethod
    def init(cls, container):
        #cls.skill_intents["time"] = 'skills/TimeSkill/time.intent'
        cls.skill_class["time"] = Time
        container.load_file("time", 'skills/TimeSkill/time.intent')

    @classmethod
    def output(cls, arg1):
        now = datetime.datetime.now()
        time = now.strftime('%I:%M %p')
        super().output(f"The Time is {time}")
