import memory_graph as mg
import copy

# create initial schedule
schedule = {2020: [], 2021: [], 2022: []}
schedule[2020] = {'January': [], 'February': []}

# bands
rockets     = ['The Rockets:', 'Jim', 'Charlotte', 'Emma']
dragonflies = ['Dragonflies:', 'Lisa', 'Alexander', 'Lucas']

def main():
    exercise1(schedule) # already completed
    exercise2(schedule)
    exercise3(schedule)
    exercise4(schedule)
    exercise5(schedule)
    exercise6(schedule)
    exercise7(schedule)
    exercise8(schedule)
    print_schedule(schedule)

def exercise1(schedule):
    """
    Add rockets to week1 of January 2020.
    Add dragonflies to week2 of January 2020.
    """
    schedule[2020]['January'].append(rockets)
    schedule[2020]['January'].append(dragonflies)

def exercise2(schedule):
    """
    In January 2020 add rockets to week3, dragonflies to week4 and rockets to week5.
    """

def exercise3(schedule):
    """
    Add 'John' as last member of the band 'rockets' but only in week3 of January 2020.
    """

def exercise4(schedule):
    """
    Change the name 'Jim' to 'Jimmi' everywhere.
    """

def exercise5(schedule):
    """
    February 2020 gets the same bands as January 2020.
    """

def exercise6(schedule):
    """
    Remove week5 from February 2020 but leave January 2020 unchanged.
    """

def exercise7(schedule):
    """
    March 2020 gets the same bands as January 2020, but add 'Maya' as last member in every week.
    """

def exercise8(schedule):
    """
    2021 gets the same schedule as 2020 but only in January 'Bianca' replaces 'Charlotte'.
    """

def print_schedule(schedule):
    """ Prints the schedule. """
    for year in schedule:
        print(year)
        for month in schedule[year]:
            print(f'  {month}')
            for index, band in enumerate(schedule[year][month]):
                print(f'    week{index+1}   {" ".join(band)}')

if __name__ == "__main__":
    main()
