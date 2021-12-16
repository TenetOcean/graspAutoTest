import sys
from os.path import dirname,abspath
sys.path.insert(0,dirname(dirname(abspath(__file__))))
from page.pay_web_page import PayWebPage
from page.dog_online_page import DogOnlinePage
import pytest
import time
import random,string

class TestAccount:
    """测试账套"""

    def hh_login(self,driver,url): # '''辉煌登录方法'''            
        page = PayWebPage(driver)
        page.get(url)
        loginHandle = page.current_window_handle
        page.first_agent_login_button.click()
        page.login_user_name_input.clear()
        page.login_user_name_input.send_keys("02899999")
        page.login_password_input.send_keys("123123")
        page.login_verification_code_input.send_keys("dfdsg2165498jdofdfd")
        page.login_button.enter()
        page.hh_buy_button.click()
        allHandle = page.window_handles
        for handle in allHandle:
            if handle != loginHandle:
                page.switch_to_window(handle)

    def test_account_buy_for_yhhERP(self,browser,base_url):
        """云辉煌ERP H3账套购买"""
        global yhh_dogNo #云辉煌ERP狗号
        global yhh_code #云辉煌ERP验证码
        self.hh_login(browser,base_url)
        page = DogOnlinePage(browser)
        page.product_buy_menu.click()
        page.soft_dog_buy_submenu.click()
        page.yhh_erp_soft_nav.click()
        page.yhh_erp_h3_icon.click()
        page.execute_script("window.scrollTo(0,document.body.scrollHeight);") # js滚动条拉到最底端
        page.yhh_erp_h3_new_buy_radio.click()
        ran_str = ''.join(random.sample(string.ascii_letters,4))
        page.yhh_erp_customer_name_input.send_keys(ran_str)
        page.yhh_erp_customer_telephone_input.send_keys("18231045141")
        page.yhh_erp_h3_buy_order_submit.click()
        page.confirm_order_button.click()
        page.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        page.pay_password_input.send_keys("123123")
        page.confirm_pay_button.click()
        page.accept_alert()
        page.buy_sucess_dog_number_copy_button.click()
        text = page.get_alert_text
        page.dismiss_alert()
        yhh_dogNo = text.split("：")[2].split(" ")[0]
        yhh_code = text.split("：")[3]
        page.get("http://192.168.9.50:8200/")
        page.account_manage_menu.click()
        page.account_buy_submenu.click()
        page.dog_number_input.send_keys(yhh_dogNo)
        page.dog_verification_code_input.send_keys(yhh_code)
        page.success_button.click()
        time.sleep(1)
        page.window_scroll(0,"document.body.scrollHeight")
        page.update_order_submit.click()
        page.execute_script("document.getElementById('UpdateConfirmForm').submit();")
        page.window_scroll(0,"document.body.scrollHeight")
        page.pay_password_input.send_keys("123123")
        page.confirm_pay_button.click()
        page.accept_alert()
        page.sleep(5)
        page.dismiss_alert()
        # time.sleep(5)
    
    def test_account_buy_for_hhERP(self,browser,base_url):
        """辉煌ERP H3账套购买"""
        global hh_dogNo #辉煌ERP h3狗号
        global hh_code #辉煌ERP h3验证码
        # self.hh_login(browser,base_url)
        page = DogOnlinePage(browser)
        page.get("http://192.168.9.50:8200/")
        page.product_buy_menu.click()
        page.soft_dog_buy_submenu.click()
        page.hh_erp_soft_nav.click()
        page.hh_erp_h3_icon.click()
        page.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        page.hh_erp_h3_new_buy_radio.click()
        page.hh_erp_h3_buy_order_submit.click()
        page.confirm_order_button.click()
        page.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        page.pay_password_input.send_keys("123123")
        page.confirm_pay_button.click()
        page.accept_alert()
        page.buy_sucess_dog_number_copy_button.click()
        text = page.get_alert_text
        page.dismiss_alert()
        hh_dogNo = text.split("：")[2].split(" ")[0]
        hh_code = text.split("：")[3]
        page.get("http://192.168.9.50:8200/")
        page.account_manage_menu.click()
        page.account_buy_submenu.click()
        page.dog_number_input.send_keys(hh_dogNo)
        page.dog_verification_code_input.send_keys(hh_code)
        page.success_button.click()
        time.sleep(1)
        page.window_scroll(0,"document.body.scrollHeight")
        page.update_order_submit.click()
        page.execute_script("document.getElementById('UpdateConfirmForm').submit();")
        page.window_scroll(0,"document.body.scrollHeight")
        page.pay_password_input.send_keys("123123")
        page.confirm_pay_button.click()
        page.accept_alert()
        page.sleep(5)
        page.dismiss_alert()
        
    def test_account_update(self,browser):
        """账套狗升级用户数"""
        page = DogOnlinePage(browser)
        page.get("http://192.168.9.50:8200/")
        page.product_update_menu.click()
        page.product_update_submenu.click()
        page.dog_number_input.send_keys(yhh_dogNo)
        page.dog_verification_code_input.send_keys(yhh_code)
        page.is_cross_product_update_checkbox.click()
        page.update_product_button.click()
        time.sleep(3)
        page.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        page.update_to_yhh_erp_h3_add_users_button.click()
        page.update_order_submit.click()
        page.execute_script("document.getElementById('UpdateConfirmForm').submit();")
        page.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        page.pay_password_input.send_keys("123123")
        page.confirm_pay_button.click()
        page.accept_alert()
        time.sleep(8)
        # page.dismiss_alert()

if __name__ == "__main__":
    pytest.main(["-v", "./test_dir/test_account.py"])