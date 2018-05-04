def genList(max_num, inc):
    numbers = []

    for i in range(0, max_num, inc,):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

genList(100,3)