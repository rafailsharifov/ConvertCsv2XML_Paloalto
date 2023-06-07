import xml.etree.ElementTree as ET


def create_zone(zones_name):

    tree = ET.parse("running-config.xml")
    root = tree.getroot()

    zones = root.find("./devices/entry/vsys/entry/zone")
    for zone_name in zones_name:
        entry = ET.SubElement(zones, "entry")
        entry.set("name", zone_name)

        network = ET.SubElement(entry, "network")
        layer3 = ET.SubElement(network, "layer3")
        

    new_file = ET.ElementTree(root)
    new_file.write("running-config.xml", encoding="utf-8", xml_declaration=True)






def create_sec_rule(object):

    object_names_list = {"to": "Destination Zone",
                         "from": "Source Zone", 
                         "source": "Source Address", 
                         "destination": "Destination Address", 
                         "source-user": "any", #because in excel is not provided
                         "category": "any",    #because in excel is not provided
                         "application": "Application", 
                         "service": "Service", 
                         "source-hip": "any",  #because in excel is not provided
                         "destination-hip": "any",  #because in excel is not provided
                         "action": "Action"}
    

    tree = ET.parse("running-config.xml")
    root = tree.getroot()

    rules = root.find("./devices/entry/vsys/entry/rulebase/security/rules")

    number= len(object["Name"])

    for n in range(number):
        name_var = object["Name"][n]

        entry = ET.SubElement(rules, "entry")
        entry.set("name", name_var)

        for config_name in object_names_list.keys():
            config_value = object_names_list[config_name]

            if config_value == "any":
                each_value_from_excel = "any"

            else:
                each_value_from_excel = str(object[config_value][n])
                if config_name == "action":
                    each_value_from_excel = each_value_from_excel.lower()

                    config_itself = ET.SubElement(entry, config_name)
                    config_itself.text = each_value_from_excel
                    continue

                else:pass

            each_value_from_excel = each_value_from_excel.split(";")
            config_itself = ET.SubElement(entry, config_name)

            for text_value in each_value_from_excel:
                member = ET.SubElement(config_itself, "member")
                member.text = text_value


    new_file = ET.ElementTree(root)
    new_file.write("running-config.xml", encoding="utf-8", xml_declaration=True)

