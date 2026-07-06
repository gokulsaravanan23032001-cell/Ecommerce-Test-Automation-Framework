import time


class DataGenerator:

    @staticmethod
    def generate_name():
        return "Gokul"

    @staticmethod
    def generate_email():
        timestamp = int(time.time())
        return f"gokul_{timestamp}@test.com"