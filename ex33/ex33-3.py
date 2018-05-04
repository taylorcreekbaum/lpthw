def genList(max_num, inc):
    i = 0
    numbers = []

    while i < max_num:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + inc
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)

genList(100,3)