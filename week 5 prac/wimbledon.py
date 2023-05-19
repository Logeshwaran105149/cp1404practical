def main(filename):
    """The main function that calls the other functions."""
    data = read_file(filename)
    champions = get_champions(data)
    countries = get_countries(data)
    display_results(champions, countries)


def read_file(filename):
    """Reads the given file and returns a list of lists containing the data."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()
    data = [line.strip().split(",") for line in lines]
    return data

def get_champions(data):
    """
    Returns a dictionary containing the champions and the number of times they have won.
    """
    champions = {}
    for row in data:
        if row[0] != "Year":  # Skip the header row
            name = row[2]
            champions[name] = champions.get(name, 0) + 1
    return champions


def get_countries(data):
    """
    Returns a set of the countries of the champions.
    """
    countries = set()
    for row in data:
        if row[0] != "Year":  # Skip the header row
            country = row[1]
            countries.add(country)
    return countries


def display_results(champions, countries):
    """Displays the processed information."""
    print("Wimbledon Champions:")
    for team, wins in champions.items():
        print(f"{team} {wins}")
    print("These", len(countries), "countries have won Wimbledon:")
    print(", ".join(countries))


filename = "wimbledon.csv"
main(filename)
