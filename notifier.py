import pywhatkit as kit
from dotenv import load_dotenv
import os


class Notifier:

    @staticmethod
    def __notify_macos(message):
        title = "NEXUS Interview Alert"
        command = f"""
        osascript -e 'display notification "{message}" with title "{title}"'
        """
        os.system(command)

    @staticmethod
    def __notify_whatsapp(message):
        load_dotenv()
        contacts = os.getenv("CONTACTS").split(", ")
        for contact in contacts:
            print(contact)
            kit.sendwhatmsg_instantly(contact, message)

    @staticmethod
    def notify(message):
        Notifier.__notify_macos(message)