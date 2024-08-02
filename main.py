from appointment_checker import AppointmentChecker
from notifier import Notifier


# TODO: make this run on a schedule
def main():
    ac = AppointmentChecker()
    results = ac.get_results()
    if len(results) > 0:
        message = "NEXUS interview appointments available at the following locations:\n" + "\n".join(results)
        print(message)
        Notifier.notify(message)


if __name__ == "__main__":
    main()
