
# 1.对象层:定义页面的元素
from selenium.webdriver.common.by import By


class LoginPage:
    # 点击登录
    login_link = (By.LINK_TEXT, "登录")
    # 用户名
    username = (By.ID, "username")
    # 密码
    password = (By.ID, "password")
    # 验证码
    verify_code = (By.ID, "verify_code")
    # 登录
    login_btn = (By.NAME, "sbtbutton")

    # 登录成功进入的首页
    home_page = (By.LINK_TEXT, "首页")

    # 登录成功信息
    login_success_msg = (By.CLASS_NAME, "mu-m-phone")

    # 登录错误信息
    password_error_msg = (By.CLASS_NAME, "layui-layer-content")

