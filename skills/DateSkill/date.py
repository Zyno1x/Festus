from skills.skill import Skill
import datetime
from lingua_franca.format import nice_date


class Date(Skill):
    @classmethod
    def init(cls, container):
        #cls.skill_intents["date"] = 'skills/DateSkill/date.intent'
        cls.skill_class["date"] = Date
        container.load_file("date", 'skills/DateSkill/date.intent')

    @classmethod
    def output(cls, arg1):
        now = datetime.datetime.now()
        date = nice_date(now)
        relayed_date = now.strftime('Today is %A, %B %-dth %Y')
        super().output(f"Today is {date}", relay=relayed_date)
