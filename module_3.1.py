calls = 0
def  count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    length = (len(string))
    upper = string.upper()
    lower = string.lower()
    return (length, upper,lower)
def is_contains(string, list):
    count_calls()
    string_lower = string.lower()
    return string_lower in (item.lower() for item in list)
print(string_info('Capibara'))
print(string_info('Matrix'))
print(is_contains('Urban',['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)







