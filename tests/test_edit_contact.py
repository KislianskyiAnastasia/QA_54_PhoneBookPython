import logging
from faker import Faker

from models.contact import Contact
from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage

fake = Faker()
logging = logging.getLogger(__name__)

def create_contact():
    return Contact(
        fake.first_name(),
        fake.last_name(),
        fake.numerify("05#########"),
        fake.email(),
        fake.street_address(),
        fake.sentence(nb_words=2))



def test_edit_contact_name_field(authenticated):
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)

    contact = create_contact()
    contact_page.create_contact_steps(contact)
    new_name = fake.first_name()

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_contact_mode()
    contacts_page.set_edit_mode(contacts_page.FIRST_NAME_INPUT, new_name)
    contacts_page.submit_edit()

    assert contacts_page.contact_name_updated() == new_name

def test_edit_contact_last_name_field(authenticated):
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)

    contact = create_contact()

    contact_page.create_contact_steps(contact)

    new_name = fake.last_name()

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_contact_mode()
    contacts_page.set_edit_mode(contacts_page.LAST_NAME_INPUT, new_name)
    contacts_page.submit_edit()

    assert contacts_page.contact_last_name_updated() == new_name

def test_edit_contact_phone_field(authenticated):
    logging.info("test_edit_contact_phone_field")
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)

    contact = create_contact()

    contact_page.create_contact_steps(contact)

    new_phone = fake.numerify(text="05#########")
    logging.debug(f"Old phone number: {new_phone}")
    logging.debug(f"New phone number: {new_phone}")

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_contact_mode()
    contacts_page.set_edit_mode(contacts_page.PHONE_INPUT, new_phone)
    contacts_page.submit_edit()

    assert contacts_page.contact_cards_visible(new_phone)

def test_edit_contact_email_field(authenticated):
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)

    contact = create_contact()

    contact_page.create_contact_steps(contact)

    new_email = fake.email()

    contacts_page.open_contact_details_card(contact.phone)
    contacts_page.open_edit_contact_mode()
    contacts_page.set_edit_mode(contacts_page.EMAIL_INPUT, new_email)
    contacts_page.submit_edit()

    assert contacts_page.contact_email_updated() == new_email