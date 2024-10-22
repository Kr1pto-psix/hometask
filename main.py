


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
    count = 0
    while count < 100:
        num = int(input("Enter the num: "))
        if num % 10 == 7:
            count += num

def task3():
    l = []
    end = False
    while True:
        num = int(input("Enter the num: "))
        l.append(num)
        if num == 0:
            if end == True:
                break
            end = True
    return l        


if __name__ == "__main__":
    print("Program started")
    print("begin task1")
    print(f"task1: {task1()}")   
    print("task2 begin")
    task2()
    print("task2 end")
    print("task 3 begin")
    print(f"task3: {task3()}")
    


