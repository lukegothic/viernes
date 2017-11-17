function shuffle(array) {
  var currentIndex = array.length, temporaryValue, randomIndex;

  // While there remain elements to shuffle...
  while (0 !== currentIndex) {

    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}
class Game {
  constructor() {
    this.stage = 1;
    this.health = 20;
    this.maxlives = 22;
    this.actioncost = 1;
    this.actions = [];
    this.discardedactions = [];
    this.nerdactions = [];
    this.hazards = [];
    this.discardedhazards = [];
  }
}
const StageColors =  Object.freeze({
  1: "#00ff00",
  2: "#ffff00",
  3: "#ff0000",
  4: "#0000ff"
});
const Skill = Object.freeze({
  LIFE: 1,
  DRAW: 2,
  DOUBLE: 3,
  DESTROY: 4,
  BELOW: 5,
  COPY: 6,
  EASY: 7,
  SORT: 8,
  EXCHANGE: 9,
  HIGHESTISZERO: 10,
  STOP: 11
});
class Action {
  constructor(name, value, skill, aged) {
    this.name = name;
    this.value = value;
    this.skill = skill || null;
    this.aged = aged || false;
  }
}
class ActionSkill {
  constructor(skill, value) {
    this.skill = skill;
    this.value = value;
  }
}
class BaseHazard {
  constructor(name, values, freeactions) {
    this.name = name;
    this.values = values;
    this.freeactions = freeactions;
  }
}
class Hazard extends BaseHazard {
  constructor(basehazard, reward) {
    super(basehazard.name, basehazard.values, basehazard.freeactions)
    this.reward = reward;
  }
}
function setup() {
  let game = new Game();
  // deck inicio
  game.actions.push(new Action("2", 2));
  for (let i = 0; i < 2; i++) {
      game.actions.push(new Action("1", 1));
  }
  for (let i = 0; i < 8; i++) {
    game.actions.push(new Action("0", 0));
  }
  game.actions.push(new Action("0+2LIFE", 1, new ActionSkill(Skill.LIFE, 2)));
  for (let i = 0; i < 5; i++) {
      game.actions.push(new Action("-1", -1));
  }
  game.actions = shuffle(game.actions);
  // deck nerd
  nerds2 = [];
  nerds2.push(new Action("Very hungry", 0, new ActionSkill(Skill.LIFE, -2), true));
  nerds2.push(new Action("Self homicidal", -5, null, true));
  nerds2.push(new Action("Idiot", -4, null, true));
  nerds2 = shuffle(nerds2);
  game.nerdactions = game.nerdactions.concat(nerds2);
  nerds1 = [];
  nerds1.push(new Action("Very stupid", -3, null, true));
  nerds1.push(new Action("Unconcentrated", -1, null, true));
  nerds1.push(new Action("Hungry", 0, new ActionSkill(Skill.LIFE, -1), true));
  nerds1.push(new Action("Kek", -2, null, true));
  nerds1.push(new Action("Afraid", 0, new ActionSkill(Skill.HIGHESTISZERO), true));
  nerds1.push(new Action("Tired", 0, new ActionSkill(Skill.STOP), true));
  nerds1 = shuffle(nerds1);
  game.nerdactions = game.nerdactions.concat(nerds1);
  // deck hazards
  let h_cannibals = new BaseHazard("Cannibals", [5,9,14], 5);
  let h_wildanimals = new BaseHazard("Wild Animals", [4,7,11], 4);
  let h_exploredeepisland = new BaseHazard("Explore Deep Island", [2,5,8], 3);
  let h_exploreisland = new BaseHazard("Explore Island", [1,3,6], 2);
  let h_wreckboat = new BaseHazard("Wreck Boat", [0,1,3], 1);
  game.hazards.push(new Hazard(h_cannibals, new Action("Weapon", 4)));
  game.hazards.push(new Hazard(h_cannibals, new Action("Weapon", 4)));
  game.hazards.push(new Hazard(h_wildanimals, new Action("Strategy", 3, new ActionSkill(Skill.EXCHANGE, 1))));
  game.hazards.push(new Hazard(h_wildanimals, new Action("Vision", 3, new ActionSkill(Skill.SORT, 3))));
  game.hazards.push(new Hazard(h_wildanimals, new Action("Experience", 3, new ActionSkill(Skill.DRAW, 1))));
  game.hazards.push(new Hazard(h_wildanimals, new Action("Knowledge", 3, new ActionSkill(Skill.DESTROY, 1))));
  game.hazards.push(new Hazard(h_exploredeepisland, new Action("Repetition", 2, new ActionSkill(Skill.DOUBLE, 1))));
  game.hazards.push(new Hazard(h_exploredeepisland, new Action("Nutriment", 2, new ActionSkill(Skill.LIFE, 1))));
  game.hazards.push(new Hazard(h_exploredeepisland, new Action("Strategy", 2, new ActionSkill(Skill.EXCHANGE, 1))));
  game.hazards.push(new Hazard(h_exploredeepisland, new Action("Vision", 2, new ActionSkill(Skill.SORT, 3))));
  game.hazards.push(new Hazard(h_exploredeepisland, new Action("Knowledge", 2, new ActionSkill(Skill.DESTROY, 1))));
  game.hazards.push(new Hazard(h_exploredeepisland, new Action("Experience", 2, new ActionSkill(Skill.DRAW, 1))));
  game.hazards.push(new Hazard(h_exploreisland, new Action("Weapon", 2)));
  game.hazards.push(new Hazard(h_exploreisland, new Action("Weapon", 2)));
  game.hazards.push(new Hazard(h_exploreisland, new Action("Nutriment", 1, new ActionSkill(Skill.LIFE, 1))));
  game.hazards.push(new Hazard(h_exploreisland, new Action("Nutriment", 1, new ActionSkill(Skill.LIFE, 1))));
  game.hazards.push(new Hazard(h_exploreisland, new Action("Trick", 1, new ActionSkill(Skill.BELOW, 1))));
  game.hazards.push(new Hazard(h_exploreisland, new Action("Repetition", 1, new ActionSkill(Skill.DOUBLE, 1))));
  game.hazards.push(new Hazard(h_exploreisland, new Action("Knowledge", 1, new ActionSkill(Skill.DESTROY, 1))));
  game.hazards.push(new Hazard(h_exploreisland, new Action("Mimicry", 1, new ActionSkill(Skill.COPY, 1))));
  game.hazards.push(new Hazard(h_wreckboat, new Action("Strategy", 0, new ActionSkill(Skill.EXCHANGE, 2))));
  game.hazards.push(new Hazard(h_wreckboat, new Action("Strategy", 0, new ActionSkill(Skill.EXCHANGE, 2))));
  game.hazards.push(new Hazard(h_wreckboat, new Action("Equipment", 0, new ActionSkill(Skill.DRAW, 2))));
  game.hazards.push(new Hazard(h_wreckboat, new Action("Equipment", 0, new ActionSkill(Skill.DRAW, 2))));
  game.hazards.push(new Hazard(h_wreckboat, new Action("Nutriment", 0, new ActionSkill(Skill.LIFE, 1))));
  game.hazards.push(new Hazard(h_wreckboat, new Action("Nutriment", 0, new ActionSkill(Skill.LIFE, 1))));
  game.hazards.push(new Hazard(h_wreckboat, new Action("Mimicry", 0, new ActionSkill(Skill.COPY, 1))));
  game.hazards.push(new Hazard(h_wreckboat, new Action("Knowledge", 0, new ActionSkill(Skill.DESTROY, 1))));
  game.hazards.push(new Hazard(h_wreckboat, new Action("Trick", 0, new ActionSkill(Skill.BELOW, 1))));
  game.hazards.push(new Hazard(h_wreckboat, new Action("Reader", 0, new ActionSkill(Skill.EASY, 1))));
  game.hazards = shuffle(game.hazards);
  console.log(game);
  return game;
}
function setupUI() {
  let ui = {
    health: $("#health span"),
    skills: $("#skills ul"),
    doaction: $("#doaction"),
    scenes: {
      select: {
        bg: $("#selectHazard"),
        hazard1: {
          bg: $("#hazard1"),
          value: $("#hazard1 .value"),
          freeactions: $("#hazard1 .freeactions"),
          reward: $("#hazard1 .reward")
        },
        hazard2: {
          bg: $("#hazard2"),
          value: $("#hazard2 .value"),
          freeactions: $("#hazard2 .freeactions"),
          reward: $("#hazard2 .reward")
        }
      },
      battle: {
        bg: $("#battleHazard"),

      }
    }
  };
  return ui;
}
function showHealth() {
  $("#health span").html(game.health);
}
function showStage() {
  $(document.body).css({ "backgroundColor": StageColors[game.stage] });
}
function battleHazard(hazard) {

}
function selectHazard(hazard1, hazard2) {
  //ui.scenes.select.hazard1.bg =
  ui.scenes.select.hazard1.value.html(hazard1.values[game.stage-1]);
  ui.scenes.select.hazard1.freeactions.html(hazard1.freeactions);
  //ui.scenes.select.hazard1.reward;
  //ui.scenes.select.hazard1.bg =
  ui.scenes.select.hazard2.value.html(hazard2.values[game.stage-1]);
  ui.scenes.select.hazard2.freeactions.html(hazard2.freeactions);
  //ui.scenes.select.hazard1.reward;
  ui.scenes.select.bg.removeClass("hidden");
}
let game, ui;
(function() {
    game = setup();
    ui = setupUI();
    showHealth();
    showStage();
    // start
    /* step1:fight hazard
    #       if no hazards left, increase stage
    #       if one hazard, you can pass*/
    if (game.hazards.length === 0) {
        game.stage++;
        showStage();
        console.log("stage", game.stage);
        game.hazards = game.discardedhazards;
        random.shuffle(game.hazards);
        game.discardedhazards = [];
    }
    if (game.stage === 4) {
        console.log("piratas");
    } else {
        let hazard1 = game.hazards.pop();
        let hazard2 = null;
        if (game.hazards.length > 0) {
            hazard2 = game.hazards.pop();
        }
        selectHazard(hazard1, hazard2);
        /*
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
            console.log(len(game.hazards), len(game.discardedhazards))
            console.log(hazard)
            //step2: fight hazard
            console.log("[INTRO] Accion [ESC] Terminar")
            actions = []
            while True:
                opt = ord(msvcrt.getch())
                if opt in [13, 27]:
                    if opt == 13:
                        pass
                    elif opt == 27:
                        break
            console.log("resultadio de la ucha")
          }
        }*/
      }
}());
