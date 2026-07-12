from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from utilities.data_generator import DataGenerator
from config.config_reader import ConfigReader
import time



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

    registration.enter_password(ConfigReader.get_password())

    registration.select_date_of_birth(
        "10",
        "May",
        "2001"
    )

    registration.subscribe_newsletter()

    registration.subscribe_offers()

    registration.enter_address_information(
        DataGenerator.generate_first_name(),
        DataGenerator.generate_last_name(),
        DataGenerator.generate_company(),
        DataGenerator.generate_address(),
        "India",
        DataGenerator.generate_state(),
        DataGenerator.generate_city(),
        DataGenerator.generate_zipcode(),
        DataGenerator.generate_mobile()
    )

    registration.click_create_account()

    assert registration.is_account_created()

    registration.click_continue()

    registration.click_delete_account()

    assert registration.is_account_deleted()

    registration.click_continue()


