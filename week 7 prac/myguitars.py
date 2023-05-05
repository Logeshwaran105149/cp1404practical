import csv


class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        return self.year < other.year


def load_guitars(filename):
    guitars = []
    with open(filename, "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def save_guitars(filename, guitars):
    with open(filename, "w", newline="") as file:
        csv_writer = csv.writer(file)
        for guitar in guitars:
            csv_writer.writerow([guitar.name, guitar.year, guitar.cost])


def main():
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("These are my guitars:")
    for guitar in guitars:
        print(guitar)

    guitars.sort()
    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(guitar)

    print("\nAdd your new guitar:")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    save_guitars(filename, guitars)

    print("\nNew guitar added successfully!")


if __name__ == "__main__":
    main()
