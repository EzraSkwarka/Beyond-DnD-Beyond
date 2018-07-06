##############
# Header Block
# Keep stats for races and refrence race traits, info for the traits in race traits page
##############
import raceTraits


class RaceTemplate:
    def __init__(self, raceTag, strMod, dexMod, conMod, intMod, wisMod, chrMod, racialAbilities = ()):
        self.nameOfRace = raceTag
        self.strMod = strMod
        self.dexMod = dexMod
        self.conMod = conMod
        self.intMod = intMod
        self.wisMod = wisMod
        self.chrMod = chrMod
        self.statMods = [self.strMod, self.dexMod, self.conMod, self.intMod, self.wisMod, self.chrMod]
        self.racialAbilities = racialAbilities


def raceStatblocks():
    race = None
    raceTag = input("Which one would you like?\n")
    if raceTag == "list races":
        list_races()
        race = None
        raceStatblocks()
    elif raceTag == "dwarf":
        race = RaceTemplate(raceTag,0,0,2,0,0,0,("Fey","Darkvision"))
    elif raceTag == "elf":
        race = RaceTemplate(raceTag,0,2,0,0,0,0,("Fey","Darkvision"))
    elif raceTag == "halfling":
        race = RaceTemplate(raceTag,0,2,0,0,0,0,(""))
    elif raceTag == "human":
        race = RaceTemplate(raceTag,0,2,0,0,0,0,("Fey","Darkvision"))
    elif raceTag== "half-orc":
        race = RaceTemplate(raceTag,2,0,1,0,0,0,("Fey","Darkvision"))
    elif raceTag == "dragonborn":
        race = RaceTemplate(raceTag,2,0,0,0,0,1,("Fey","Darkvision"))
    elif raceTag == "gnome":
        race = RaceTemplate(raceTag,0,0,0,2,0,0,("Fey","Darkvision"))
    elif raceTag == "half-elf":
        race = RaceTemplate(raceTag,0,0,0,0,0,2,("Fey","Darkvision"))
        ###CAN CHOOSE TWO OTHERS TO INCREASE
        print("You chose a half elf so you can increase two additional stats by one, but I haven't implemented that yet. :(")
    elif raceTag == "tiefling":
        race = RaceTemplate(raceTag,0,0,0,1,0,2,("Fey","Darkvision"))
    else:
        print("I did not understand that. PLease try again. or type lsit races to see the list of races.")
        race = None
        raceStatblocks()

    if race != None and race != "list races":
        return race

def list_races():
    print("""The current races are:
    Elf,
    Half-Orc,
    Human""")

def setRace():
    return raceTag.lower()



def testImport():
    print("raceClasses import success")
