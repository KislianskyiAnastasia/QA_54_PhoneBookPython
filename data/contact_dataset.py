import pytest
from faker import Faker
fake = Faker()

PHONE_ALERT_TEXT = " Phone not valid: Phone number must contain only digits! And length min 10, max 15!"
EMAIL_ALERT_TEXT = "Email not valid: Email address is not valid!"

INVALID_CONTACT_FIELDS = [
    pytest.param("phone","1234",PHONE_ALERT_TEXT,id="phone_is_empty"),
    pytest.param("phone",fake.numerify("#" * 20),PHONE_ALERT_TEXT,id="phone_is_invalid"),
    pytest.param("phone",("aasdfaadasdhdg"),PHONE_ALERT_TEXT,id="phone_is_invalid"),
    pytest.param("email","jhewghdjhsd",EMAIL_ALERT_TEXT,id="Email not valid"),
    pytest.param("email","testgmail.com",EMAIL_ALERT_TEXT,id="Email not valid"),
]
