def weight_average(my_list=[]):
    weighted_sum = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)
    return weighted_sum / total_weight if total_weight != 0 else 0
