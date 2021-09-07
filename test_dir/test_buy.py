import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.pay_web_page import PayWebPage
from page.dog_online_page import DogOnlinePage
import pytest
import time
import random,string


class TestBuy:
    """测试购买"""

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

    # @pytest.mark.xfail(raises=AssertionError) # 标记函数进行异常断言
    def test_buy_hh_top(self,browser,base_url):
        """辉煌ⅡTop购买"""
        self.hh_login(browser,base_url)
        page = DogOnlinePage(browser)
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
        assert len(dogNo) == 12
        time.sleep(1)

    def test_buy_yhh_erp(self,browser):
        """云辉煌ERP H3买断购买"""
        page = DogOnlinePage(browser)
        page.get("http://192.168.9.50:8200/")
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
        dogNo = text.split("：")[2].split(" ")[0]
        code = text.split("：")[3]
        assert len(dogNo) == 12
        time.sleep(1)

    def test_hard_dog_buy(self,browser):
        """硬狗辉煌ⅡTop单机版购买"""
        page = DogOnlinePage(browser)
        page.get("http://192.168.9.50:8200/")
        page.product_buy_menu.click()
        page.hard_dog_buy_submenu.click()
        page.hh_top_add_to_cart_button.click()
        page.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        page.order_type_select.select_by_value("1")
        page.submit_order_button.click()
        page.hard_dog_confirm_order_button.click()
        page.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        page.pay_password_input.send_keys("123123")
        page.confirm_pay_button.click()
        page.accept_alert()
        page.get("http://192.168.9.50:8200/")

    def test_product_material_buy(self,browser):
        """资料辉煌Ⅱ彩单购买"""
        page = DogOnlinePage(browser)
        page.product_buy_menu.click()
        page.pruduct_material_buy_submenu.click()
        page.hh_color_list_add_to_cart_button.click()
        page.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        page.submit_order_button.click()
        page.hard_dog_confirm_order_button.click()
        page.pay_password_input.send_keys("123123")
        page.confirm_pay_button.click()
        page.accept_alert()
        page.get("http://192.168.9.50:8200/")

    def test_batch_buy(self,browser):
        """批量购买"""
        pass

if __name__ == '__main__':
    pytest.main(["-v", "./test_dir/test_buy.py"])