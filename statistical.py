# File contains stattisical functions

import statistics as stats

def average(data: list) -> float:

    avg= stats.mean(data)
    return round(avg)

    
    # clean_data=data
    # total_hr = 0
    # for i in clean_data:
    #     total_hr = total_hr + i
    # avg_hr =total_hr/len(clean_data)   
    # return round(avg_hr,2)

def median(data: list) -> float:
    
    # 1. Sorting the list
    sorted_list= sorted(data)
    length= len(sorted_list)
    #2. Calculate the median
    if length % 2 != 0:
        return sorted_list[length//2]
    else:
       return round((sorted_list[length//2] +sorted_list[length//2 -1]) //2, 2)

def range(data: list) -> float:
    
    sorted_list= sorted(data)
    return sorted_list [-1] - sorted_list[0]