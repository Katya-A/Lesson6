import sys, json

input_name = open("name.csv", encoding='utf-8')
input_hobby = open("hobby.csv", encoding='utf-8')
output = open("name_hobby.csv", "w", encoding='utf-8')
for left, right in zip(input_name, input_hobby):

    output.write(left.rstrip() + ", " + right)

input_name.close()
input_hobby.close()
output.close()
sys.exit(1)