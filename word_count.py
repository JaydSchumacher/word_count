def word_count(a_str):
    str = a_str.lower()   
    list = str.split(" ")
    my_dict = {word:list.count(word) for word in list}        
    return my_dict

print(word_count("I do not like it Sam I Am I Sam not"))