import memory_graph as mg
import band_schedule
import copy

# copy the initial state from band_schedule.py
schedule    = copy.deepcopy(band_schedule.schedule)
rockets     = copy.deepcopy(band_schedule.rockets)
dragonflies = copy.deepcopy(band_schedule.dragonflies)

def main():
    exercise1(schedule) # already completed
    exercise2(schedule)
    exercise3(schedule)
    exercise4(schedule)
    exercise5(schedule)
    exercise6(schedule)
    exercise7(schedule)
    exercise8(schedule)
    band_schedule.print_schedule(schedule)

def exercise1(schedule):
    """
    Add rockets to week1 of January 2020.
    Add dragonflies to week2 of January 2020.
    """
    schedule[2020]['January'].append(rockets)
    schedule[2020]['January'].append(dragonflies)

def exercise2(schedule):
    """
    In January 2020 add rockets to week3, dragonflies to week4 amd rockets to week5.
    """
    schedule[2020]['January'].append(rockets)
    schedule[2020]['January'].append(dragonflies)
    schedule[2020]['January'].append(rockets)

def exercise3(schedule):
    """
    Add 'John' as last member of the band 'rockets' but only in week3 of January 2020.
    """
    schedule[2020]['January'][2] = schedule[2020]['January'][2].copy()
    schedule[2020]['January'][2].append('John')

def exercise4(schedule):
    """
    Change the name 'Jim' to 'Jimmi' everywhere.
    """
    rockets[1] = 'Jimmi'
    schedule[2020]['January'][2][1] = 'Jimmi'

def exercise5(schedule):
    """
    February 2020 gets the same bands as January 2020.
    """
    schedule[2020]['February'] = schedule[2020]['January']

def exercise6(schedule):
    """
    Remove week5 from February 2020 but leave January 2020 unchanged.
    """
    schedule[2020]['February'] = schedule[2020]['February'][:-1]

def exercise7(schedule):
    """
    March 2020 gets the same bands as January 2020, but add 'Maya' as last member in every week.
    """
    schedule[2020]['March'] = copy.deepcopy(schedule[2020]['January'])
    for week in schedule[2020]['March']:
        if week[-1] != 'Maya':
            week.append('Maya')

def exercise8(schedule):
    """
    2021 gets the same schedule as 2020 but only in January 'Bianca' replaces 'Charlotte'.
    """
    schedule[2021] = copy.deepcopy(schedule[2020])
    january = schedule[2021]['January']
    for week_index in range(len(january)):
        if 'Charlotte' in january[week_index]:
            january[week_index] = january[week_index].copy()
            for person_index in range(len(january[week_index])):
                if january[week_index][person_index] == 'Charlotte':
                    january[week_index][person_index] = 'Bianca'


if __name__ == "__main__":
    main()
