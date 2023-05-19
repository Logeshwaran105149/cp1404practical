from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def print_taxi_list(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_cost = 0
    current_taxi = None

    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        action = input(">>> ").lower()
        if action == 'q':
            break
        elif action == 'c':
            print("Taxis available:")
            print_taxi_list(taxis)
            taxi_choice = int(input("Choose taxi: "))
            if taxi_choice < 0 or taxi_choice >= len(taxis):
                print("Invalid taxi choice")
            else:
                current_taxi = taxis[taxi_choice]
        elif action == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
                print(f"Bill to date: ${total_cost:.2f}")
                continue
            distance = float(input("Drive how far? "))
            try:
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_cost += trip_cost
                current_taxi.start_fare()
            except Exception as e:
                print(str(e))
                continue
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_cost:.2f}")

    print("Total trip cost: ${:.2f}".format(total_cost))
    print("Taxis are now:")
    print_taxi_list(taxis)


if __name__ == "__main__":
    main()
