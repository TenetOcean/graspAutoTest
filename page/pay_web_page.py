from poium import Page, Element


class PayWebPage(Page):
    """任我行订货平台Page元素"""
    first_agent_login_button = Element(
        xpath="/html/body/div/div[2]/div/div/div/div[1]/div", describe="一级代理登录")
    second_agent_login_button = Element(
        xpath="/html/body/div/div[2]/div/div/div/div[3]/div", describe="二级代理登")
    login_user_name_input = Element(css="#UserName", describe="登录用户名输入框")
    login_password_input = Element(css="#PassWord", describe="登录密码输入框")
    login_verification_code_input = Element(css="#UserCode", describe="登录验证码输入框")
    login_button = Element(css="#LoginForm > button", describe="登录按钮")
    hh_buy_button = Element(
        xpath="//*[@id='page-wrapper']/div[3]/div[2]/div[5]/div/div/div[2]/div/a[1]", describe="通用系列产品购买按钮")
    yhh_buy_button = Element(
        xpath="//*[@id='page-wrapper']/div[3]/div[2]/div[13]/div/div/div[2]/div/a[1]", describe="云辉煌系列产品购买按钮")
    cm_buy_button = Element(
        xpath="//*[@id='page-wrapper']/div[3]/div[2]/div[2]/div/div/div[2]/div/a[1]", describe="财贸系列产品购买按钮")
