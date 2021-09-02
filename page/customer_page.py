from poium import Page,Element

class CustomerPage(Page):
    """客户信息管理系统页面元素"""

    login_user_name_input = Element(css="#UserCode",describe="登录用户名输入框")
    login_password_input = Element(css="#PassWord",describe="登录密码输入框")
    login_verification_code_input = Element(css="#ValiCode",describe="登录验证码输入框")
    login_button = Element(css="#InsertRoleFrorm > fieldset > div.clearfix > button",describe="登录按钮")
    register_review_menu = Element(css="#\\34 01 > a",describe="注册审核菜单")
    wait_register_review_submenu = Element(css="#\\34 01001 > a",describe="注册待审核信息子菜单")
    update_review_menu = Element(css="#\\35 01 > a",describe="升级审核菜单")
    wait_update_review_submenu = Element(css="#\\35 01001 > a",describe="升级待审核信息子菜单")

    review_pass_button = Element(css="#Form > div.form-actions > div > button.btn.btn-success",
                                   describe="审核通过按钮")
    wait_review_content_first_tr = Element(css="#sample-table-2 > tbody > tr",describe="待审核信息第一行")
    review_popup_submit_button = Element(css="#layui-layer2 > div.layui-layer-btn > a.layui-layer-btn0",
                                           describe="审核弹出框提交按钮")
    search_input = Element(css="#sample-table-2_filter > label > input",describe="搜索框")