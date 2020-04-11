'''
# print welcome message
print("Hello Python !")

message = "Hello world !"
print(message)

message = 'I\'m Thien!' 
print(message)

message2 = "i'm thien 2!"
print(message2)

message3 = """i'm thien
3 la tao 
"""
print(message3)

message = 'I\'m Thien!' 
print(len(message)) # length = 10

print(message[1]) # '
print(message[-2]) # n
print(message[0:6]) # I'm Th || [:6]
print(message[6:]) # ien!


mess = "Hello World"
print(mess.lower()) # hello world
print(mess.upper()) # HELLO WORLD
print(mess.count('l')) # 3
print(mess.count('lo')) # 1
print(mess.find('l')) # 2
print(mess.find('World')) # 6
print(mess.find('Thien')) # -1 

new_mess = mess.replace('World', 'Thien')
print(new_mess) # Hello Thien

'''
greeting = 'Hello'
name = 'Thienkute'

# message = '{}, {}. Welcome!'.format(greeting, name)
# message = f'{greeting}, {name}. Welcome!'

# print(message)
print(dir(name))
print(help(str))
print(help(str.lower))

