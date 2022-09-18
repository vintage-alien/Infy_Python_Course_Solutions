# Represent a small bilingual (English-Swedish) glossary given below as a Python dictionary
# {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} 
# and use it to translate your Christmas wishes from English into Swedish.
# That is, write a Python function translate(b_dict,list_words) that accepts the bilingual
# dictionary and a list of English words (your Christmas wish) and returns a list of equivalent Swedish words.


def translate(d_dict, wish_message):
    wish_msg = []
    for wish in wish_message:
            wish_msg.append(d_dict[wish.lower()])
    return wish_msg   



d_dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} 
message= ["happy", "Christmas"]
print(translate(d_dict, message))

