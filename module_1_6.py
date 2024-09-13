my_dict={'Григорий':1956,"Ольга":1957,"Валерия":1995}
print('Dict:',my_dict)
print('Existing value',my_dict['Ольга'])
print('Not existing value:',my_dict.get('Лариса'))
my_dict.update({'Алексей':1995,
                "Вилена":2024})
print('Modified dict:',my_dict)
my_set={1,2,3,987.56,'zero',5.0,2,1}
print('Set:',my_set)
list_=((6,8),'one')
my_set.remove(5.0)
my_set.add(list_)
print('Modified set:',my_set)