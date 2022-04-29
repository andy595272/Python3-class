import logging

format = '%(asctime)s-%(levelname)s %(name)s % (meseage)s'
logging.basicConfig(level='INFO', format=format)
# 可以在終端使用 根據format格式打印出來不同東西

def main():
    logging.debug('this is debug')
    logging.info('this is info')
    logging.warning('this is warning')
    logging.error('this is error')
    logging.critical('this is critical')

if __name__ == "__main__":
    main()