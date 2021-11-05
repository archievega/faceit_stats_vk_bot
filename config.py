import configparser

config = configparser.ConfigParser()
config.read('config.ini')

DATA = config['DATA']
FACEIT_TOKEN = DATA['FACEIT_TOKEN']
VK_TOKEN = DATA['VK_TOKEN']
VK_GROUP_ID = DATA['VK_GROUP_ID']
