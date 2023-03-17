import argparse
import logging
import os
from time import sleep

# Описание параметров
parser = argparse.ArgumentParser()
parser.add_argument('-rn', '--row_number', required=True, type=int, help='Требуемое количество записей')
parser.add_argument('-lat', '--latency', required=True, type=int, help='Требуемая задержка')
args = parser.parse_args()

# Настрока базового конфига логгирования
logging.basicConfig(filename='log_file.log', format='%(asctime)s  %(levelname)s  %(message)s',
                    datefmt='%b %d %H:%M:%S', level='INFO')

v_rn = 0
for i in os.environ:
    logging.info(f'{i} : {os.environ[i]}')
    v_rn += 1
    if v_rn < args.row_number:
        sleep(args.latency)
    else:
        break

# print("Logging ended")
