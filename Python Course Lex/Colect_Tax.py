result=0
def find_sum(num1,num2):
    if(num1!=num2):
        result=num1+num2
    else:
        result=2*(num1+num2)

find_sum(3,4)
print(result)
find_sum(5,5)
print(result)