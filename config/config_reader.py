import configparser


class ConfigReader:

    config = configparser.ConfigParser()

    config.read("config/config.ini")

    @classmethod
    def get_base_url(cls):
        return cls.config["DEFAULT"]["base_url"]

    @classmethod
    def get_password(cls):
        return cls.config["DEFAULT"]["password"]

    @classmethod
    def get_browser(cls):
        return cls.config["DEFAULT"]["browser"]