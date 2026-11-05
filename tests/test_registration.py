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
