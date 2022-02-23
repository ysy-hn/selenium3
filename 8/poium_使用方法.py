from poium import Page, Element


# 8种定位方式
class SomePage(Page):
    elem_id = Element(id_='id')
    elem_name = Element(name='name')
    elem_class = Element(class_name='class')
    elem_tag = Element(tag='input')
    elem_link_text = Element(link_text='this_is_link')
    elem_part = Element(partial_link_text='is_link')
    elem_xpath = Element(xpath='//*[@id="kk"]')
    elem_css = Element(css='#id')

    # 设置元素超时时间
    search_input = Element(id_='kw', timeout=5)
    search_button = Element(id_='su', timeout=30)

    # 设置元素描述
    username = Element(css='#loginAccount', describe='用户名')
    password = Element(css='#loginPwd', describe='密码')
    login_button = Element(css='#login_btn', describe='登录按钮')
    user_info = Element(css='#a.nav_user_name > span', describe='用户信息')
