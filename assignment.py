
# Exercise 1
def count_characters(text):
    f=len(text)
    return f
    pass

# Exercise 2
def remove_spaces(text):
    return text.replace(" ","")
    pass

# Exercise 3
def count_vowels(text):
    s=0
    for i in range(len(text)):
            if text[i]=="a" or text[i]=="o" or text[i]=="u":
                s+=1
            else:
                if text[i]=="e" or text[i]=="i" or text[i]=="A":
                    s+=1
                else:
                    if text[i]=="E" or text[i]=="I" or text[i]=="O":
                        s += 1
                    else:
                        if text[i]=="U":
                            s += 1
    return s
    pass

# Exercise 4
def replace_vowels(text):
    new_text=""
    vowels="aeiouAEIOU"
    for char in text:
        if char in vowels:
            new_text=new_text+"*"
        else:
            new_text=new_text+char
    pass
    return new_text

# Exercise 5
def count_words(text):
    new=text.split()
    return len(new)
    pass

# Exercise 6
def find_longest_word(text):
    s=text.split()
    f=max(s,key=len)
    return f
    pass
print(find_longest_word("tehas agsgaas"))
