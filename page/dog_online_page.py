from poium import Page, Element


class DogOnlinePage(Page):
    """软狗在线销售系统页面元素"""

    product_buy_menu = Element(css="#\\31 01", describe="产品购买菜单")
    soft_dog_buy_submenu = Element(css="#sidebar > ul > li.sub-menu.open > ul > li:nth-child(1)",
                                   describe="软狗产品购买子菜单")
    hh_top_soft_nav = Element(css="#pills > ul > li:nth-child(4)",describe="管家婆辉煌ⅡTOP软件导航")
    hh_top_soft_icon = Element(xpath="/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[6]/" + 
                               "form/div[1]/div[1]/a",describe="辉煌ⅡTOP软件选择图标")
    hh_top_new_buy_radio = Element(xpath="/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[6]/" + 
                                   "form/div[2]/div[3]/div/div/label[1]/input",describe="辉煌ⅡTOP单选按钮'新购'")
    hh_top_buy_order_submit = Element(xpath="/html/body/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/" +
                                      "div[6]/form/div[2]/div[14]/div/button[1]",describe="辉煌ⅡTOP提交订单")
    buy_sucess_dog_number_copy_button = Element(xpath="//*[@id=\"modalId\"]/div[1]/div/div[2]/div/div[3]/div/input[1]",
                                                describe="购买成功狗号验证码复制按钮")
    confirm_order_button = Element(css="#formsubmit",describe="确认订单按钮")
    pay_password_input = Element(css="#PassWord",describe="支付密码输入框")
    confirm_pay_button = Element(css="#ConfirmPay",describe="确认支付按钮")
