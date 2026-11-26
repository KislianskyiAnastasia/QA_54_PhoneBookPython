from itertools import count

import logging
from faker import Faker

from models.contact import Contact
from pages.add_contact_page import ContactPage
from pages.contacts_page import ContactsPage

fake = Faker()
logger = logging.getLogger(__name__)


def create_contact():
    return Contact(
        fake.first_name(),
        fake.last_name(),
        fake.numerify("05########"),
        fake.email(),
        fake.street_address(),
        fake.sentence(nb_words=2)
    )


def test_remove_contact(ensure_min_contacts):
    logger.info(f"test_remove_contact")
    contacts_page = ContactsPage(ensure_min_contacts)

    contacts_page.open_contact_list()
    count_before = contacts_page.get_contact_cards_number()

    logger.info(f"Contacts before delete: {count_before}")

    contacts_page.open_first_contact()
    contacts_page.remove_current_contact()
    count_after = contacts_page.get_contact_cards_number()

    logger.info(f"Contacts after delete: {count_after}")

    assert count_after == count_before -1

def test_remove_all_contact(ensure_min_contacts):
    contacts_page = ContactsPage(ensure_min_contacts)

    contacts_page.open_first_contact()
    contacts_page.remove_all_contacts()

    assert contacts_page.get_contact_cards_number() == 0