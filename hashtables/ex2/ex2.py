class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

cache = {}

def reconstruct_trip(tickets, length):
    # create an empty route array
    route = []
    # for every ticket in the tickets array,
    # add the ticket to the cache by using
    # the ticket source as the key, and 
    # the ticket destination as the value
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    # initial setup, knowing the original flight has a source of NONE
    # append it to the list with the key NONE from the cache
    route.append(cache['NONE'])

    # iterate over the length of the tickets array,
    # finding the next value in the routes array
    for index in range(length):
        # if the value from route is in the cache (which it should be)
        if route[index] in cache:
            # first check to make sure we aren't re-adding the initial value
            if cache[route[index]] == route[0]:
                continue
            # add the remaining stops to the route array,
            # by grabbing the value at route[index]
            # and pulling it's value out of the cache
            route.append(cache[route[index]])

    # when we get to this point, we have a full route
    return route

