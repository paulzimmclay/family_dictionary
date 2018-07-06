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

family_list = []
for keys, vals in pauls_family.items():
  if vals['age'] == 1:
    family_list.append((f'{vals["name"]} is my {keys} and is {str(vals["age"])} year old.'))
  else:
    family_list.append((f'{vals["name"]} is my {keys} and is {str(vals["age"])} years old.'))

  
print(family_list)