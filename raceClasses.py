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


def raceStatblocks(raceTag):
    elf = RaceTemplate("elf",1,1,2,2,3,3,("Fey","Darkvision"))
    if raceTag == "elf":
        return elf

def list_races():
    print("""The current races are:
    Elf,
    Orc,
    Human
    """)

def setRace():
    list_races()
    raceTag = input("Which one would you like?\n")
    return raceTag.lower()



def testImport():
    print("raceClasses import success")
