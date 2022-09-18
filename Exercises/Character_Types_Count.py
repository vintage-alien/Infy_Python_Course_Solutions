# Write a Python function vowel_count(sentence) to return a dictionary with vowels, consonants, 
# others as key and respective number of vowels, consonants, others characters as value.
# Note: Do case insensitive operations
# Example: sentence=“I love python and it so easy to learn”
#                 sample output={“vowels”:12,”consonants”:17, “others”:8}

def vowel_count(sentense):
    vowels = ['a','e','i','o','u']
    consonants = ['m', 'n', 'b', 'v', 'c', 'x', 'z', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'p', 'y', 't', 'r', 'w', 'q']
    vowel,cons,other = 0,0,0
    for letter in sentense:
        if letter.lower() in vowels:
            vowel +=1
        elif letter.lower() in consonants:
            cons += 1
        else:
            other +=1
    type_counts = {}
    type_counts["vowels"] = vowel
    type_counts["consonants"] = cons
    type_counts["others"] = other
    
    return type_counts



print(vowel_count("I love python and it so easy to learn"))