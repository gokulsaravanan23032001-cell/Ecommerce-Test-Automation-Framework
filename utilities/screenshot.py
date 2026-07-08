import os
from datetime import datetime


class Screenshot:

    @staticmethod
    def take(driver, test_name):

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"screenshots/{test_name}_{timestamp}.png"

        driver.save_screenshot(filename)

        return filename