##############
# Header Block
##############


class TraitTemplate:
    def __init__(self, name, race, id, des):
        self.traitName = name
        self.traitRace = race
        self.traitId = id
        self.traitDescription = des
        self.list = [self.traitName, self.traitRace, self.traitId, self.traitDescription]


traitDictionary = {
    # Debug Race (0, X)
    (0, 0): TraitTemplate("test trait 1", "debug race", (0, 0), "test trait 1 des"),
    (0, 1): TraitTemplate("test trait 2", "debug race", (0, 1), "test trait 2 des"),
    # Dwarf Races (1, X)
    # # Dwarf
    (1, 0): TraitTemplate("Ability Score Increase", "dwarf", (1, 0), "Your Constitution score increases by 2."),
    (1, 1): TraitTemplate("Age", "dwarf", (1, 1), "Dwarves mature at the sam e rate as humans, but they’re considered young until they reach the age of 50. On average, they live about 350 years."),
    (1, 2): TraitTemplate("Alignment", "dwarf", (1, 2), "Most dwarves are lawful, believing firmly in the benefits of a well-ordered society. They tend toward good as well, with a strong sense of fair play and a belief that everyone deserves  to share in the benefits of a just order"),
    (1, 3): TraitTemplate("Size", "dwarf", (1, 3), "Dwarves stand between 4 and 5 feet tall and average about 150 pounds. Your size is Medium."),
    (1, 4): TraitTemplate("Speed", "dwarf", (1, 4), "Your base walking speed is 25 feet. Your speed is not reduced by w earing heavy armor."),
    (1, 5): TraitTemplate("Darkvision", "dwarf", (1, 5), "Accustomed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it w ere dim light. You can’t discern color in darkness, only shades of gray."),
    (1, 6): TraitTemplate("Dwarven Resilience", "dwarf", (1, 6), "You have advantage on saving throws against poison, and you have resistance against poison damage (explained in chapter 9)."),
    (1, 7): TraitTemplate("Dwarven Combat Training", "dwarf", (1, 7), "You have proficiency with the battleaxe, handaxe, throwing hammer, and warhammer."),
    (1, 8): TraitTemplate("Tool Proficiency", "dwarf", (1, 8), "You gain proficiency with the artisan’s tools of your choice: smith’s tools, brew er’s supplies, or m ason’s ."),
    (1, 9): TraitTemplate("Stonecunning", "dwarf", (1, 9), "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."),
    (1, 10): TraitTemplate("Languages", "dwarf", (1, 10), "You can speak, read, and write Com m on and Dwarvish. Dwarvish is full of hard consonants and guttural sounds, and those characteristics spill over into whatever other language a dw arf might speak."),
    (1, 11): TraitTemplate("Subrace", "dwarf", (1, 11), "Two main subraces o f dwarves populate the worlds of D&D: hill dwarves and mountain dwarves. Choose one of these subraces."),
    # ### Hill Dwarf
    (1, 12): TraitTemplate("Ability Score Increase", "dwarf", (1, 12), "Your Wisdom score increases by 1."),
    (1, 13): TraitTemplate("Dwarven Toughness", "dwarf", (1, 13), "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."),
    # ### Mountain Dwarf
    (1, 14): TraitTemplate("Ability Score Increase", "dwarf", (1, 14), "Your Strength score increases by 2."),
    (1, 15): TraitTemplate("Dwarven Armor Training", "dwarf", (1, 15), "You have proficiency with light and medium armor."),

    # # Elf
    (2, 0): TraitTemplate("Ability Score Increase", "elf", (2, 0), "Your Dexterity score increases by 2."),
    (2, 1): TraitTemplate("Age", "elf", (2, 1), "Although elves reach physical maturity at about the sam e age as humans, the elven understanding of adulthood goes beyond physical growth to encom pass worldly experience. An elf typically claim s adulthood and an adult name around the age of 100 and can live to be 750 years old."),
    (2, 2): TraitTemplate("Alignment", "elf", (2, 2), "Elves love freedom , variety, and selfexpression, so they lean strongly toward the gentler aspects of chaos. They value and protect others' freedom as well as their own, and they are more often good than not. The drow are an exception; their exile into the Underdark has made them vicious and dangerous. D row are m ore often evil than not."),
    (2, 3): TraitTemplate("Size", "elf", (2, 3), "Elves range from under 5 to over 6 feet tall and have slender builds. Your size is ."),
    (2, 4): TraitTemplate("Speed", "elf", (2, 4), "Your base walking speed is 30 feet."),
    (2, 5): TraitTemplate("Darkvision", "elf", (2, 5), "Accustom ed to twilit forests and the night sky, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it w ere bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray."),
    (2, 6): TraitTemplate("Keen Senses", "elf", (2, 6), "You have proficiency in the Perception skill."),
    (2, 7): TraitTemplate("Fey Ancestry", "elf", (2, 7), "You have advantage on saving throws against being charm ed, and m agic can’t put you to sleep."),
    (2, 8): TraitTemplate("Trance", "elf", (2, 8), "Elves don’t need to sleep. Instead, they meditate deeply, remaining sem iconscious, for 4 hours a day. (The Com m on w ord for such meditation is “trance.”) W hile meditating, you can dream after a fashion; such dream s are actually mental exercises that have becom e reflexive through years of practice. After resting in this way, you gain the sam e benefit that a human does from 8 hours of sleep."),
    (2, 9): TraitTemplate("Languages", "elf", (2, 9), "You can speak, read, and write Com m on and Elvish. Elvish is fluid, with subtle intonations and intricate grammar. Elven literature is rich and varied, and their songs and poem s are fam ous am ong other races. Many bards learn their language so they can add Elvish ballads to their repertoires."),
    (2, 10): TraitTemplate("Subrace", "elf", (2, 10), "Ancient divides am ong the elven people resulted in three main subraces: high elves, w ood elves, and dark elves, w ho are com m only called drow. Choose one of these subraces. In som e worlds, these subraces are divided still further (such as the sun elves and m oon elves of the Forgotten Realms), so if you wish, you can choose a narrower subrace."),
    # ### High Elf
    (2, 11): TraitTemplate("Ability Score Increase", "elf", (2, 11), "Your Intelligence score increases by 1."),
    (2, 12): TraitTemplate("Elf Weapon Training", "elf", (2, 12), "You have proficiency with the longsword, shortsword, shortbow, and longbow."),
    (2, 13): TraitTemplate("Cantrip", "elf", (2, 13), "You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it."),
    (2, 14): TraitTemplate("Extra Language", "elf", (2, 14), "You can speak, read, and write one extra language of your choice."),
    # ### Wood Elf
    (2, 15): TraitTemplate("Ability Score Increase", "elf", (2, 15), "Your W isdom score increases by 1."),
    (2, 16): TraitTemplate("Elf Weapon Training", "elf", (2, 16), "You have proficiency with the longsword, shortsword, shortbow, and longbow."),
    (2, 17): TraitTemplate("Fleet of Foot", "elf", (2, 17), "Your base walking speed increases to 35 feet."),
    (2, 18): TraitTemplate("Mask of the Wild", "elf", (2, 18), "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, and other natural phenomena."),
    # ### Dark Elf (Drow)
    (2, 19): TraitTemplate("Ability Score Increase", "elf", (2, 19), "Your Charisma score increases by 1."),
    (2, 20): TraitTemplate("Superior Darkvision", "elf", (2, 20), "Your darkvision has a radius of 120 feet."),
    (2, 21): TraitTemplate("Sunlight Sensitivity", "elf", (2, 21), "You have disadvantage on attack rolls and on W isdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight."),
    (2, 22): TraitTemplate("Drow Magic", "elf", (2, 22), "You know the dancing lights cantrip. W hen you reach 3rd level, you can cast the faerie fire spell once per day. W hen you reach 5th level, you can also cast the darkness spell once per day. Charisma is your spellcasting ability for these spells."),
    (2, 23): TraitTemplate("Drow Weapon Training", "elf", (2, 23), "You have proficiency with rapiers, shortswords, and hand crossbow s."),

    # # Halfling
    (3, 0): TraitTemplate("Ability Score Increase", "halfling", (3, 0), "Your Dexterity score increases by 2."),
    (3, 1): TraitTemplate("Age", "halfling", (3, 1), "A halfling reaches adulthood at the age of 20 and generally lives into the middle of his or her second century."),
    (3, 2): TraitTemplate("Alignment", "halfling", (3, 2), "M ost halflings are lawful good. As a rule, they are good-hearted and kind, hate to see others in pain, and have no tolerance for oppression. They are also very orderly and traditional, leaning heavily on the support of their com m unity and the com fort of their old ways."),
    (3, 3): TraitTemplate("Size", "halfling", (3, 3), "Halflings average about 3 feet tall and weigh about 40 pounds. Your size is ."),
    (3, 4): TraitTemplate("Speed", "halfling", (3, 4), "Your base walking speed is 25 feet."),
    (3, 5): TraitTemplate("Lucky", "halfling", (3, 5), "W hen you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll."),
    (3, 6): TraitTemplate("Brave", "halfling", (3, 6), "You have advantage on saving throws against being frightened."),
    (3, 7): TraitTemplate("Halfling Nimbleness", "halfling", (3, 7), "You can move through the space of any creature that is of a size larger than yours."),
    (3, 8): TraitTemplate("Languages", "halfling", (3, 8), "You can speak, read, and write Com m on and Halfling. The Halfling language isn’t secret, but halflings are loath to share it with others. They write very little, so they don’t have a rich body o f literature. Their oral tradition, however, is very strong. Alm ost all halflings speak Com m on to converse with the people in w hose lands they dwell or through which they are traveling."),
    (3, 9): TraitTemplate("Subrace", "halfling", (3, 9), "The two main kinds of halfling, lightfoot and stout, are m ore like closely related fam ilies than true subraces. C hoose one of these subraces."),
    # ### Lightfoot
    (3, 10): TraitTemplate("Ability Score Increase", "halfling", (3, 10), "Your Charisma score increases by 1."),
    (3, 11): TraitTemplate("Naturally Stealthy", "halfling", (3, 11), "You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you."),
    # ### Stoneheart
    (3, 12): TraitTemplate("Ability Score Increase", "halfling", (3, 12), "Your Constitution score increases by 1."),
    (3, 13): TraitTemplate("Stout Resilience", "halfling", (3, 13), "You have advantage on saving throws against poison, and you have resistance against poison damage."),

    # # Human
    (4, 0): TraitTemplate("Ability Score Increase", "human", (3, 0), "Your ability scores each increase by 1."),
    (4, 1): TraitTemplate("Age", "human", (3, 1), "Humans reach adulthood in their late teens and live less than a century."),
    (4, 2): TraitTemplate("Alignment", "human", (3, 2), "Humans tend toward no particular alignment. The best and the worst are found am ong them."),
    (4, 3): TraitTemplate("Size", "human", (3, 3), "Humans vary widely in height and build, from barely 5 feet to well over 6 feet tall. Regardless of your position in that range, your size is Medium."),
    (4, 4): TraitTemplate("Speed", "human", (3, 4), "Your base w alking speed is 30 feet."),
    (4, 5): TraitTemplate("Languages", "human", (3, 5), "You can speak, read, and write Com m on and one extra language of your choice. Humans typically learn the languages of other peoples they deal with, including obscure dialects. They are fond of sprinkling their speech with w ords borrow ed from other tongues: Orc curses, Elvish musical expressions, Dwarvish military phrases, and so on."),

    # # Dragonborn
    (5, 0): TraitTemplate("Ability Score Increase", "dragonborn", (5, 0), "Your Strength score increases by 2, and your Charisma score increases by 1."),
    (5, 1): TraitTemplate("Age", "dragonborn", (5, 1), "Young dragonborn grow quickly. They walk hours after hatching, attain the size and development of a 10-year-old human child by the age of 3, and reach adulthood by 15. They live to be around 80."),
    (5, 2): TraitTemplate("Alignment", "dragonborn", (5, 2), "Dragonborn tend to extremes, making a conscious choice for one side or the other in the cosm ic war between good and evil (represented by Bahamut and Tiamat, respectively). Most dragonborn are good, but those w ho side with Tiamat can be terrible villains."),
    (5, 3): TraitTemplate("Size", "dragonborn", (5, 3), "Dragonborn are taller and heavier than humans, standing well over 6 feet tall and averaging almost 250 pounds. Your size is Medium."),
    (5, 4): TraitTemplate("Speed", "dragonborn", (5, 4), "Your base walking speed is 30 feet."),
    (5, 5): TraitTemplate("Languages", "dragonborn", (5, 5), "You can speak, read, and write Com m on and D raconic. D raconic is thought to be one of the oldest languages and is often used in the study of magic. The language sounds harsh to m ost other creatures and includes num erous hard consonants and sibilants."),
    (5, 6): TraitTemplate("Draconic Ancestry", "dragonborn", (5, 6), "You have draconic ancestry. C hoose one type of dragon from the D raconic Ancestry table. Your breath weapon and damage resistance are determined by the dragon type, as show n in the table."),
    (5, 7): TraitTemplate("Breath Weapon", "dragonborn", (5, 7), "You can use your action to exhale destructive energy. Your draconic ancestry determines the size, shape, and damage type of the exhalation. \nWhen you use your breath weapon, each creature in the area of the exhalation must make a saving throw, the type of which is determined by your draconic ancestry. The DC for this saving throw equals 8 + your Constitution m odifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increases to 3d6 at 6th level, 4d6 at 11th level, and 5d6 at 16th level. \nAfter you use your breath weapon, you can’t use it again until you com plete a short or long rest."),
    (5, 8): TraitTemplate("Damage Resistance", "dragonborn", (5, 8), "You have resistance to the damage type associated with your draconic ancestry."),

    # # Gnome
    (6, 0): TraitTemplate("Ability Score Increase", "gnome", (6, 0), "Your Intelligence score increases by 2."),
    (6, 1): TraitTemplate("Age", "gnome", (6, 1), " G nom es mature at the sam e rate humans do, and m ost are expected to settle down into an adult life by around age 40. They can live 350 to almost 500 years."),
    (6, 2): TraitTemplate("Alignment", "gnome", (6, 2), " Gnom es are most often good. T hose who tend toward law are sages, engineers, researchers, scholars, investigators, or inventors. T hose w ho tend toward chaos are minstrels, tricksters, wanderers, or fanciful jew elers. G nom es are good-hearted, and even the tricksters am ong them are m ore playful than vicious."),
    (6, 3): TraitTemplate("Size", "gnome", (6, 3), "Gnom es are between 3 and 4 feet tall and average about 40 pounds. Your size is Small."),
    (6, 4): TraitTemplate("Speed", "gnome", (6, 4), "Your base walking speed is 25 feet."),
    (6, 5): TraitTemplate("Languages", "gnome", (6, 5), "You can speak, read, and write Com m on and Gnomish. The Gnom ish language, which uses the Dwarvish script, is renow ned for its technical treatises and its catalogs o f knowledge about the natural world."),
    (6, 6): TraitTemplate("Darkvision", "gnome", (6, 6), "Accustom ed to life underground, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it w ere bright light, and in darkness as if it were dim light. You can't discern color in darkness, only shades of gray."),
    (6, 7): TraitTemplate("Gnome Cunning", "gnome", (6, 7), "You have advantage on all Intelligence, W isdom , and Charisma saving throws against magic."),
    (6, 8): TraitTemplate("Subrace", "gnome", (6, 8), "Two subraces of gnom es are found am ong the worlds of D&D: forest gnom es and rock gnom es. C hoose one of these subraces."),
    # ### Forest Gnome
    (6, 9): TraitTemplate("Ability Score Increase", "gnome", (6, 9), "Your Dexterity score increases by 1."),
    (6, 10): TraitTemplate("Natural Illusionist", "gnome", (6, 10), "You know the minor illusion cantrip. Intelligence is your spellcasting ability for it."),
    (6, 11): TraitTemplate("Speak with Small Beasts", "gnome", (6, 11), "Through sounds and gestures, you can com m unicate simple ideas with Small or sm aller beasts. Forest gnom es love animals and often keep squirrels, badgers, rabbits, m oles, w oodpeckers, and other creatures as beloved pets."),
    # ### Rock Gnome
    (6, 12): TraitTemplate("Ability Score Increase", "gnome", (6, 12), "Your Constitution score increases by 1."),
    (6, 13): TraitTemplate("Artificer’s Lore", "gnome", (6, 13), "W henever you make an Intelligence (History) check related to m agic items, alchemical objects, or technological devices, you can add tw ice your proficiency bonus, instead of any proficiency bonus you normally apply."),
    (6, 14): TraitTemplate("Tinker", "gnome", (6, 14), "You have proficiency with artisan’s tools (tinker’s tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockw ork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep the device functioning), or when you use your action to dismantle it; at that time, you can reclaim the materials used to create it. You can have up to three such devices active at a time. \nW hen you create a device, choose one of the following options: \nClockwork Toy. This toy is a clockw ork animal, monster, or person, such as a frog, mouse, bird, dragon, or soldier. W hen placed on the ground, the toy m oves 5 feet across the ground on each of your turns in a random direction. It makes noises as appropriate to the creature it represents. \nFire Starter. The device produces a flame, which you can use to light a candle, torch, or campfire. Using the device requires your action. \nMusic Box. W hen opened, this music box plays a single song at a moderate volume. The box stops playing when it reaches the son g’s end or when it is closed."),

    # # Half-Elf
    (7, 0): TraitTemplate("Ability Score Increase", "half-elf", (7, 0), "Your Charisma score increases by 2, and two other ability scores of your choice increase by 1."),
    (7, 1): TraitTemplate("Age", "half-elf", (7, 1), "Half-elves mature at the sam e rate humans do and reach adulthood around the age o f 20. They live much longer than humans, however, often exceeding 180 years."),
    (7, 2): TraitTemplate("Alignment", "half-elf", (7, 2), "Half-elves share the chaotic bent of their elven heritage. They value both personal freedom and creative expression, demonstrating neither love of leaders nor desire for followers. They chafe at rules, resent others’ demands, and som etim es prove unreliable, or at least unpredictable."),
    (7, 3): TraitTemplate("Size", "half-elf", (7, 3), "Half-elves are about the same size as humans, ranging from 5 to 6 feet tall. Your size is Medium."),
    (7, 4): TraitTemplate("Speed", "half-elf", (7, 4), "Your base walking speed is 30 feet."),
    (7, 5): TraitTemplate("Languages", "half-elf", (7, 5), "You can speak, read, and write Com m on, Elvish, and one extra language of your choice."),
    (7, 6): TraitTemplate("Darkvision", "half-elf", (7, 6), "Thanks to your elf blood, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it w ere bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray."),
    (7, 7): TraitTemplate("Fey Ancestry", "half-elf", (7, 7), "You have advantage on saving throws against being charm ed, and m agic can’t put you to sleep."),
    (7, 8): TraitTemplate("Skill Versatility", "half-elf", (7, 8), "You gain proficiency in two skills of your choice."),

    # # Half-Orc
    (8, 0): TraitTemplate("Ability Score Increase", "half-orc", (7, 0), "Your Strength score increases by 2, and your Constitution score increases by 1.."),
    (8, 1): TraitTemplate("Age", "half-orc", (7, 1), "Half-orcs mature a little faster than humans, reaching adulthood around age 14. They age noticeably faster and rarely live longer than 75 years."),
    (8, 2): TraitTemplate("Alignment", "half-orc", (7, 2), "H alf-orcs inherit a tendency toward chaos from their orc parents and are not strongly inclined toward good. Half-orcs raised am ong ores and willing to live out their lives am ong them are usually evil."),
    (8, 3): TraitTemplate("Size", "half-orc", (7, 3), "H alf-orcs are som ewhat larger and bulkier than humans, and they range from 5 to well over 6 feet tall. Your size is Medium."),
    (8, 4): TraitTemplate("Speed", "half-orc", (7, 4), "Your base w alking speed is 30 feet."),
    (8, 5): TraitTemplate("Languages", "half-orc", (7, 5), "You can speak, read, and write Com m on and Orc . Orc is a harsh, grating language with hard consonants. It has no script of its own but is written in the Dwarvish script."),
    (8, 6): TraitTemplate("Darkvision", "half-orc", (7, 6), "Thanks to your orc blood, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it w ere bright light, and in darkness as if it w ere dim light. You can't discern color in darkness, only shades o f gray."),
    (8, 7): TraitTemplate("Menacing", "half-orc", (7, 7), "You gain proficiency in the Intimidation skill."),
    (8, 8): TraitTemplate("Relentless Endurance", "half-orc", (7, 8), "W hen you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can’t use this feature again until you finish a long rest."),
    (8, 9): TraitTemplate("Savage Attacks", "half-orc", (7, 9), "W hen you score a critical hit with a melee weapon attack, you can roll one of the w eapon’s damage dice one additional time and add it to the extra damage of the critical hit."),

    # # Tiefling
    (9, 0): TraitTemplate("Ability Score Increase", "tiefling", (9, 0), "Your Intelligence score increases by 1, and your Charisma score increases by 2."),
    (9, 1): TraitTemplate("Age", "tiefling", (9, 1), "Tieflings mature at the sam e rate as humans but live a few years longer."),
    (9, 2): TraitTemplate("Alignment", "tiefling", (9, 2), "Tieflings might not have an innate tendency toward evil, but many of them end up there. Evil or not, an independent nature inclines many tieflings toward a chaotic alignment."),
    (9, 3): TraitTemplate("Size", "tiefling", (9, 3), "Tieflings are about the sam e size and build as humans. Your size is Medium."),
    (9, 4): TraitTemplate("Speed", "tiefling", (9, 4), "Your base walking speed is 30 feet."),
    (9, 5): TraitTemplate("Languages", "tiefling", (9, 5), "You can speak, read, and write Com m on and Infernal."),
    (9, 6): TraitTemplate("Darkvision", "tiefling", (9, 6), "Thanks to your infernal heritage, you have superior vision in dark and dim conditions. You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it w ere dim light. You can’t discern color in darkness, only shades o f gray."),
    (9, 7): TraitTemplate("Hellish Resistance", "tiefling", (9, 7), "You have resistance to fire damage."),
    (9, 8): TraitTemplate("Infernal Legacy", "tiefling", (9, 8), "You know the thaumaturgy cantrip. Once you reach 3rd level, you can cast the hellish rebuke spell once per day as a 2nd-level spell. O nce you reach 5th level, you can also cast the darkness spell once per day. Charisma is your spellcasting ability for these spells."),
}
