from poium import Page, Element


class DogOnlinePage(Page):
    """软狗在线销售系统页面元素"""

    product_buy_menu = Element(css="#\\31 01", describe="产品购买菜单")
    product_update_menu = Element(css="#\\32 01",describe="产品升级菜单")
    dog_manage_menu = Element(css="#\\33 21",describe="加密狗管理菜单")
    soft_dog_buy_submenu = Element(css="#sidebar > ul > li.sub-menu.open > ul > li:nth-child(1)",
                                   describe="软狗产品购买子菜单")
    hard_dog_buy_submenu = Element(css="#sidebar > ul > li:nth-child(2) > ul > li:nth-child(2)",
                                   describe="硬狗产品购买子菜单")
    pruduct_material_buy_submenu = Element(css="#sidebar > ul > li.sub-menu.open > ul > li:nth-child(3)",
                                           describe="产品资料购买子菜单")
    product_update_submenu = Element(css="#sidebar > ul > li.sub-menu.open > ul > li:nth-child(1)",
                                     describe="产品升级子菜单")
    wait_update_submenu = Element(css="#sidebar > ul > li.sub-menu.open > ul > li:nth-child(2)",
                                  describe="升级中客户子菜单")
    dog_query_submenu = Element(css="#sidebar>ul>li:nth-child(5)>ul>li>a",describe="加密狗查询子菜单")
    hh_top_soft_nav = Element(css="#pills > ul > li:nth-child(4)",describe="管家婆辉煌ⅡTOP软件导航")
    yhh_erp_soft_nav = Element(css="#pills > ul > li:nth-child(5)",describe="管家婆云辉煌ERP软件导航")
    hh_top_soft_icon = Element(css="#pills-tab11101 >form > div.row > div:nth-child(1) > a",
                               describe="辉煌ⅡTOP软件选择图标")
    yhh_erp_h3_icon = Element(css="#pills-tab11504 > form > div.row > div:nth-child(2) > a",
                              describe="云辉煌ERP H3买断选择图标")
    hh_top_add_to_cart_button = Element(css="#BuyForm > div.row > div:nth-child(4) > div > button.btn.btn-danger",
                                        describe="辉煌ⅡTop单机版加入购物车按钮")
    hh_color_list_add_to_cart_button = Element(css="#BuyForm > div > div:nth-child(1) > div > button",
                                               describe="资料辉煌Ⅱ彩单加入购物车按钮")
    hh_top_new_buy_radio = Element(css="#pills-tab11101 > form > div.top-line > div:nth-child(3) > div > div >" +
                                   "label:nth-child(1) > input",describe="辉煌ⅡTOP单选按钮'新购'")
    yhh_erp_h3_new_buy_radio = Element(css="#pills-tab11504 > form > div.top-line > div:nth-child(3) > div > div >" +
                                       "label:nth-child(1) > input",describe="云辉煌ERP H3买断单选按钮'新购'")
    yhh_erp_customer_name_input = Element(css="#pills-tab11504 > form > div.top-line > div:nth-child(10) > div >" + 
                                             "input",describe="云辉煌ERP H3买断客户名称输入框")
    yhh_erp_customer_telephone_input = Element(css="#pills-tab11504 > form > div.top-line > div:nth-child(11) >" +
                                                  "div > input",describe="云辉煌ERP H3买断客户电话输入框")
    order_type_select = Element(css=".ordergoodstype",describe="订货类型下拉框")
    hh_top_buy_order_submit = Element(css="#pills-tab11101 > form > div.top-line > div:nth-child(14) > div >" +
                                      "button.btn.btn-success",describe="辉煌ⅡTOP提交订单")
    yhh_erp_h3_buy_order_submit = Element(css="#pills-tab11504 > form > div.top-line > div:nth-child(14) > div >" +
                                          "button.btn.btn-success",describe="云辉煌ERP H3买断提交订单")
    submit_order_button = Element(css=".btn-primary",describe="提交订单按钮")
    buy_sucess_dog_number_copy_button = Element(xpath="//*[@id='modalId']/div[1]/div/div[2]/div/div[3]/div/input[1]",
                                                timeout=20,describe="购买成功狗号验证码复制按钮")
    
    update_dog_number_input = Element(css="#DogNo",describe="升级狗号输入框")
    update_dog_verification_code_input = Element(css="#VerificaCode",describe="升级狗号验证码输入框")
    is_cross_product_update_checkbox = Element(css="#IsCrossProduct",describe="是否跨产品升级勾选框")
    update_product_button = Element(css=".btn-success",describe="升级产品按钮")
    update_to_yhh_erp_h3_icon = Element(css="#YHHERPH3MD_TY",describe="升级到云辉煌ERP H3买断图标")
    update_to_hh_top_add_users_button = Element(css="#pills-tab297 > div.row > div:nth-child(1) > div >" + 
                                                "button:nth-child(4)",describe="升级到辉煌ⅡTop增加用户数按钮")
    update_to_yhh_erp_h3_add_users_button = Element(css="#pills-tab365 > div.row > div:nth-child(1) > div >" + 
                                                    "button:nth-child(4)",describe="升级到云辉煌ERP H3买断增加用户数按钮")
    update_order_submit = Element(css="#UpdateBuy",describe="升级确认提交")
    update_company_name_input = Element(css="#CompanyName",describe="升级客户公司名称输入框")
    update_industry_select = Element(css="#IndustryID_chzn",describe="升级所属行业下拉")
    update_industry_list_select_it = Element(css="#IndustryID_chzn_o_4",describe="升级所属行业列表选择‘IT’")
    update_province_select = Element(css="#AreaID_chzn",describe="升级省份下拉")
    update_province_list_select_sichuan = Element(css="#AreaID_chzn_o_1",describe="升级省份下拉列表选择‘四川’")
    update_address_input = Element(css="#Address",describe="升级详细通讯地址输入框")
    update_contact_input = Element(css="#UserName",describe="升级联系人输入框")
    update_mobile_number_input = Element(css="#MobileTel",describe="升级手机号码输入框")
    update_fixed_telephone_input = Element(css="#Tel",describe="升级固定电话1输入框")
    update_customer_email_input = Element(css="#Email",describe="升级客户邮箱输入框")
    update_company_contact_radio = Element(xpath="//*[@id='SubmitInfoForm']/div[14]/div/div/label[5]/input",
                                           describe="升级公司联系人单选按钮‘其他’")
    update_channel_radio = Element(xpath="//*[@id='SubmitInfoForm']/div[15]/div/div/label[6]/input",
                                   describe="升级知晓渠道单选按钮‘其他’")
    update_is_website_radio = Element(xpath="//*[@id='SubmitInfoForm']/div[16]/div/div/label[2]/input",
                                      describe="升级有无网站单选按钮‘无’")
    update_is_network_radio = Element(xpath="//*[@id='SubmitInfoForm']/div[17]/div/div/label[2]/input",
                                      describe="升级是否联网单选按钮‘无’")
    update_is_exist_branch_radio = Element(xpath="//*[@id='SubmitInfoForm']/div[18]/div/div/label[2]/input",
                                           describe="升级是否有分支机构单选按钮‘否’")
    update_computer_count_radio = Element(xpath="//*[@id='SubmitInfoForm']/div[19]/div/div/label[5]/input",
                                          describe="升级电脑数量单选按钮‘50台以上’")
    update_review_submit_button = Element(css="#ConfirmInfo",describe="升级审核提交按钮")
    wait_update_pay_button = Element(css="#sample_1 > tbody > tr:nth-child(1) > td:nth-child(12) >" + 
                                     "button.btn.btn-success",describe="升级中客户付款按钮")

    search_input = Element(css=".form-control",describe="搜索输入框")
    search_button = Element(css=".col-md-5 > button",describe="搜索按钮")
    submit_headquarters_review_button = Element(css=".btn-success",describe="提交总部审核按钮")
    agent_review_pass_button = Element(css="#Through",describe="代理审核通过按钮")
    agent_review_dissmiss_button = Element(css="#NotThrough",describe="代理审核不通过按钮")

    # customer_name_input = Element(css="#CustomerName",describe="客户名称输入框")
    # customer_telephone_input = Element(css="#CustomerTel",describe="客户电话输入框")

    confirm_order_button = Element(css="#formsubmit",describe="确认订单按钮")
    hard_dog_confirm_order_button = Element(css="#formsubmits",describe="硬狗确认订单按钮")
    
    pay_password_input = Element(css="#PassWord",describe="支付密码输入框")
    confirm_pay_button = Element(css="#ConfirmPay",describe="确认支付按钮")
