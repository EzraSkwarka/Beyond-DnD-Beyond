##############
# Header Block
##############
import raceClasses

class Toon():
    def __init__(self):
        ##### Race info
        self.raceTag = ""
        self.race = ""
        self.strMod = 0
        self.dexMod = 0
        self.conMod = 0
        self.intMod = 0
        self.wisMod = 0
        self.chrMod = 0
        self.statMods = [self.strMod, self.dexMod, self.conMod, self.intMod, self.wisMod, self.chrMod]
        ##### Stat Block
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.stats = [self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma]
        self.statList=["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

    def importRaceStatMods(self):
        self.race = raceClasses.race_stat_blocks()
        self.raceTag = self.race.nameOfRace
        for i in range(6):
            self.statMods[i] = self.race.statMods[i]
            print(self.statMods[i])


    def statBlock(self):
        for i in range(6):
            self.stats[i] = int(input("set {0} to: ".format(self.statList[i])))
        print("""Your stats are: {0}, {1}, {2}, {3}, {4}, {5}""".format(*self.stats))
        ### add race mods
        ##### import stat mods
        print("adding race mods")
        for i in range(6):
            self.stats[i] += self.statMods[i]
        print("""Your stats are: {0}, {1}, {2}, {3}, {4}, {5}""".format(*self.stats))


def main():
    playerChar = Toon()

    # raceClasses.testImport()
    playerChar.importRaceStatMods()
    playerChar.statBlock()



main()
