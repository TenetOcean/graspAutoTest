import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.pay_web_page import PayWebPage
from page.dog_online_page import DogOnlinePage
from page.customer_page import CustomerPage
from page.register_page import RegisterPage
import pytest
import time

class TestRegister:
    """注册"""

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

    def customer_login(self,driver): # '''客户信息管理系统登录方法'''
        page = CustomerPage(driver)
        page.get("http://192.168.9.50:8300")
        page.login_user_name_input.send_keys("admin")
        page.login_password_input.send_keys("123123")
        page.login_verification_code_input.send_keys("sdf3554kjs5d56afs55od54fj56o6565isg6577js")
        page.login_button.click()

    def test_hh_top_register(self,browser,base_url):
        """辉煌Ⅱtop产品注册"""
        # self.hh_login(browser,base_url)
        page = DogOnlinePage(browser)
        page.get("http://192.168.9.50:8200/Home/Index")
        page.product_buy_menu.click()
        page.soft_dog_buy_submenu.click()
        page.hh_top_soft_nav.click()
        page.hh_top_soft_icon.click()
        page.execute_script("window.scrollTo(0,document.body.scrollHeight);") # js滚动条拉到最底端
        page.hh_top_new_buy_radio.click() # 购买单选按钮‘新购’
        page.hh_top_buy_order_submit.click()
        page.confirm_order_button.click()
        page.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        page.pay_password_input.send_keys("123123")
        page.confirm_pay_button.click()
        page.accept_alert()
        page.buy_sucess_dog_number_copy_button.click()
        text = page.get_alert_text
        page.dismiss_alert()
        dogNo = text.split("：")[2].split(" ")[0]
        code = text.split("：")[3]
        rpage = RegisterPage(browser)
        rpage.get("http://192.168.9.50:8500")
        rpage.register_dog_number_input.send_keys(dogNo)
        rpage.register_dog_verification_code_input.send_keys(code)
        rpage.submit_verification_button.click()
        rpage.agent_name_input.send_keys("六六")
        rpage.contact_input.send_keys("小华")
        rpage.customer_email_input.send_keys("120624697@qq.com")
        rpage.company_name_input.send_keys("任我逍遥任我行")
        rpage.address_input.send_keys("软件园D")
        rpage.industry_select.click()
        rpage.industry_list_select_it.click()
        rpage.province_select.click()
        rpage.province_list_select_sichuan.click()
        rpage.mobile_number_input.send_keys("18280331234")
        rpage.fixed_telephone_input.send_keys("028803379")
        rpage.company_contact_radio.click()
        rpage.channel_radio.click()
        rpage.is_website_radio.click()
        rpage.is_network_radio.click()
        rpage.is_exist_branch_radio.click()
        rpage.computer_count_radio.click()
        rpage.submit_register_button.click()
        rpage.accept_alert()
        page.get("http://192.168.9.50:8200/Home/Index")
        page.dog_manage_menu.click()
        page.dog_query_submenu.click()
        page.search_input.send_keys(dogNo)
        page.search_button.click()
        page.submit_headquarters_review_button.click()
        page.agent_review_pass_button.click()
        page.accept_alert()
        time.sleep(1)
        page.accept_alert()
        self.customer_login(browser)
        cpage = CustomerPage(browser)
        cpage.register_review_menu.click()
        cpage.wait_register_review_submenu.click()
        cpage.search_input.send_keys(dogNo)
        time.sleep(1)
        cpage.wait_review_content_first_tr.click()
        cpage.execute_script("window.scrollTo(0,450);")
        cpage.review_pass_button.click()
        cpage.review_popup_submit_button.click()
        time.sleep(5)

if __name__ == '__main__':
    pytest.main(["-v", "./test_dir/test_register.py"])