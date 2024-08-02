import pywhatkit as kit
from dotenv import load_dotenv
import os


class Notifier:

    @staticmethod
    def notify(message):
        load_dotenv()
        contacts = os.getenv("CONTACTS").split(", ")
        for contact in contacts:
            print(contact)
            kit.sendwhatmsg_instantly(contact, message)


if __name__ == "__main__":
    Notifier.notify("test")