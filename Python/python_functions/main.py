def hotel_cost(nights):
    return 140*nights


def plane_ride_cost(city):
    if "cape town" :
        print(2500)
    elif "Durban":
        print(2300)
    elif "JHB":
        print(2000)
    elif "BFN":
        print(1800)


def rental_car_cost(days):
    cost = 40 * days

    if cost >= 7:
        cost = cost -50
    elif days >= 3 and days < 7:
        cost = cost -20
    return cost


def new_sum(*numbers):
    return new_sum(numbers)


def trip_cost(city, days):
    return new_sum(rental_car_cost(days), hotel_cost(days), plane_ride_cost(city))


print(trip_cost("cape town", 1))