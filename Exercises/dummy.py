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

