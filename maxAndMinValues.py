def findMaxMin(list):
    max_value = max(list)
    min_value = min(list)
    if max_value == min_value:
        return [len(list)]
    return ([min_value,max_value])