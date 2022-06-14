from selenium.webdriver.common.by import By


class OrderPage:
    # 我的商城
    my_mall = (By.CSS_SELECTOR, "a.menu-item")

    # 我的订单
    my_order = (By.CLASS_NAME, "J_chgurl")

    # 获取编号
    order_no = (By.CSS_SELECTOR, 'em.num')  # 获取列表第二个

    # 商品名称
    shop_name = (By.CSS_SELECTOR, "div.shop_name")

    # 商品单价
    shop_price = (By.CSS_SELECTOR, "td.sx2")  # 获取列表第二个

    # 商品数量
    shop_num = (By.CSS_SELECTOR, "td.sx3")  # 获取列表第二个

    # 支付状态
    pay_status = (By.CSS_SELECTOR, "p.d_yzo")  # 获取列表第三个数
