# Write a Python program to generate the next 15 leap years starting from a given year. 
# Populate the leap years into a list and display the list.

def nearest_leapyear(year):
    add=4-(year%4)
    if (year%100==0):
        if(year%400==0):
            return year
        else:
            return year+add
    else:
        if(year%4==0):
            return year
        else:
            return year+add
        
        
def next_fifteen_leapyears(year):
    years = []
    next_leapyear = nearest_leapyear(year)
    for i in range(15):
        years.append(next_leapyear + (4*i))
    return years


print(next_fifteen_leapyears(2015))

