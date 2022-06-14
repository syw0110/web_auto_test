# 2.逻辑层：定义操作逻辑
import datetime
import time

from selenium.webdriver import ActionChains
from utils.object_utils import cache
from pages.goods_page import GoodsPage
from pages.login_page import LoginPage
from pages.oder_page import OrderPage
from pages.settle_page import SettlePage
from loguru import logger


class BuyFlowLogic:

    def login(self, driver, username, password, verify_code):
        driver.find_element(*LoginPage.login_link).click()
        driver.find_element(*LoginPage.username).send_keys(username)
        driver.find_element(*LoginPage.password).send_keys(password)
        driver.find_element(*LoginPage.verify_code).send_keys(verify_code)
        driver.find_element(*LoginPage.login_btn).click()
        time.sleep(3)

    def buy_goods(self, driver):
        # 点击首页
        driver.find_element(*LoginPage.home_page).click()
        time.sleep(5)

        # 点击商品
        driver.find_elements(*GoodsPage.goods_link)[0].click()
        time.sleep(15)

        # 获取商品名称，商品单价，商品数量
        shop_name = driver.find_element(*GoodsPage.goods_name).text
        logger.info(f"从商品页获得的商品名称：{shop_name}")
        cache.set("shop_name", shop_name[0:13])

        shop_price = driver.find_element(*GoodsPage.goods_price).text
        logger.info(f"从商品页获得的商品单价：{shop_price}")
        cache.set("shop_price", shop_price)

        # 加入购物车
        driver.find_element(*GoodsPage.add_cart).click()
        time.sleep(5)

        # 关闭对话框
        driver.find_element(*GoodsPage.close_promt).click()
        driver.implicitly_wait(10)

        # 点击我的购物车
        driver.find_element(*GoodsPage.my_cart).click()
        time.sleep(15)

        # 点击去结算
        driver.find_element(*SettlePage.settle).click()
        time.sleep(5)

        # 点击提交订单
        driver.find_element(*SettlePage.submit_order).click()
        time.sleep(3)

        # 点击支付方式
        driver.find_element(*SettlePage.pay_way).click()

        # 点击确认支付方式
        driver.find_element(*SettlePage.confirm_pay).click()
        # 鼠标悬停到我的商城
        ActionChains(driver).move_to_element(driver.find_element(*OrderPage.my_mall)).perform()
        driver.implicitly_wait(2)
        # 点击我的订单
        driver.find_element(*OrderPage.my_order).click()

    def get_order_msg(self, driver):
        # 跳转到新窗口
        driver.switch_to.window(driver.window_handles[-1])

        # 获取订单编号
        order_no = driver.find_elements(*OrderPage.order_no)[1].text
        logger.info(f"获取到订单的编号：{order_no}")

        # 获取商品名称
        shop_name = driver.find_elements(*OrderPage.shop_name)[0].text
        logger.info(f"获取到的商品名称：{shop_name}")

        # 获取商品的单价
        shop_price = driver.find_elements(*OrderPage.shop_price)[0].text
        logger.info(f"获取到的商品单价：{shop_price}")

        # 获取商品的数量
        shop_num = driver.find_elements(*OrderPage.shop_num)[0].text
        logger.info(f"获取到的商品数量：{shop_num}")

        # 获取商品的支付状态
        pay_status = driver.find_elements(*OrderPage.pay_status)[2].text
        logger.info(f"获取到的支付状态：{pay_status}")

        return order_no, shop_name, shop_price, shop_num, pay_status
