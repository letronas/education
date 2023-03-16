import argparse
import logging
from time import sleep

# Описание параметров
parser = argparse.ArgumentParser()
parser.add_argument('-rn', '--row_number', required=True, type=int, help='Требуемое количество записей')
parser.add_argument('-lat', '--latency', required=True, type=int, help='Требуемая задержка')
args = parser.parse_args()

# Настрока базового конфига логгирования
logging.basicConfig(filename='log_file.log', format='%(asctime)s  %(levelname)s  %(message)s',
                        datefmt='%b %d %H:%M:%S', level='INFO')

for i in range(args.row_number):
    logging.info('Info message')
    sleep(args.latency)
    
# print("Logging ended")