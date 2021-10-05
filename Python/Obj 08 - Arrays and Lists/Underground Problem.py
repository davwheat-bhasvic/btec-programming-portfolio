"""
2 points

Each line on the London underground has several stations. The Victoria line has these stations in the following order:
Brixton, Stockwell, Vauxhall, Pimlico, Victoria, Green Park, Oxford Circus, Warren Street, Euston, King's Cross,
Highbury & Islington, Finsbury Park, Seven Sisters, Tottenham Hale, Blackhorse Road and Walthamstow Central.

Write a program that allows the user to input two stations. A function should return the number of stops between the
two stations. The station names can be input in any order, but you can make the problem easier by only inputting stations
in the correct order if you need to.
"""

stops = [
    "Brixton",
    "Stockwell",
    "Vauxhall",
    "Pimlico",
    "Victoria",
    "Green Park",
    "Oxford Circus",
    "Warren Street",
    "Euston",
    "King's Cross",
    "Highbury & Islington",
    "Finsbury Park",
    "Seven Sisters",
    "Tottenham Hale",
    "Blackhorse Road",
    "Walthamstow Central",
]


def validate_station(station):
    if station not in stops:
        return False
    return True


def station_input():
    while True:
        station = input("Enter a station: ")
        if validate_station(station):
            return station
        print("Invalid station")


start = station_input()
end = station_input()

startIndex = stops.index(start)
endIndex = stops.index(end)

stops = abs(startIndex - endIndex)

if stops == 1:
    print(f"There is 1 stop between {start} and {end}.")
else:
    print(f"There are {stops} stops from {start} to {end}.")
