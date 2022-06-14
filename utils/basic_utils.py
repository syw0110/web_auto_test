import datetime

from loguru import logger


def get_cz(order_no, cz=20):
    order_str = str(order_no)[10:14]
    # 获取当前时间
    now = datetime.datetime.now()
    logger.info(f"获取的当前时间：{now}")
    time_str = now.strftime("%Y%m%d%H%M%S")[10:14]

    # 两者相减,取绝对值
    vls = abs(int(order_str) - int(time_str)) - cz
    return vls

