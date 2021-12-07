d= {"phone": "Телефон", "water": "Вода","opel vectra b": "корыто"}    
word = input()
trans_word=input()
if not word in d.keys():
    d[word] = trans_word
print(d)