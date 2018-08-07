def unique_in_order(iterable):
    result = []
    last = ''
    for item in iterable:
        if item != last:
            result.append(item)
        last = item
    return result
