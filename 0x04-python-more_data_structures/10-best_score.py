def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None

    max_key = max(a_dictionary, key=a_dictionary.get)
    return max_key
