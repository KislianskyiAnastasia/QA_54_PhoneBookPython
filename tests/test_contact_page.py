import random
from faker import Faker

from models.contact import Contact
from pages.add_contact_page import ContactPage

fake = Faker()
def test_add_contact_success(authenticated_client):
    contact_page = ContactPage(authenticated_client)
    random_suffix = random.randint(10000, 99999)
    contact = Contact(
        "User_first_name",
        "User_last_name",
        f"09876543{random_suffix}",
        f"user{random_suffix}@rtu.com",
        "User_address",
        fake.sentence(nb_words=4)
    )

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()
    assert contact_page.contact_card_visible(contact.phone)

def test_add_contact_all_req_fields_success(authenticated_client):
    contact_page = ContactPage(authenticated_client)
    contact = Contact(
        name = fake.name(),
        last_name =fake.last_name(),
        phone = fake.numerify("05#########"),
        email= fake.email(),
        address = fake.street_address(),
        description = ""
    )
    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    contact_page.submit_contact()
    assert contact_page.contact_card_visible(contact.phone)