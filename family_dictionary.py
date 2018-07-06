pauls_family = {
  'wife': {
    'name': 'Katie',
    'age': 40
  },
  'son': {
    'name': 'James',
    'age': 4
  },
  'daughter': {
    'name': 'Penny',
    'age': 1
  }
}

for a, b in pauls_family.items():
  print(f'{b["name"]} is my {a} and is {str(b["age"])} years old.')