from enum import Enum
class Hazard:
    def __init__(self, name='', values=[0,0,0], freeactions=0, reward=None):
        self.name = name
        self.values = values
        self.freeactions = freeactions
        self.reward = reward
class Pirate:
    def __init__(self, name='', value=0, special=None):
        self.name = name
        self.value = value
        self.special = special
class Skill(Enum):
     LIFE = 1
     DRAW = 2
     DOUBLE = 3
     DESTROY = 4
     BELOW = 5
     COPY = 6
     EASY = 7
     SORT = 8
     EXCHANGE = 9
     HIGHESTISZERO = 10
     STOP = 11
class ActionSkill:
    def __init__(self, skill=None, value=1):
        self.skill = skill
        self.value = value
class Action:
    def __init__(self, name='', value=0, skill=None, age=0):
        self.name = name
        self.value = value
        self.skill = None
        self.age = age
def start():
    stage = 1
    lives = 20
    # deck inicio
    actions = []
    actions.append(Action("2", 2))
    for i in range(2):
        actions.append(Action("1", 1))
    for i in range(8):
        actions.append(Action("0", 0))
    actions.append(Action("02LIFE", 1, ActionSkill(Skill.LIFE, 2)))
    for i in range(5):
        actions.append(Action("-1", -1))
    print(vars(actions[0]))
start()
