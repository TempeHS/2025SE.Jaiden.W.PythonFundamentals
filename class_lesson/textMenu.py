def main():
    while True:
        display_menu()
        user = input("What would u like? ")
        if selection(user):
            break


def display_menu():
    print("1) Selection 1")
    print("2) Selection 2")
    print("3) Selection 3")
    print("4) Exit")


def selection(user):
    if user == "1":
        print("Anything Else?")
    elif user == "2":
        print("Anything Else?")
    elif user == "3":
        print("Anything Else?")
    elif user == "4":
        print("Thanks for using")
        return True
    else:
        print("Invalid Option")


main()
