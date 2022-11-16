from property_decorator import student

s = student('saurav')
del s.name
s.name = 'Bill'
print(s.name)
