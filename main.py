import json

f_name = 'Иванов, Иван, Иванович', 'Петров, Петр, Петрович'
print(type(f_name))
str_f_name = json.dumps(f_name)

with open('name.csv', 'w', encoding='utf-8') as f:
    json.dump(f_name, f, ensure_ascii=False, indent=2)

with open('name.csv', 'r', encoding='utf-8') as f:
    f_name2 = json.load(f)
print(type(f_name2), f_name2)

f_hobby = 'скалолазание', 'охота'
print(type(f_hobby))
str_f_hobby = json.dumps(f_hobby)

with open('hobby.csv', 'w', encoding='utf-8') as f:
    json.dump(f_hobby, f, ensure_ascii=False, indent=2)

with open('hobby.csv', 'r', encoding='utf-8') as f:
    f_hobby2 = json.load(f)
print(type(f_hobby2), f_hobby2)
