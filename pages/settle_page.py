
# 结算页面
from selenium.webdriver.common.by import By


class SettlePage:

    # 去结算
    settle = (By.LINK_TEXT, "去结算")

    # 提交订单
    submit_order = (By.CSS_SELECTOR, "a[onclick='submit_order();']")

    # 选择支付方式
    pay_way = (By.CSS_SELECTOR,"input[value='pay_code=cod']")

    # 点击确认支付
    confirm_pay = (By.LINK_TEXT, '确认支付方式')