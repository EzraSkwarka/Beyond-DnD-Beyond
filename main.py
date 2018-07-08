##############
# Header Block
##############
import raceClasses
import raceTraits

class Toon:
    def __init__(self):
        # ### Biography info
        self.playerName = ""
        self.characterName = ""
        # ### Race info
        self.raceTag = ""
        self.race = ""
        self.strMod = 0
        self.dexMod = 0
        self.conMod = 0
        self.intMod = 0
        self.wisMod = 0
        self.chrMod = 0
        self.statMods = [self.strMod, self.dexMod, self.conMod, self.intMod, self.wisMod, self.chrMod]
        self.raceTraits = None
        # ### Stat Block
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.stats = [self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma]
        self.statList = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        # ### Class Info

    def set_names(self):
        # Player Name
        self.playerName = input("What is your name?\n")
        while True:
            print("Ah, so your name is {0}.".format(self.playerName))
            temp = input("Is that correct? (Yes/No)\n").lower()
            if temp == "yes":
                break
            else:
                self.playerName = input("I'm very sorry I misunderstood. So then, what is your name?\n")
        # Character Name
        print("awesome, now that I know your name {0}, I need to know what your character is named.".format(self.playerName))
        self.characterName = input("What is your character's name?")
        while True:
            print("Ah, so their name is {0}.".format(self.characterName))
            temp = input("is that correct? (Yes/No)").lower()
            if temp == "yes":
                break
            else:
                self.characterName = input("I'm very sorry I misunderstood. So then, what is your character's name?")

    def import_race_stat_mods(self):
        """
        Pulls the stat modifiers from the raceClasses.py file and writes them into the toon class under stat mods.
        :return: None
        """
        self.race = raceClasses.set_race()
        self.raceTag = self.race.nameOfRace
        for i in range(6):
            self.statMods[i] = self.race.statMods[i]
        self.raceTraits = self.race.racialAbilities
        # for i, val in range(len(self.raceTraits)):
        #     print(self.raceTraits)

    def apply_race_stat_mods(self):
        """
        Pulls the racial mod info from the toon race stat block and adds the modifiers to the toon stat block. Still needs polish
        :return: None
        """
        print("adding race mods")
        for i in range(6):
            self.stats[i] += self.statMods[i]
        print("""Your stats are: {0}, {1}, {2}, {3}, {4}, {5}""".format(*self.stats))

    def set_toon_stat_block(self):
        """
        When called opens the console to set the stat block using input. As of now will error out if the user does not input an int. Does not apply racial mods. Still needs polish.
        :return:
        """
        for i in range(6):  # TODO: Set input to not error out on non-int input
            self.stats[i] = int(input("set {0} to: ".format(self.statList[i])))
        print("""Your stats are: {0}, {1}, {2}, {3}, {4}, {5}""".format(*self.stats))

    # def get_race_traits(self):
    #     self.race = raceClasses
    #     self.raceTraits = self.race.racialAbilities()


def main():
    playerChar = Toon()
    # print("at some point, this will be an introductory schpeel.")
    # playerChar.set_names()
    playerChar.import_race_stat_mods()
    playerChar.set_toon_stat_block()
    playerChar.apply_race_stat_mods()
    # playerChar.get_race_traits()


main()
