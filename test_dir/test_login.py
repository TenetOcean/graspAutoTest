import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.pay_web_page import PayWebPage
from page.dog_online_page import DogOnlinePage
import pytest
import time


class TestLoginSucess:
    """登录"""

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
    def test_buy(self,browser,base_url):
        """生成狗号验证码"""
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

    def test_buy_success(self,browser,base_url):
        ''''''
        self.hh_login(browser,base_url)
        page = DogOnlinePage(browser)
        page.get("http://192.168.9.50:8200/Home/Index")
        page.product_buy_menu.click()
        page.soft_dog_buy_submenu.click()
        page.hh_top_soft_nav.click()
        page.hh_top_soft_icon.click()
        page.window_scroll(0,"document.body.scrollHeight")
        page.hh_top_new_buy_radio.click() # 购买单选按钮‘新购’
        page.hh_top_buy_order_submit.click()
        



if __name__ == '__main__':
    pytest.main(["-v", "./test_dir/test_login.py"])
