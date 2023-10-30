def encode(password):
    new_pass = ""
    for i in password:
        i = int(i)
        if i >= 7:
            if i == 7:
                i = "0"
            if i == 8:
                i = "1"
            if i == 9:
                i = "2"
            new_pass += i
        else:
            i += 3
            i = str(i)
            new_pass += i
    return new_pass

def main():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    while True:
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            new_pass = encode(password)
            print("Your password has been encoded and stored!")
        if option == 2:
            print(f"The encoded password is {new_pass}, and the original password is {variable}")
        if option == 3:
            break

if __name__ == "__main__":
    main()




