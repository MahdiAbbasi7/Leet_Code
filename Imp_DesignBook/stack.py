stack = []

def display():
    print(stack)

def push():
    input_ = int(input('Enter the number for pushing:'))
    stack.append(input_)
    print(f'{input_} Successfully pushed')

def pop():
    temp=stack[-1]
    stack.pop()
    print(temp, "is deleted.")

while True:
    print(" menu ")
    print("1-push")
    print("2-pop")
    print("3-display")
    print("4-exit")
    choice=input("enter choice-")
    if choice=="1":
        push()
    elif choice=="2":
        pop()
    elif choice=="3":
        display()
    elif choice=="4":
        exit(0)