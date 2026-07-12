import random
import time


class DataGenerator:

    @staticmethod
    def generate_name():
        return "Gokul"

    @staticmethod
    def generate_email():
        timestamp = int(time.time())
        return f"gokul_{timestamp}@test.com"

    @staticmethod
    def generate_password():
        return "Password@123"

    @staticmethod
    def generate_first_name():
        return "Gokul"

    @staticmethod
    def generate_last_name():
        return "Saravanan"

    @staticmethod
    def generate_company():
        return "OpenAI Testing"

    @staticmethod
    def generate_address():
        return "Anna Nagar"

    @staticmethod
    def generate_state():
        return "Tamil Nadu"

    @staticmethod
    def generate_city():
        return "Chennai"

    @staticmethod
    def generate_zipcode():
        return "600040"

    @staticmethod
    def generate_mobile():
        return f"98{random.randint(10000000,99999999)}"