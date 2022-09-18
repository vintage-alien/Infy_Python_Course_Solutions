# Write a Python function words_count(sentence) to return a dictionary with the length of words
#  as key and number words with such length as value.
# Example: sentence=“I love python and it so easy to learn” sample output={1:1,4:2,5:1,3:1,2:3,6:1}

def word_count(sentense):
    words = sentense.split()
    word_lengths = []
    #word_lenghts - list of concurrent word lengths of words list
    for item in words:
        word_lengths.append(len(item))
    
    #make a dictionary
    dictionary = {}
    for i in range(len(word_lengths)):
        key = word_lengths[i]
        count = 0
        for j in range(len(word_lengths)):
            if(word_lengths[i]==word_lengths[j]):
                count +=1 
        dictionary[key]=count
    return dictionary
        

sent = "I love python and it so easy to learn"
print(word_count(sent))