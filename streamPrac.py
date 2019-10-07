#포맷 문자열 리터럴
year = 2016
event = 'Referendum'
print(f'results of the {year} {event}')

s = 'hello world.'
print(str(s))
print(repr(s))

table = {'Gj' : 3044, 'hm' : 3042, 'hj' : 1151}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')