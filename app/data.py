import configparser

config = configparser.ConfigParser()
config.read('settings.ini', encoding='utf8')

HOST = config['db']['HOST']
DATABASE = config['db']['DATABASE']
PORT = config['db']['PORT']
USER = config['db']['USER']
ADMIN = config['db']['ADMIN']

COMPANY_NAME = config['document']['Наименование организации']
ADDRESS = config['document']['Адрес']
PHONE = config['document']['Номер телефона']

MARGIN = int(config['document']['Поля'])
SPACE_AFTER = int(config['document']['Между абзацами'])

H_FONT_SIZE = int(config['document']['шрифт шапки'])
H_LENDING = int(config['document']['высота строки шапки'])

P_FONT_SIZE = int(config['document']['шрифт параграфа'])
P_LENDING = int(config['document']['высота строки параграфа'])

MD_FONT_SIZE = int(config['document']['шрифт документа заявки'])
MD_LENDING = int(config['document']['высота строки документа заявки'])
