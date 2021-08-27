from poium import Page, Element


class PayWebPage(Page):
    first_agent_login_button = Element(xpath="/html/body/div/div[2]/div/div/div/div[1]/div",describe="一级代理登录")
    second_agent_login_button = Element(xpath="/html/body/div/div[2]/div/div/div/div[3]/div",describe="二级代理登")
    login_user_name_input = Element(css="#UserName",describe="登录用户名输入框")
    login_password_input = Element(css="#PassWord",describe="登录密码输入框")
    login_user_code_input = Element(css="#UserCode",describe="登录验证码输入框")
    login_button = Element(css="#LoginForm > button",describe="登录按钮")
    # search_input = Element(css="kw", describe="搜索框")
    # search_button = Element(css="su", describe="搜索按钮")
    # settings = Element(css="#s-usersetting-top", describe="设置")
    # search_setting = Element(css="#s-user-setting-menu > div > a.setpref", describe="搜索设置")
    # save_setting = Element(link_text="保存设置", describe="保存设置")
