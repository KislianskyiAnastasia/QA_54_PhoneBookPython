import random

from models.contact import Contact
from pages.add_contact_page import ContactPage


def test_add_contact_success(authenticated):
    contact_page = ContactPage(authenticated)
    random_suffix = random.randint(1,1000000)

    cantact1 = Contact(
        "Anastasia",
        "Kislianskyi",
        f"05863{random_suffix}",
        f"nastya_{random_suffix}@gmail.com",
        "Yokneam-Illit, Ha-oranim6/29",
        "QA"
    )
    contact_page.open_contact_form()
    contact_page.fill_contact_form(cantact1)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(cantact1.phone)
