from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.data_generator import DataGenerator


def test_register_new_user(driver):

    home = HomePage(driver)
    login = LoginPage(driver)

    home.load()

    home.click_login()

    name = DataGenerator.generate_name()
    email = DataGenerator.generate_email()

    login.signup(name, email)