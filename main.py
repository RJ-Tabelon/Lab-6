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

def decode(password):
    decoded = ""
    for char in password:
        decode_char = str((int(char) - 3) % 10)
        decoded += decode_char
    return decoded

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            password = input("Please enter your password to encode: ")
            new_pass = encode(password)
            print("Your password has been encoded and stored!")
        if option == 2:
            org_pass = decode(new_pass)
            print(f"The encoded password is {new_pass}, and the original password is {org_pass}.")
        if option == 3:
            break

if __name__ == "__main__":
    main()




