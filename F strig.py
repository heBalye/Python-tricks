from datetime import datetime
first_name = 'Jinliang'
last_name = 'Fu'
sentence = 'My name is {} {} '.format(first_name, last_name)
sentence_2 = f'My name is {first_name.upper()} {last_name.upper()}'
person = {'name': 'Daniel', 'age': 23}

for n in range(1, 11):
    print(f"The value is {n:05}")

pi = 3.14159265

print(f'Pi is equal to {pi:.4f}')


birthday = datetime(1990, 1, 1)

print(f'My birthday is {birthday:%B %d,%Y}')
print(f'{100000000:,}')
