def list_max(*args):
    max_value = -1e9
    for arg in args:
        for i in arg:            
            if i > max_value:
                max_value = i
    return max_value
    # return max([i for arg in args for i in arg])

def list_min(*args):
    min_value = 1e9
    for arg in args:
        for i in arg:            
            if i <= min_value:
                min_value = i
    return min_value
    # return min([i for arg in args for i in arg])
def list_avg(*args):
    sum_value = 0
    len_value = 0
    for arg in args:
        for i in arg:            
            len_value += 1
            sum_value += i
    
    avg_value = sum_value / len_value

    return avg_value
    
    # one_list = [i for arg in args for i in arg]
    # return sum(one_list) / len(one_list)


