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
    (0, 0): TraitTemplate("test trait 1", "debug race", (0, 1), "test trait 1 des"),
    (0, 1): TraitTemplate("test trait 2", "debug race", (0, 1), "test trait 2 des")
}
