from pages import registration_page
from pages.registration_page import RegistrationPage

VALID_EMAIL = "anastasia_26@gmail.com"
VALID_PASSWORD = "Asdasdasd236!"
INVALID_EMAIL = "nastya_26gmail.com"
INVALID_PASSWORD = "Asdasdasd246"


def test_valid_registration_success(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_email_field(VALID_EMAIL)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.click_registration_button()

    assert registration_page.is_sing_out_displayed()


def test_registration_with_invalid_email(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_email_field(INVALID_EMAIL)
    registration_page.fill_password_field(VALID_PASSWORD)
    registration_page.click_registration_button()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_with_invalid_password(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_email_field(VALID_EMAIL)
    registration_page.fill_password_field(INVALID_PASSWORD)
    registration_page.click_registration_button()

    assert "Wrong email or password format" in registration_page.get_alert_text()
    registration_page.accept_alert()

def test_registration_existed_user(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open_registration_page()
    registration_page.fill_email_field("anastasia_26@gmail.com")
    registration_page.fill_password_field("Asdasdasd236!")
    registration_page.click_registration_button()

    assert registration_page.get_alert_text() == "User already exist"
    registration_page.accept_alert()