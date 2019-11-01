#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve,)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # Add tickets to hashtable
    for ticket in tickets: # O(n)
        hash_table_insert(ht, ticket.source, ticket.destination)

    route[0] = hash_table_retrieve(ht, "NONE")

    for i in range(1, length): # O(n)
        # retrive the current using the previous destination as source
        route[i] = hash_table_retrieve(ht, route[i - 1])
    return route
