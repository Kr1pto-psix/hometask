


def task1():
    l = []
    for i in range(5):
        num = int(input("Enter the number: "))
        l.append(num)

    count = 0
    for i in l:
        if i >= 10 and i <= 100:
                  count += 1
    return count              

def task2():
    pass

def task3():
    pass

if __name__ == "__main__":
    print("Program started")
    print("begin task1")
    print(f"task1: {task1()}")   

