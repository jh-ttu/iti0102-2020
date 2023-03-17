"""This is my first program."""  
name = "Ago"
name = """Ago"""
name = 'Ago'
name = '''Ago'''
print("Hello, ")
print("B!")
print()

#TEST GRUPPP new3, multiple custom grades v334
# persistent 4


name = input('What is your name?')
year = input(f'Hello, {name}! What year were you born in?')
value = int(year)

if value < 2008:
    result = 2008 - value
    print(f'You were {result} years old when Python 3.0 was released.')
else:
    result = value - 2008
    print(f'Python 3 was {result} years old when you were born. ') 
