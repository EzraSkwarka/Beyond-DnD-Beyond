##############
# Header Block
# Keep stats for races and refrence race traits, info for the traits in race traits page
##############
import raceTraits


class RaceTemplate:
    def __init__(self, race_tag, str_mod, dex_mod, con_mod, int_mod, wis_mod, chr_mod, racial_abilities=()):
        self.nameOfRace = race_tag
        self.strMod = str_mod
        self.dexMod = dex_mod
        self.conMod = con_mod
        self.intMod = int_mod
        self.wisMod = wis_mod
        self.chrMod = chr_mod
        self.statMods = [self.strMod, self.dexMod, self.conMod, self.intMod, self.wisMod, self.chrMod]
        self.racialAbilities = racial_abilities


def race_stat_blocks():
    race = None
    race_tag = input("Which one would you like?\n")
    if race_tag == "list races":
        list_races()
        race = None
        race_stat_blocks()
    elif race_tag == "dwarf":
        race = RaceTemplate(race_tag, 0, 0, 2, 0, 0, 0, ("Fey", "Darkvision"))
    elif race_tag == "elf":
        race = RaceTemplate(race_tag, 0, 2, 0, 0, 0, 0, ("Fey", "Darkvision"))
    elif race_tag == "halfling":
        race = RaceTemplate(race_tag, 0, 2, 0, 0, 0, 0, "")
    elif race_tag == "human":
        race = RaceTemplate(race_tag, 0, 2, 0, 0, 0, 0, ("Fey", "Darkvision"))
    elif race_tag == "half-orc":
        race = RaceTemplate(race_tag, 2, 0, 1, 0, 0, 0, ("Fey", "Darkvision"))
    elif race_tag == "dragonborn":
        race = RaceTemplate(race_tag, 2, 0, 0, 0, 0, 1, ("Fey", "Darkvision"))
    elif race_tag == "gnome":
        race = RaceTemplate(race_tag, 0, 0, 0, 2, 0, 0, ("Fey", "Darkvision"))
    elif race_tag == "half-elf":
        race = RaceTemplate(race_tag, 0, 0, 0, 0, 0, 2, ("Fey", "Darkvision"))
        # ##CAN CHOOSE TWO OTHERS TO INCREASE
        print("You chose a half elf so you can increase two additional stats by one, but I haven't implemented that yet. :(")
    elif race_tag == "tiefling":
        race = RaceTemplate(race_tag, 0, 0, 0, 1, 0, 2, ("Fey", "Darkvision"))
    else:
        print("I did not understand that. PLease try again. or type lsit races to see the list of races.")
        race = None
        race_stat_blocks()

    if race is not None and race != "list races":
        return race


def list_races():
    print("""The current races are:
    Dwarf,
    Elf,
    Halfling,
    Human,
    Dragonborn,
    Gnome,
    Half-Elf,
    Half-Orc,
    Tiefling""")
