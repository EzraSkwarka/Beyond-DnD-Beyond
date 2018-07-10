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
        self.strModRace = 0
        self.dexModRace = 0
        self.conModRace = 0
        self.intModRace = 0
        self.wisModRace = 0
        self.chrModRace = 0
        self.statModsRace = [self.strModRace, self.dexModRace, self.conModRace, self.intModRace, self.wisModRace, self.chrModRace]
        self.subrace = None
        self.raceTraits = []


        # ### Stat Block
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        self.stats = [self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma]
        self.statList = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
        self.strMod = 0
        self.dexMod = 0
        self.conMod = 0
        self.intMod = 0
        self.wisMod = 0
        self.chrMod = 0
        self.statMods = [self.strMod, self.dexMod, self.conMod, self.intMod, self.wisMod, self.chrMod]
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

    def import_race_information(self):
        """
        Pulls the stat modifiers from the raceClasses.py file and writes them into the toon class under stat mods.
        :return: None
        """
        self.race = raceClasses.set_race()
        self.raceTag = self.race.nameOfRace
        if self.race.hasSubrace:
            self.subrace = raceClasses.get_sub_race(self.raceTag)
            for i in range(6):
                self.statModsRace[i] += self.subrace.statMods[i]
                # print("your racial stat modifier is {0}".format(self.subrace.statMods[i]))
        for i in range(6):
            self.statModsRace[i] += self.race.statMods[i]
        for i in range(len(self.race.racialAbilities)):
            self.raceTraits.append(self.race.racialAbilities[i])
        if self.race.hasSubrace:
            for i in range(len(self.subrace.racialAbilities)):
                self.raceTraits.append(self.subrace.racialAbilities[i])

    def apply_race_stat_mods(self):
        """
        Pulls the racial mod info from the toon race stat block and adds the modifiers to the toon stat block. Still needs polish
        :return: None
        """
        print("adding race mods")
        for i in range(6):
            self.stats[i] += self.statModsRace[i]
        print("""Your stats are: {0}, {1}, {2}, {3}, {4}, {5}""".format(*self.stats))

    def set_toon_stat_block(self):
        """
        When called opens the console to set the stat block using input. As of now will error out if the user does not input an int. Does not apply racial mods. Still needs polish.
        :return:
        """
        for i in range(6):

            temp = input("set {0} to: ".format(self.statList[i]))
            if temp.isdigit():
                temp = int(temp)
            while type(temp) != int:
                print("That has to be a number. Try again")
                temp = input("set {0} to: ".format(self.statList[i]))
                if temp.isdigit():
                    temp = int(temp)
            self.stats[i] = temp
        print("""Your stats are: {0}, {1}, {2}, {3}, {4}, {5}""".format(*self.stats))

    def set_stat_modifiers(self, score):
        if score % 2 != 0:
            score -= 1
        modifier = int(-5 + score / 2)
        if modifier > 10:
            modifier = 10
        print("the modifier is: {0}".format(str(modifier)))
        return modifier

    def create_character_sheet(self):
        pass

def main():
    playerChar = Toon()
    # print("at some point, this will be an introductory schpeel.")
    # playerChar.set_names()
    playerChar.import_race_information()
    playerChar.set_toon_stat_block()
    playerChar.apply_race_stat_mods()
    for stat in playerChar.stats:
        playerChar.statMods = playerChar.set_stat_modifiers(stat)


main()
