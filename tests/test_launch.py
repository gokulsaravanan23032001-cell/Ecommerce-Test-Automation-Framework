from pages.home_page import HomePage


def test_launch_browser(driver):
    home_page = HomePage(driver)

    home_page.load()

    assert "Automation Exercise" in driver.title