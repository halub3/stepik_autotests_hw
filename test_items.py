from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_have_button_add_to_basket(browser):
    browser.get(link)
    # Для проверки
    # time.sleep(30)
    button_cnt = len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket[type=\"submit\"]"))
    assert button_cnt == 1, f"Кнопка не найдена"