import configparser
import os


class ReadConfig:
    @staticmethod
    def read_config(section, option):
        cf = configparser.ConfigParser()
        cf.read(ReadConfig.get_config_path(), encoding="utf-8")
        return cf[section][option]

    @staticmethod
    def get_config_path():
        base_path = os.getcwd().replace('\\', '/')
        config_path = '%sPython_work/common/config.conf' % base_path.split('Python_work')[0]
        return config_path


if __name__ == '__main__':
    ipc_port = ReadConfig.read_config('DATABASE', 'host')
    print(type(ipc_port))

