# Write a python function, encrypt_sentence(msg) which accepts a message and 
# encrypts it based on rules given below and returns the encrypted message.
# characters at odd position -> Reverse It
# characters at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not 
# change
# Note: Assume that the sentence would begin with a word and there will be only a single space between the words.
#     Perform case sensitive string operations wherever necessary.
# Example: msg=the sun rises in the east    output=eht snu sesir ni eht stea


def encrypt_message(message):
    msg_list = message.split()
    encrypted_msg = ""
    for msg in msg_list:
        odd = []
        even_c = []
        even_v = []
        for i in range(len(msg)):
            if(i%2==0):
                odd.append(msg[i])
            else:
                if(msg[i].lower() in ("a","e","i","o","u")):
                    even_v.append(msg[i])
                else:
                    even_c.append(msg[i])

        even = even_c + even_v
        odd.reverse()
        final = ""
        if(len(msg)%2==0):
            for n in range(len(odd)):
                final += odd[n]
                final += even[n]
        else:
            for n in range(len(odd)-1):
                final += odd[n]
                final += even[n]
            final += odd[len(odd)-1]
        encrypted_msg += final+" "
    return encrypted_msg

msg="heavy"
print("Encrypted message : ", encrypt_message(msg))




        
       




msg="the sun rises in the east"
encrypt_message(msg)
        
    

