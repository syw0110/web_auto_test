import unittest
from time import sleep

import allure
from loguru import logger
from selenium import webdriver
from utils.object_utils import cache
from logic.test_logic import BuyFlowLogic
from setting import BASE_URL, LOGIN_INFO
import warnings
from utils.basic_utils import get_cz
driver = webdriver.Chrome()

@allure.feature("购买模块")
@allure.story("购买子模块：购买流程")
class TestFlow(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.bf = BuyFlowLogic()
        cls.username = LOGIN_INFO.get("username")
        cls.password = LOGIN_INFO.get("password")
        cls.verify_code = LOGIN_INFO.get("verify_code")

    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        self.driver = driver
        self.driver.get(BASE_URL)
        self.driver.maximize_window()

    def tearDown(self) -> None:
        pass
        # self.driver.quit()

    @allure.title("正常购买流程")
    @allure.description("用户选择商品进行购买，断言购买商品数据正确")
    def test_buy_flow(self):
        with allure.step("选择商品加入购物车流程"):
            allure.attach(f"1.输入正确的用户名:{self.username}和密码:{self.password},进行登录")
            allure.attach("2.选择商品，加入购物车，支付下单")
            allure.attach("2.选择商品，加入购物车，支付下单")
        self.bf.login(self.driver, self.username, self.password, self.verify_code)
        self.bf.buy_goods(self.driver)
        self.order_no, self.shop_name, self.shop_price, self.shop_num, self.pay_status = self.bf.get_order_msg(self.driver)

        # 断言订单编号
        self.assertGreaterEqual(0, get_cz(self.order_no))

        # 断言商品名称，商品单价，商品数量
        goods_name = cache.get("shop_name")
        logger.info(f"从缓存中获取到的商品名称：{goods_name}")
        goods_price = cache.get("shop_price")
        logger.info(f"从缓存中获取到的商品单价：{goods_price}")

        self.assertEqual(goods_name, self.shop_name[0:13])
        self.assertEqual(goods_price, self.shop_price)
        self.assertEqual("x1", self.shop_num)
        # 断言发货状态
        self.assertEqual("待发货", self.pay_status)


if __name__ == '__main__':
    unittest.main()
