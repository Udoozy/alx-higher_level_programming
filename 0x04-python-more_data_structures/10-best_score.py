def best_score(a_dictionary):
    if a_dictionary:
        my_keys = list(a_dictionary.keys())
        size = 0
        largestKey = ""
        for i in my_keys:
            if a_dictionary.keys > size:
                size = a_dictionary[i]
                largestKey = i
        return largestKey
