from locations import locations
import requests


class AppointmentChecker:

    def __init__(self):
        self.results = []
        self.get_locations_with_appointments()

    @staticmethod
    def has_appointments(location):
        response = requests.get(
            f'https://ttp.cbp.dhs.gov/schedulerapi/slots?orderBy=soonest&limit=1&locationId={location}&minimum=1')
        return len(response.json()) > 0

    def get_locations_with_appointments(self):
        for key, value in locations.items():
            if self.has_appointments(key):
                self.results.append(value)

    def get_results(self):
        return self.results




