import cc_dat_utils
import cc_classes
import  json

def make_level_pack_from_json( json_data ):
    #Initialize a new GameLibrary
    level_pack = cc_classes.CCLevelPack()
    levels = json_data["levels"]
    for level in levels:
        new_level = cc_classes.CCLevel()
        new_level.level_number = level["levelNumber"]
        new_level.time = level["time"]
        new_level.num_chips = level["chipNumber"]
        new_level.upper_layer = level["upperLayer"]
        for field in level["optionalFields"]:
            if field["type"] == "Title":
                new_level.add_field(cc_classes.CCMapTitleField(field["title"]))
            elif field["type"] == "Password":
                new_level.add_field(cc_classes.CCEncodedPasswordField(field["password"]))
            elif field["type"] == "Hint":
                new_level.add_field(cc_classes.CCMapHintField(field["hint"]))
            elif field["type"] == "Monsters":
                monsters = [cc_classes.CCCoordinate(monster["x"], monster["y"]) for monster in field["monsters"]]
                new_level.add_field(cc_classes.CCMonsterMovementField(monsters))
        level_pack.add_level(new_level)
    return level_pack

input_json_file = "data/jianif_cc1.json"

with open(input_json_file, "r") as reader:
    cc_json_data = json.load(reader)

#print(make_level_pack_from_json(cc_json_data))
cc_dat_utils.write_cc_level_pack_to_dat(make_level_pack_from_json(cc_json_data), "data/jianif_cc1.dat")


#Part 3
#Load your custom JSON file
#Convert JSON data to CCLevelPack
#Save converted data to DAT file