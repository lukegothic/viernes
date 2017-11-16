from enum import Enum
class Hazard:
    def __init__(self, name='', values=[0,0,0], reward=None):
        self.name = name
        self.values = values
        self.reward = reward
class Boss:
    def __init__(self, name='', value=0, special=None):
        self.name = name
        self.value = value
        self.special = special
class Skill(Enum):
     LIFE = 1
     DRAW = 2
     SCRY = 3
     EXCHANGE = 4
class CardSkill:
    def __init__(self, skill=None, power=1):
        self.skill = skill
        self.power = power
class Card:
    def __init__(self, name='', value=0, skill=None):
        self.name = name
        self.value = value
        self.skill = None
