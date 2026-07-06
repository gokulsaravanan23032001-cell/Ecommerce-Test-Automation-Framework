from utilities.data_generator import DataGenerator


def test_generate_email():

    email = DataGenerator.generate_email()

    print(email)

    assert "@test.com" in email