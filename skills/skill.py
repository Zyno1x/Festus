from engines import tts


class Skill:
    skill_class = {}
    skill_entity = {}

    @staticmethod
    def output(out_val, relay=None):
        tts.speak(out_val, relay)

    @classmethod
    def skill_out(cls, intent, arg1=None):
        skill = cls.skill_class.get(intent)
        skill.output(arg1)

    @classmethod
    def init_all(cls):
        from skills.TimeSkill import time
        from skills.DateSkill import date
