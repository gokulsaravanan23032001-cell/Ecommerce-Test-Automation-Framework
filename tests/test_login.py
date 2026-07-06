from pages.home_page import HomePage


def test_open_login_page(driver):
    home = HomePage(driver)

    home.load()

    home.click_login()

    assert "login" in driver.current_url.lower()