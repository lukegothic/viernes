import msvcrt
import random
from enum import Enum
class BaseHazard:
    def __init__(self, name='', values=[0,0,0], freeactions=0):
        self.name = name
        self.values = values
        self.freeactions = freeactions
class Hazard:
    def __init__(self, basehazard=None, reward=None):
        self.name = basehazard.name
        self.values = basehazard.values
        self.freeactions = basehazard.freeactions
        self.reward = reward
    def __str__(self):
        return "{} VALUE:{} ACTIONS:{} REWARD:{}".format(self.name, self.values[game.stage-1], self.freeactions, self.reward)
# class Pirate:
#     def __init__(self, value=0, freeactions=0, special=None):
#         self.value = value
#         self.freeactions = freeactions
#         self.special = special
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
    def __str__(self):
        return "{} {}".format(self.skill.name, self.value)
class Action:
    def __init__(self, name='', value=0, skill=None, aged=False):
        self.name = name
        self.value = value
        self.skill = skill
        self.aged = aged
    def __str__(self):
        return ("{} VALUE:{} {}".format(self.name, self.value, "SKILL:{}".format(self.skill) if not self.skill is None else ""))
class Game:
    def __init__(self):
        pass
game = Game()
def setup():
    game.stage = 1
    game.lives = 20
    game.maxlives = 22
    game.actioncost = 1
    # deck inicio
    game.actions = []
    game.discardedactions = []
    game.actions.append(Action("2", 2))
    for i in range(2):
        game.actions.append(Action("1", 1))
    for i in range(8):
        game.actions.append(Action("0", 0))
    game.actions.append(Action("02LIFE", 1, ActionSkill(Skill.LIFE, 2)))
    for i in range(5):
        game.actions.append(Action("-1", -1))
    random.shuffle(game.actions)
    # deck nerd
    game.nerdactions = []
    nerds1 = []
    nerds1.append(Action("Hungry", 0, ActionSkill(Skill.LIFE, -1), True))
    nerds1.append(Action("Unconcentrated", -1, None, True))
    nerds1.append(Action("Afraid", 0, ActionSkill(Skill.HIGHESTISZERO), True))
    nerds1.append(Action("Tired", 0, ActionSkill(Skill.STOP), True))
    nerds1.append(Action("Very stupid", -3, None, True))
    random.shuffle(nerds1)
    game.nerdactions.extend(nerds1)
    nerds2 = []
    nerds2.append(Action("Very hungry", 0, ActionSkill(Skill.LIFE, -2), True))
    nerds2.append(Action("Self homicidal", -5, None, True))
    nerds2.append(Action("Idiot", -4, None, True))
    random.shuffle(nerds2)
    game.nerdactions.extend(nerds2)
    # deck hazards
    game.hazards = []
    game.discardedhazards = []
    h_cannibals = BaseHazard("Cannibals", [5,9,14], 5)
    h_wildanimals = BaseHazard("Wild Animals", [4,7,11], 4)
    h_exploredeepisland = BaseHazard("Explore Deep Island", [2,5,8], 3)
    h_exploreisland = BaseHazard("Explore Island", [1,3,6], 2)
    h_wreckboat = BaseHazard("Wreck Boat", [0,1,3], 1)
    game.hazards.append(Hazard(h_cannibals, Action(Action("Weapon", 4))))
    game.hazards.append(Hazard(h_cannibals, Action(Action("Weapon", 4))))
    game.hazards.append(Hazard(h_wildanimals, Action("Strategy", 3, ActionSkill(Skill.EXCHANGE, 1))))
    game.hazards.append(Hazard(h_wildanimals, Action("Vision", 3, ActionSkill(Skill.SORT, 3))))
    game.hazards.append(Hazard(h_wildanimals, Action("Experience", 3, ActionSkill(Skill.DRAW, 1))))
    game.hazards.append(Hazard(h_wildanimals, Action("Knowledge", 3, ActionSkill(Skill.DESTROY, 1))))
    game.hazards.append(Hazard(h_exploredeepisland, Action("Repetition", 2, ActionSkill(Skill.DOUBLE, 1))))
    game.hazards.append(Hazard(h_exploredeepisland, Action("Nutriment", 2, ActionSkill(Skill.LIFE, 1))))
    game.hazards.append(Hazard(h_exploredeepisland, Action("Strategy", 2, ActionSkill(Skill.EXCHANGE, 1))))
    game.hazards.append(Hazard(h_exploredeepisland, Action("Vision", 2, ActionSkill(Skill.SORT, 3))))
    game.hazards.append(Hazard(h_exploredeepisland, Action("Knowledge", 2, ActionSkill(Skill.DESTROY, 1))))
    game.hazards.append(Hazard(h_exploredeepisland, Action("Experience", 2, ActionSkill(Skill.DRAW, 1))))
    game.hazards.append(Hazard(h_exploreisland, Action("Weapon", 2)))
    game.hazards.append(Hazard(h_exploreisland, Action("Weapon", 2)))
    game.hazards.append(Hazard(h_exploreisland, Action("Nutriment", 1, ActionSkill(Skill.LIFE, 1))))
    game.hazards.append(Hazard(h_exploreisland, Action("Nutriment", 1, ActionSkill(Skill.LIFE, 1))))
    game.hazards.append(Hazard(h_exploreisland, Action("Trick", 1, ActionSkill(Skill.BELOW, 1))))
    game.hazards.append(Hazard(h_exploreisland, Action("Repetition", 1, ActionSkill(Skill.DOUBLE, 1))))
    game.hazards.append(Hazard(h_exploreisland, Action("Knowledge", 1, ActionSkill(Skill.DESTROY, 1))))
    game.hazards.append(Hazard(h_exploreisland, Action("Mimicry", 1, ActionSkill(Skill.COPY, 1))))
    game.hazards.append(Hazard(h_wreckboat, Action("Strategy", 0, ActionSkill(Skill.EXCHANGE, 2))))
    game.hazards.append(Hazard(h_wreckboat, Action("Strategy", 0, ActionSkill(Skill.EXCHANGE, 2))))
    game.hazards.append(Hazard(h_wreckboat, Action("Equipment", 0, ActionSkill(Skill.DRAW, 2))))
    game.hazards.append(Hazard(h_wreckboat, Action("Equipment", 0, ActionSkill(Skill.DRAW, 2))))
    game.hazards.append(Hazard(h_wreckboat, Action("Nutriment", 0, ActionSkill(Skill.LIFE, 1))))
    game.hazards.append(Hazard(h_wreckboat, Action("Nutriment", 0, ActionSkill(Skill.LIFE, 1))))
    game.hazards.append(Hazard(h_wreckboat, Action("Mimicry", 0, ActionSkill(Skill.COPY, 1))))
    game.hazards.append(Hazard(h_wreckboat, Action("Knowledge", 0, ActionSkill(Skill.DESTROY, 1))))
    game.hazards.append(Hazard(h_wreckboat, Action("Trick", 0, ActionSkill(Skill.BELOW, 1))))
    game.hazards.append(Hazard(h_wreckboat, Action("Reader", 0, ActionSkill(Skill.EASY, 1))))
    random.shuffle(game.hazards)
    # deck pirates
    # pirates = []
    # pirates.append(Pirate(20, 6))
    # pirates.append(Pirate(25, 7))
    # pirates.append(Pirate(30, 8))
    # pirates.append(Pirate(35, 9))
    # pirates.append(Pirate(40, 10))
def play():
    # step1:fight hazard
    #       if no hazards left, increase stage
    #       if one hazard, you can pass
    while True:
        if len(game.hazards) == 0:
            game.stage += 1
            print("stage", game.stage)
            game.hazards = game.discardedhazards
            random.shuffle(game.hazards)
            game.discardedhazards = []
        if game.stage == 4:
            #todo: piratas
            print("piratas")
            pass
        else:
            hazard1 = game.hazards.pop(len(game.hazards)-1)
            if len(game.hazards) > 0:
                hazard2 = game.hazards.pop(len(game.hazards)-1)
            else:
                hazard2 = None
            print("=Enfréntate a un PELIGRO=")
            print("[1] {}".format(hazard1))
            if hazard2 is None:
                print("[2] Escurrir el bulto")
            else:
                print("[2] {}".format(hazard2))
            while True:
                opt = ord(msvcrt.getch())
                if opt in [49, 50]:
                    break
            if opt == 50 and hazard2 is None:
                # si optamos por no luchar, simplemente descartamos el peligro
                game.discardedhazards.append(hazard1)
            else:
                if opt == 49:
                    hazard = hazard1
                    game.discardedhazards.append(hazard2)
                else:
                    hazard = hazard2
                    game.discardedhazards.append(hazard1)
                #print(len(game.hazards), len(game.discardedhazards))
                print(hazard)
                #step2: fight hazard
                print("[INTRO] Accion [ESC] Terminar")
                actions = []
                while True:
                    opt = ord(msvcrt.getch())
                    if opt in [13, 27]:
                        if opt == 13:
                            pass
                        elif opt == 27:
                            break
                print("resultadio de la ucha")

def restart():
    setup()
    play()
restart()
