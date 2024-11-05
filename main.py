

def betterSum(lst):
    total_sum = sum(x for x in lst if isinstance(x, (int, float)))  # Сумма всех чисел
    concatenated_str = ''.join(x for x in lst if isinstance(x, str))  # Конкатенация всех строк
    if total_sum == 0:
        return concatenated_str
    return str(total_sum)

def task2(a):
    return all(int(c) % 2 == 0 for c in str(a))

def task3(a):
   return all(int(c) < 5 for c in str(a))

def task4(s):
   return any(c in 'aeiouAEIOU' for c in s)

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))



if __name__ == "__main__":
    l = [1, 2, 3, 4]
    s = ["qwe", "asd", "qwe"]
    print(betterSum(l))  # 10
    print(betterSum(s))  # qweasdqwe
    a = 1348
    print(task2(a))  # False
    a = 2468
    print(task2(a)) # true

    a = 131231
    print(task3(a))# True
    a = 1234
    print(task3(a)) # False
    s = "Hello World"
    print(task4(s))# True
    s = "Hll Wrld"
    print(task4(s)) # False

    print(is_prime(7))  # True
    print(is_prime(10))  # False
    input()

