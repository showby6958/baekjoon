while True:
    try:
        num = input()
        if num[0] == '0' and num[-1] == '0':
            break
        
        if num == num[::-1]:
            print("yes")

        else:
            print("no")

    except EOFError:
        break