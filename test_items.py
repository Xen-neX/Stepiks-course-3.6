import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket(browser):
    browser.get(link)
    # строку ниже нужно расскоментировать при проверке fr или другого языка!
    # time.sleep(30)
    assert browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket"), 'Ошибка - кнопка не найдена'
