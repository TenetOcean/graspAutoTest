import sys
import pytest
import time
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.pay_web_page import PayWebPage


class TestLogin:
    """登录"""

    def test_login_sucess(self, browser, base_url):
        '''登录测试'''
        page = PayWebPage(browser)
        page.get(base_url)
        page.first_agent_login_button.click()
        page.login_user_name_input.send_keys("02899999")
        page.login_password_input.send_keys("123123")
        page.login_user_code_input.send_keys("dfdsg2165498jdofdfd")
        page.login_button.enter()
        page.window_scroll(100,100)


if __name__ == '__main__':
    pytest.main(["-v", "./test_dir/test_login.py"])
