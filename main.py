from appointment_checker import AppointmentChecker


def main():
    ac = AppointmentChecker()
    results = ac.get_results()
    if len(results) > 0:
        print([r for r in results])


if __name__ == "__main__":
    main()
