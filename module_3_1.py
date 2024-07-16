calls = 0
def count_calls(calls):
    calls += 1
    return (calls)

def string_info(string):
    global calls
    calls = count_calls(calls)
    tu = (len(string), string.upper(), string.lower())
    return (tu)
def is_contains(string, list_to_search):
    global calls
    calls = count_calls(calls)
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    string = string.lower()
    if string in list_to_search:
        return True

    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
