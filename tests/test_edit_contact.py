from faker.proxy import Faker

from pages.add_contact_page import ContactPage
from models.contact import Contact
from pages.contacts_page import ContactsPage

fake = Faker


def create_contact():
    import fake
    return Contact(
        name=fake.name(),
        last_name=fake.last_name(),
        phone=fake.numerify("05#########"),
        email=fake.email(),
        address=fake.street_address(),
        description=fake.sentence(nb_words=2)
    )


def test_edit_contact_name_field(authenticated):
    contact_page = ContactPage(authenticated)
    contacts_page = ContactsPage(authenticated)

    contact = create_contact()
    submit_new_contact(contacts_page, contact)
    new_name =fake.first_name()

