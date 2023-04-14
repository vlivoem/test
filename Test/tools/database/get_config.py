import configparser


def get_config(section):
    configs = {}
    # 读取配置文件
    config = configparser.RawConfigParser()
    config.read("config.txt")
    # 获取配置文件中，指定section中的key
    options = config.options(section)
    # 将指定section中的key及value获取到，并存放到configs字典中
    for option in options:
        try:
            configs[option] = config.get(section, option)
        except:
            print("读取配置失败！")
            return False
    return configs