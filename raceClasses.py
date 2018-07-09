##############
# Header Block
# Keep stats for races and reference race traits, info for the traits in race traits page
##############
from raceTraits import traitDictionary as traitDict

class RaceTemplate:
    def __init__(self, race_tag, str_mod, dex_mod, con_mod, int_mod, wis_mod, chr_mod, racial_abilities, subraces=False):
        self.nameOfRace = race_tag
        self.strMod = str_mod
        self.dexMod = dex_mod
        self.conMod = con_mod
        self.intMod = int_mod
        self.wisMod = wis_mod
        self.chrMod = chr_mod
        self.statMods = [self.strMod, self.dexMod, self.conMod, self.intMod, self.wisMod, self.chrMod]
        self.racialAbilities = racial_abilities
        self.hasSubrace = subraces

class SubRaceTemplate:
    def __init__(self, race_tag, str_mod, dex_mod, con_mod, int_mod, wis_mod, chr_mod, racial_abilities):
        self.nameOfSubRace = race_tag
        self.strModSub = str_mod
        self.dexModSub = dex_mod
        self.conModSub = con_mod
        self.intModSub = int_mod
        self.wisModSub = wis_mod
        self.chrModSub = chr_mod
        self.statMods = [self.strModSub, self.dexModSub, self.conModSub, self.intModSub, self.wisModSub, self.chrModSub]
        self.racialAbilities = racial_abilities


def set_race():
    """
    Asks and sets player race, can list if asked. Case and white space insensitive.
    :return: race class using RaceTemplate
    """
    race = None
    while race is None:
        race_tag = str(input("Which race would you like your character to be?\n"))
        if type(race_tag) == str:
            race_tag = race_tag.lower().replace(" ", "")
        did_list = False
        if race_tag == "listraces":
            list_races()
            did_list = True
            # set_race()
        elif type(race_tag) == str and race_tag != "listraces" and race_tag in races:
            race = races[race_tag]
        if race is None and not did_list:
            print("I did not understand that. PLease try again, or type list races to see the list of races.")
    if race is not None and race != "list races":
        return race


def get_sub_race(major_race):
    """
    Asks and sets player subrace, can list if asked. Case and white space insensitive.
    :param major_race: players race
    :return: race class using SubRaceTemplate
    """
    subrace = None
    race = major_race
    while subrace is None:
        race_tag = str(input("Which subrace would you like your character to be?\n"))
        if type(race_tag) == str:
            race_tag = race_tag.lower().replace(" ", "")
        did_list = False
        if race_tag == "list subraces":
            list_subraces(race)
            did_list = True
        elif type(race_tag) == str and race_tag in subraces[str(race)]:
            subrace = subraces[race][race_tag]
        if subrace is None and not did_list:
            print("I did not understand that. PLease try again, or type list races to see the list of races.")
    if subrace is not None and subrace != "list races":
        return subrace


races = {
    "debugrace": RaceTemplate("debugrace", 1, 2, 3, 4, 5, 100, traitDict[(0, 0)], True),
    "dwarf": RaceTemplate("dwarf", 0, 0, 2, 0, 0, 0, ["Fey", "Darkvision"]),
    "elf": RaceTemplate("elf", 0, 2, 0, 0, 0, 0, ("Fey", "Darkvision")),
    "halfling": RaceTemplate("halfling", 0, 2, 0, 0, 0, 0, ""),
    "human": RaceTemplate("human", 0, 2, 0, 0, 0, 0, ("Fey", "Darkvision")),
    "half-orc": RaceTemplate("half-orc", 2, 0, 1, 0, 0, 0, ("Fey", "Darkvision")),
    "dragonborn": RaceTemplate("dragonborn", 2, 0, 0, 0, 0, 1, ("Fey", "Darkvision")),
    "gnome": RaceTemplate("gnome", 0, 0, 0, 2, 0, 0, ("Fey", "Darkvision")),
    "half-elf": RaceTemplate("half-elf", 0, 0, 0, 0, 0, 2, ("Fey", "Darkvision")),    # ##CAN CHOOSE TWO OTHERS TO INCREASE
    "tiefling": RaceTemplate("tiefling", 0, 0, 0, 1, 0, 2, ("Fey", "Darkvision"))
}

subraces = {
    "debugrace": {"subraceA": SubRaceTemplate("Debug Sub Race A", 0, 0, 0, 0, 12, 13, "fey"),
                  "subraceB": SubRaceTemplate("Debug Sub Race B", 0, 0, 0, 0, 12, 13, "fey")}


}


def list_races():
    """
    Helper function. Lists all keys in races dict
    :return: None
    """
    print("The currently supported races are:")
    for key in races:
        print(key)

def list_subraces(subrace):
    """
    Helper function. Lists all keys in subraces dict's nested subrace passed in
    :param subrace: key to locate nested dictionary
    :return: None
    """
    print("The currently supported subraces are:")
    temp_dict = subraces[subrace]
    for key in temp_dict:
        print(key)

