age = int(input("How old are you? "))

bus_fare = 4.25
fare_type = "standard"

# Kids ride for free.
if age < 5:
    bus_fare = 0
    fare_type = "kids"

# Seniors get a dollar off.
if age >= 60:
    bus_fare = bus_fare - 1
    fare_type = "senior"

print("The " + fare_type + " bus fare is $" + str(bus_fare) + ".")
