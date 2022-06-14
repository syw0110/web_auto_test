# 商品页
from selenium.webdriver.common.by import By


class GoodsPage:
    # 商品链接
    goods_link = (By.CLASS_NAME, "floor-goods-item")  # 返回一个列表

    # 加入购物车
    add_cart = (By.ID, "join_cart")

    # 关闭对话框
    close_promt = (By.CLASS_NAME, "layui-layer-ico")

    # 我的购物车
    my_cart = (By.CSS_SELECTOR, "i.share-shopcar-index")

    # 商品名称
    goods_name = (By.CLASS_NAME, "detail-ggsl")

    # 商品价格
    goods_price = (By.ID, "goods_price")

    # 商品数量
    goods_num = (By.CLASS_NAME, "buyNum")


