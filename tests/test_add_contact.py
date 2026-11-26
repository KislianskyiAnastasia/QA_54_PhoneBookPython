import random

import logging

import pytest
from faker import Faker

from data.contact_dataset import INVALID_CONTACT_FIELDS
from models.contact import Contact
from pages import contacts_page
from pages.add_contact_page import ContactPage

fake = Faker()
logger = logging.getLogger(__name__)

@pytest.mark.parametrize(
    "phone",
     [
    fake.numerify("05#########")

     ]
)


def test_add_contact_success(authenticated, phone):
    logger.info(f"test_add_contact_success")
    contact_page = ContactPage(authenticated)
    random_suffix = random.randint(10000, 1000000)

    cantact = Contact(
        name= fake.name(),
        last_name= fake.last_name(),
        phone=phone,
        email = f"test_{random_suffix}@gm.com",
        address="Yokneam-Illit, Ha-oranim6/29",
        description="QA"
    )
    contact_page.create_contact_steps(cantact)


    assert contact_page.contact_card_visible(cantact.phone)


# @pytest.mark.parametrize("phone",[fake.numerify("05#########")])
def test_add_contact_success_all_req_fields(authenticated,phone):
    contact_page = ContactPage(authenticated)

    cantact1 = Contact(
        name = fake.name(),
        last_name= fake.last_name(),
        phone=phone,
        email= fake.email(),
        address= fake.street_address(),
        description = ""
    )
    contact_page.open_contact_form()
    contact_page.fill_contact_form(cantact1)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(cantact1.phone)

# @pytest.mark.parametrize(INVALID_CONTACT_FIELDS)
# def test_add_contact_empty_phone_negative(authenticated, phone,):
#     contact_page = ContactPage(authenticated)
#     contact = Contact(
#         fake.first_name(),
#         fake.last_name(),
#         phone,
#         fake.email(),
#         fake.street_address(),
#         fake.sentence(nb_words=2)
#     )
#     contact_page.create_contact_steps(contact)
#     # assert contact_page.is_alert_visible()
#     assert "Phone number must contain only digits" in contact_page.get_alert_text()
#     contact_page.accept_alert()