from padatious.intent_container import IntentContainer
from skills.skill import Skill


def init():
    global container
    container = IntentContainer("lib/intent_cache")

    for skill in Skill.__subclasses__():
        skill.init(container)

    container.train()
