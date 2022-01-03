import configparser

config = configparser.RawConfigParser()
config.read(".//Configurations//config.ini")


class ReadConfig:
    application_URL = config.get('common info', 'login_url')
    user_email = config.get('common info', 'useremail')
    user_password = config.get('common info', 'password')


