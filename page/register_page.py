from poium import Page,Element

class RegisterPage(Page):
    """产品注册page"""

    register_dog_number_input = Element(css="#DogNo",describe="注册狗号输入框")
    register_dog_verification_code_input = Element(css="#VerificaCode",describe="注册狗验证码输入框")
    submit_verification_button = Element(css="#ConfirmInfo",describe="提交验证按钮")
    agent_name_input = Element(css="#AgentName",describe="代理商销售人员名字输入框")
    contact_input = Element(css="#UserName",describe="联系人输入框")
    customer_email_input = Element(css="#Email",describe="客户邮箱输入框")
    company_name_input = Element(css="#CompanyName",describe="公司名称输入框")
    address_input = Element(css="#Address",describe="详细通讯地址输入框")
    industry_select = Element(css="#IndustryID_chzn",describe="所属行业下拉")
    industry_list_select_it = Element(css="#IndustryID_chzn_o_4",describe="所属行业列表选择‘IT’")
    province_select = Element(css="#AreaID_chzn",describe="省份下拉")
    province_list_select_sichuan = Element(css="#AreaID_chzn_o_1",describe="省份下拉列表选择‘四川’")
    mobile_number_input = Element(css="#MobileTel",describe="手机号码输入框")
    fixed_telephone_input = Element(css="#Tel",describe="固定电话1输入框")
    company_contact_radio = Element(xpath="//*[@id='dch']/div[1]/div/div/label[5]/input",describe="公司联系人单选按钮‘其他’")
    channel_radio = Element(xpath="//*[@id='dch']/div[2]/div/div/label[6]/input",describe="知晓渠道单选按钮‘其他’")
    is_website_radio = Element(xpath="//*[@id='dch']/div[3]/div/div/label[2]/input",describe="有无网站单选按钮‘无’")
    is_network_radio = Element(xpath="//*[@id='dch']/div[4]/div/div/label[2]/input",describe="是否联网单选按钮‘无’")
    is_exist_branch_radio = Element(xpath="//*[@id='dch']/div[5]/div/div/label[2]/input",describe="是否有分支机构单选按钮‘否’")
    computer_count_radio = Element(xpath="//*[@id='dch']/div[6]/div/div/label[5]/input",describe="电脑数量单选按钮‘50台以上’")
    submit_register_button = Element(css="#ConfirmInfo",describe="提交注册信息按钮")
