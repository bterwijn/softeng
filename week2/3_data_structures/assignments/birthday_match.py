import random

def main():
    people_birthdays = get_random_people_birthdays()
    print('people_birthdays:', people_birthdays)
    matches = find_birthday_matches(people_birthdays)
    print('matches:', matches)

class Date:

    def __init__(self, year: int, month: int, day: int):
        """ Initialize a Date object using 'year', 'month', 'day'. """
        self.year = year
        self.month = month
        self.day = day

    def __repr__(self) -> str:
        """ Return a string representation of the Date object. """
        return f'{self.year:04}-{self.month:02}-{self.day:02}'

    def random_date(year: int) -> 'Date':
        """ Generate a random date in the given 'year'. """
        day = 365 +  (1 if is_leap_year(year) else 0)
        n = random.randint(1, day)
        months = [31, 28 + (1 if is_leap_year(year) else 0), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = 1
        while n > 0:
            if n <= months[month - 1]:
                day = n
                break
            n -= months[month - 1]
            month += 1
        return Date(year, month, day)

def is_leap_year(year: int) -> bool:
    """ Return True if 'year' is a leap year, False otherwise. """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def get_random_people_birthdays() -> dict[str, Date]:
    """ Generate a dictionary of people with their name and random birthday. """
    min_year, max_year = 1900, 2026
    n = 2000
    return {'name'+str(i+1) : Date.random_date(random.randint(min_year, max_year)) for i in range(n)}

def find_birthday_matches(birthdays: dict[str, Date]) -> list[list[str]]:
    """ Returns a list of lists of people who share the same birthday. """
    # Implement thi function
    matches = []
    return matches

if __name__ == "__main__":
    main()
