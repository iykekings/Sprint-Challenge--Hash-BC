#  Hint:  You may not need all of these.  Remove the unused functions.
from typing import List
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights: List, length: int, limit: int):
    ht = HashTable(length or len(weights))

    """
    YOUR CODE HERE
    """
    # insert weights to hash table
    for index, weight in enumerate(weights):
        hash_table_insert(ht, weight, index)


    c_index = None  # complement index
    w_index = None # weight index
    for weight in weights:
        complement = limit - weight
        if hash_table_retrieve(ht, complement):
            # Get index of both by retrieving it from the ht
            c_index = hash_table_retrieve(ht, complement)
            w_index = hash_table_retrieve(ht, weight)
            if complement == weight:
                return (1, 0)
            return (c_index, w_index) if c_index > w_index else (w_index, c_index)
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
