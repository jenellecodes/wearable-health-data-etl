def clean_heartrate_data(data: list) -> tuple:
    cleaned_hr_data = []
    num_rows_removed =0
    # Filter Non- Digit Strings uses isdigit() method, adds number to cleaned_hr_data (), else removes it and stores in it removed[]
    for j in data:
        if j != None and j.isdigit(): 
           cleaned_hr_data.append(int(j))
        else:
            num_rows_removed +=1
    return cleaned_hr_data