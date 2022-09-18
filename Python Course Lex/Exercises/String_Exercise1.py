# Write a Python program to generate the ticket numbers for specified number of passengers
#  traveling in a flight as per the details mentioned below:
# The ticket number should be generated as airline:src:dest:number where

# Consider AL1 as the value for airline

# src and dest should be the first three characters of the source and destination cities.

# number should be auto-generated starting from 101

# The program should return the list of ticket numbers of last five passengers.
# Note: If passenger count is less than 5, then return the list of all generated ticket numbers.

def ticket_generator(src,dest):
    airline = "AL1"
    base_num = 101
    tickets = []
    for i in range(len(src)):
        source_code = src[i][:3]
        dest_code=dest[i][:3]
        ticket= airline+source_code+dest_code+str(base_num)
        tickets.append(ticket)
    return tickets    

src=["MUMBAI", "KOLKATA", "CHENNAI", "DELHI"]
dest=["CHENNAI", "MUMBAI", "BENGALURU", "KOLKATA"]
print(ticket_generator(src, dest))
print(ticket_generator(dest, src))
