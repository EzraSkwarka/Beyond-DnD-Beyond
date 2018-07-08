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

    def bundle_race_trait_info(self):
        array = []
        for val in self.list:
            array.append(val)
        return array

# def test1():
#     print("test1 worked")
#     return "test 1"
#
#
def test2():
    print("test2 worked")
    trait = TraitTemplate("test trait 1", "debug race", (0, 1), "test trait 1 des")




traitDictionary = {
    # (0, 0): ("test trait 1", "debug race", (0, 1), "test trait 1 des"),
    # (0, 1): ("test trait 2", "debug race", (0, 1), "test trait 2 des")
    (0, 0): TraitTemplate("test trait 1", "debug race", (0, 1), "test trait 1 des"),
    (0, 1): TraitTemplate("test trait 2", "debug race", (0, 1), "test trait 2 des")
}
