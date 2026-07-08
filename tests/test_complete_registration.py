from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utilities.data_generator import DataGenerator


def test_complete_registration(driver):

    home = HomePage(driver)
    login = LoginPage(driver)
    registration = RegistrationPage(driver)

    home.load()
    home.click_login()

    name = DataGenerator.generate_name()
    email = DataGenerator.generate_email()

    login.signup(name, email)

    registration.select_title()

    registration.enter_password("Password@123")

    registration.select_date_of_birth(
        "10",
        "May",
        "2001"
    )