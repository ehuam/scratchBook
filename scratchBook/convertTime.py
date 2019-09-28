from datetime import datetime
import pprint

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k,v = line.strip().split(',')
        flights[k] = v

    pprint.pprint(flights)
    print()

    flights2 = {}

    for time, flight in flights.items():
        flights2[convert2ampm(time)] = flight.title() 

    pprint.pprint(flights2)
