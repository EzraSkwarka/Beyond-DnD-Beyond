##############
# Header Block
# Keep stats for races and reference race traits, info for the traits in race traits page
##############
import raceTraits


class RaceTemplate:
    def __init__(self, race_tag, str_mod, dex_mod, con_mod, int_mod, wis_mod, chr_mod, racial_abilities):
        self.nameOfRace = race_tag
        self.strMod = str_mod
        self.dexMod = dex_mod
        self.conMod = con_mod
        self.intMod = int_mod
        self.wisMod = wis_mod
        self.chrMod = chr_mod
        self.statMods = [self.strMod, self.dexMod, self.conMod, self.intMod, self.wisMod, self.chrMod]
        self.racialAbilities = racial_abilities


def set_race():
    race = None
    race_tag = input("Which race would you like your character to be?\n")
    if race_tag == "list races":
        list_races()
        race = None
        set_race()
    elif type(race_tag) == str and race_tag != "list races":
        race = races[race_tag]
    else:
        print("I did not understand that. PLease try again. or type lsit races to see the list of races.")
        race = None
        set_race()

    if race is not None and race != "list races":
        return race


races = {
    "debug race": RaceTemplate("debug race", 1, 2, 3, 4, 5, 100, "darkvision"),
    "dwarf": RaceTemplate("dwarf", 0, 0, 2, 0, 0, 0, ["Fey", "Darkvision"]),
    "elf": RaceTemplate("elf", 0, 2, 0, 0, 0, 0, ("Fey", "Darkvision")),
    "halfling": RaceTemplate("halfling", 0, 2, 0, 0, 0, 0, ""),
    "human": RaceTemplate("human", 0, 2, 0, 0, 0, 0, ("Fey", "Darkvision")),
    "half-orc": RaceTemplate("half-orc", 2, 0, 1, 0, 0, 0, ("Fey", "Darkvision")),
    "dragonborn": RaceTemplate("dragonborn", 2, 0, 0, 0, 0, 1, ("Fey", "Darkvision")),
    "gnome": RaceTemplate("gnome", 0, 0, 0, 2, 0, 0, ("Fey", "Darkvision")),
    "half-elf": RaceTemplate("half-elf", 0, 0, 0, 0, 0, 2, ("Fey", "Darkvision")),
    # ##CAN CHOOSE TWO OTHERS TO INCREASE
    "tiefling": RaceTemplate("tiefling", 0, 0, 0, 1, 0, 2, ("Fey", "Darkvision"))




}
def list_races():
    print("The current races are:")
    for key, value in races:
        print(key)
