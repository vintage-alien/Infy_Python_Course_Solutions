#count number of words in a given sentense

def count_words(sentense):
    words = sentense.split()
    return len(words)

sen = "hey pal! how are you"
print("Total number of words present is ", count_words(sen))