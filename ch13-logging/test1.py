# logging 日誌記錄

"""
級別從低到高 ->
debug(). info(). warning(). error(). critical().
"""

import logging

logging.basicConfig(level = 'INFO') # 設置級別 相關配置
logging.basicConfig(filename='test.log',filemode='w')
#執行會新開一個test.log  並且使用w每次重新寫入
logging.debug('this is debug')
logging.info('this is info')
logging.warning('this is warning')
logging.error('this is error')
logging.critical('this is critical')