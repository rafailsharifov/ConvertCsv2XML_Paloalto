import read_excel
import creat_configs




filename= "Pa_rules.xlsx"

zones = read_excel.read_zones(filename)
creat_configs.create_zone(zones)

sec_rule_data = read_excel.read_sec_rules(filename)
creat_configs.create_sec_rule(sec_rule_data)

