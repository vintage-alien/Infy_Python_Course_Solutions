# Given a string containing uppercase characters (A-Z), compress the string using Run Length 
# encoding. Repetition of character has to be replaced by storing the length of that run.
# Write a python function encode(message)  which performs the run length encoding for a given 
# String and returns the run length encoded String.
# Provide different String values and test your program.
# Example: message=AAAABBBBCCCCCCCC  output: 4A4B8C

def encode(message):
    encoded_msg = ""
    count = 1
    i=0
    while i < len(message)-1:        
        if (message[i]==message[i+1]):
            count +=1
            if (i==len(message)-2):
                encoded_msg += (str(count)+message[i])
        else:
            encoded_msg += (str(count)+message[i])
            count=1
        i+=1
    return encoded_msg

msg="AAAABBBBCCCCCCCC"
print(encode(msg))  




          