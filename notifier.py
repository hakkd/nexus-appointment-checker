from functools import partial
from mac_notifications import client


class Notifier:
# TODO: make notifications send (desktop, email, whatsapp?)
    @staticmethod
    def notify(message):
        client.create_notification(
            title="NEXUS appointments available at the following locations:",
            text=message
        )
