from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")             # Есть ссылка для входа/регистрации
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")         # Есть форма для входа
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")   # Есть форма регистрации