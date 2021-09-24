import yaml

CONF_FILEPATH = "conf.yml"

def read_conf(path):
    f = open(path, "r")
    conf_data = yaml.full_load(f)
    f.close()
    return conf_data

CONFIG = read_conf(CONF_FILEPATH)