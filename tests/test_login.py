from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("validUser", "validPass")
    assert "dashboard" in driver.current_url
