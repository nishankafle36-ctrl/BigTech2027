'''

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
        
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
        
main()



'''
'''
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
       print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
'''


i = 0
while i < 3:
    print("Meow")
    i = i + 1
    