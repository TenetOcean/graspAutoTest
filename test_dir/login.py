import sys
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.pay_web_page import PayWebPage

def hh_login(driver,url):
    '''辉煌登录'''
    page = PayWebPage(driver)
    page.get(url)
    loginHandle = page.current_window_handle
    page.first_agent_login_button.click()
    page.login_user_name_input.send_keys("02899999")
    page.login_password_input.send_keys("123123")
    page.login_user_code_input.send_keys("dfdsg2165498jdofdfd")
    page.login_button.enter()
    page.hh_buy_button.click()
    allHandle = page.window_handles
    for handle in allHandle:
        if handle != loginHandle:
            page.switch_to_window(handle)
