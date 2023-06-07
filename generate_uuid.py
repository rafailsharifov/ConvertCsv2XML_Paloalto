import uuid
import xml.etree.ElementTree as ET


def gen_uuid():
    # Generate a UUID
    generated_uuid = uuid.uuid4()

    # Print the UUID
    print(generated_uuid)
    return generated_uuid






def add_uuid_config():
    tree = ET.parse("running-config.xml")
    root = tree.getroot()

    rules = root.find("./devices/entry/vsys/entry/rulebase/security/rules")
    for entries in rules:
        entry = entries.attrib
        if "uuid" in entry:
            pass
        else:
            entries.set("uuid", str(gen_uuid()))
        print(entry)

        

    new_file = ET.ElementTree(root)
    new_file.write("running-config.xml", encoding="utf-8", xml_declaration=True)

    

add_uuid_config()
