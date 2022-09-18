def find_adjuscent(given_list):
    count = 0
    i = 0
    j=i+1
    while j<len(given_list):
        if(given_list[i]==given_list[j]):
            count += 1
        else:
            i=j
        j += 1

    return count

given_list = [[1,1,5,100,-20,-20,6,0,0],[10,20,30,40,30,20],[1,2,2,3,4,4,4,10]]
for list_item in given_list:
    print(find_adjuscent(list_item))