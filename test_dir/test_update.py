from os import cpu_count
import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.pay_web_page import PayWebPage
from page.dog_online_page import DogOnlinePage
from page.customer_page import CustomerPage
from page.register_page import RegisterPage
import pytest
import time
import random,string

class TestUpdate:
    """测试升级"""

    def hh_login(self,driver,url): # '''辉煌登录方法'''            
        dPage = PayWebPage(driver)
        dPage.get(url)
        loginHandle = dPage.current_window_handle
        dPage.first_agent_login_button.click()
        dPage.login_user_name_input.clear()
        dPage.login_user_name_input.send_keys("02899999")
        dPage.login_password_input.send_keys("123123")
        dPage.login_verification_code_input.send_keys("dfdsg2165498jdofdfd")
        dPage.login_button.enter()
        dPage.hh_buy_button.click()
        allHandle = dPage.window_handles
        for handle in allHandle:
            if handle != loginHandle:
                dPage.switch_to_window(handle)

    def customer_login(self,driver): # '''客户信息管理系统登录方法'''
        dPage = CustomerPage(driver)
        dPage.get("http://192.168.9.50:8300")
        dPage.login_user_name_input.send_keys("admin")
        dPage.login_password_input.send_keys("123123")
        dPage.login_verification_code_input.send_keys("sdf3554kjs5d56afs55od54fj56o6565isg6577js")
        dPage.login_button.click()

    def test_update_user_count(self,browser,base_url):
        """未注册辉煌ⅡTop升级用户数"""
        global hh_dogNo
        global hh_code
        self.hh_login(browser,base_url)
        dPage = DogOnlinePage(browser)
        dPage.product_buy_menu.click()
        dPage.soft_dog_buy_submenu.click()
        dPage.hh_top_soft_nav.click()
        dPage.hh_top_soft_icon.click()
        dPage.execute_script("window.scrollTo(0,document.body.scrollHeight);") # js滚动条拉到最底端
        dPage.hh_top_new_buy_radio.click() # 购买单选按钮‘新购’
        dPage.hh_top_buy_order_submit.click()
        dPage.confirm_order_button.click()
        dPage.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        dPage.pay_password_input.send_keys("123123")
        dPage.confirm_pay_button.click()
        dPage.accept_alert()
        dPage.buy_sucess_dog_number_copy_button.click()
        text = dPage.get_alert_text
        dPage.dismiss_alert()
        hh_dogNo = text.split("：")[2].split(" ")[0]
        hh_code = text.split("：")[3]
        dPage.get("http://192.168.9.50:8200/")
        dPage.product_update_menu.click()
        dPage.product_update_submenu.click()
        dPage.update_dog_number_input.send_keys(hh_dogNo)
        dPage.update_dog_verification_code_input.send_keys(hh_code)
        dPage.is_cross_product_update_checkbox.click()
        dPage.update_product_button.click()
        time.sleep(3)
        dPage.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        dPage.update_to_hh_top_add_users_button.click()
        dPage.update_order_submit.click()
        dPage.execute_script("document.getElementById('UpdateConfirmForm').submit();")
        dPage.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        dPage.pay_password_input.send_keys("123123")
        dPage.confirm_pay_button.click()
        dPage.accept_alert()
        time.sleep(8)
        dPage.dismiss_alert()

    def test_update_user_conunt_for_yhh(self,browser):
        """未注册云辉煌ERP H3买断升级用户数"""
        pass
        # dPage = DogOnlinePage(browser)
        # dPage.get

    def test_update_user_count_for_registered_hh(self,browser):
        """已注册辉煌ⅡTop升级用户数"""
        rPage = RegisterPage(browser)
        dPage = DogOnlinePage(browser)
        rPage.get("http://192.168.9.50:8500")
        rPage.register_dog_number_input.send_keys(hh_dogNo)
        rPage.register_dog_verification_code_input.send_keys(hh_code)
        rPage.submit_verification_button.click()
        rPage.agent_name_input.send_keys("六六")
        rPage.contact_input.send_keys("小华")
        rPage.customer_email_input.send_keys("120624697@qq.com")
        rPage.company_name_input.send_keys("任我逍遥任我行")
        rPage.address_input.send_keys("软件园D")
        rPage.industry_select.click()
        rPage.industry_list_select_it.click()
        rPage.province_select.click()
        rPage.province_list_select_sichuan.click()
        rPage.mobile_number_input.send_keys("18280331234")
        rPage.fixed_telephone_input.send_keys("028803379")
        rPage.company_contact_radio.click()
        rPage.channel_radio.click()
        rPage.is_website_radio.click()
        rPage.is_network_radio.click()
        rPage.is_exist_branch_radio.click()
        rPage.computer_count_radio.click()
        rPage.submit_register_button.click()
        rPage.accept_alert()
        dPage.get("http://192.168.9.50:8200/Home/Index")
        dPage.dog_manage_menu.click()
        dPage.dog_query_submenu.click()
        dPage.search_input.send_keys(hh_dogNo)
        dPage.search_button.click()
        dPage.submit_headquarters_review_button.click()
        dPage.agent_review_pass_button.click()
        dPage.accept_alert()
        time.sleep(1)
        dPage.accept_alert()
        self.customer_login(browser)
        cPage = CustomerPage(browser)
        cPage.register_review_menu.click()
        cPage.wait_register_review_submenu.click()
        cPage.search_input.send_keys(hh_dogNo)
        time.sleep(1)
        cPage.wait_review_content_first_tr.click()
        cPage.execute_script("window.scrollTo(0,450);")
        cPage.review_pass_button.click()
        cPage.review_popup_submit_button.click()
        time.sleep(3)
        dPage.get("http://192.168.9.50:8200/")
        dPage.product_update_menu.click()
        dPage.product_update_submenu.click()
        dPage.update_dog_number_input.send_keys(hh_dogNo)
        dPage.update_dog_verification_code_input.send_keys(hh_code)
        dPage.is_cross_product_update_checkbox.click()
        dPage.update_product_button.click()
        time.sleep(3)
        dPage.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        dPage.update_to_hh_top_add_users_button.click()
        dPage.update_order_submit.click()
        dPage.execute_script("document.getElementById('UpdateConfirmForm').submit();")
        dPage.update_company_name_input.send_keys("任我逍遥任我行")
        dPage.update_industry_select.click()
        dPage.update_industry_list_select_it.click()
        dPage.update_province_select.click()
        dPage.update_province_list_select_sichuan.click()
        dPage.update_address_input.send_keys("软件园")
        dPage.update_contact_input.send_keys("小华")
        dPage.update_mobile_number_input.send_keys("18280556617")
        dPage.update_fixed_telephone_input.send_keys("028803375")
        dPage.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        dPage.update_customer_email_input.send_keys("120624697@qq.com")
        dPage.update_company_contact_radio.click()
        dPage.update_channel_radio.click()
        dPage.update_is_website_radio.click()
        dPage.update_is_network_radio.click()
        dPage.update_is_exist_branch_radio.click()
        dPage.update_computer_count_radio.click()
        dPage.update_review_submit_button.click()
        dPage.accept_alert()
        time.sleep(1)
        dPage.dismiss_alert()
        cPage.get("http://192.168.9.50:8300/UpdateAudit/UpdateAudit")
        cPage.update_review_menu.click()
        cPage.wait_update_review_submenu.click()
        cPage.search_input.send_keys(hh_dogNo)
        time.sleep(1)
        cPage.wait_review_content_first_tr.click()
        cPage.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        cPage.review_pass_button.click()
        cPage.review_popup_submit_button.click()
        dPage.get("http://192.168.9.50:8200/")
        dPage.product_update_menu.click()
        dPage.wait_update_submenu.click()
        dPage.wait_update_pay_button.click()
        dPage.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        dPage.pay_password_input.send_keys("123123")
        dPage.confirm_pay_button.click()
        dPage.accept_alert()


if __name__ == "__main__":
    pytest.main(["-v", "./test_dir/test_update.py"])
