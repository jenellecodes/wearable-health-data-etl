from data_cleaning import clean_heartrate_data
from statistical import average
from statistical import median
from statistical import range

# def clean_heartrate_data(data: list) -> tuple:
#     cleaned_hr_data = []
#     num_rows_removed =0
#     # Filter Non- Digit Strings uses isdigit() method, adds number to cleaned_hr_data (), else removes it and stores in it removed[]
#     for j in data:
#         if j != None and j.isdigit(): 
#            cleaned_hr_data.append(int(j))
#         else:
#             num_rows_removed +=1
#     return cleaned_hr_data



# def average(data: list) -> float:
    
#     clean_data=data
#     total_hr = 0
#     for i in clean_data:
#         total_hr = total_hr + i
#     avg_hr =total_hr/len(clean_data)   
#     return round(avg_hr,2)
#      # test 
#      #print(f"This is the sum of hr : {total_hr}" ) 
#      # print(f" This is the average hr : {avg_hr}" ) 
    


# def median(data: list) -> float:
    
#     # 1. Sorting the list
#     sorted_list= sorted(data)
#     length= len(sorted_list)
#     #2. Calculate the median
#     if length % 2 != 0:
#         return sorted_list[length//2]
#     else:
#        return round((sorted_list[length//2] +sorted_list[length//2 -1]) //2, 2)


#     #return sorted_list


# def range(data: list) -> float:
    
#     sorted_list= sorted(data)
#     return sorted_list [-1] - sorted_list[0]

def rolling_avg(data: list, k: int) -> float:
 """""
   clean_data=data
   total_hr = 0
   for i in clean_data:
        if i <= k:
            total_hr = total_hr + i
        else:
            return total_hr/k    

    Was working through the challenge 
    """
 pass

def run(file: str):
    """
    Process heart rate data from the a file by cleaning and
    calculating summary statistics. Print out final values.

    Args:
        filename (str): The path to the data file (e.g., 'data/phase0.txt').

    Returns:
        float, float, float: You will return the average, median, and range.
    """
    data = []
    cleaned_data = []
    # open file using file I/O and read it into the `data` list
    file_obj = open(file) 
    data = file_obj.readlines()

 
    # Use `clean_heartrate_data` to clean the data and remove invalid entries
    #cleaned_list, removed_values = clean_heartrate_data (data)
    #clean_hr_data = clean_heartrate_data(data)

    for item in data:
     cleaned_data.append(item.replace('\n', ''))

    new_data = clean_heartrate_data(cleaned_data)
   
    #calculate the average, median, and range of this file using the functions you've wrote
    average_hr = average(new_data)
    median_hr= median(new_data)
    range_hr = range (new_data)
    #rolling_avg_hr = rolling_avg(clean_hr_data)

    # print out your data quality measure to the console
    #print (f"Cleaned Heart Rate Data: {new_data}")

    # print out your descriptive statistics to the console

    #print(f"Average Heart-Rate {average_hr}")
    #print(f"Median Heart-Rate {median_hr}")
    print(f"Range Heart-Rate {range_hr}")
    #print(f"Average Heart-Rate{rolling_avg_hr} + {int = 10}")

if __name__ == "__main__":
    run("data/phase0.txt")
    run("data/phase1.txt")
    run("data/phase2.txt")
    run("data/phase3.txt")
