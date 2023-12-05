from Store import Store

def init_Store():
    name = input("Enter a name: ")
    kroger = Store(name)

    while True:
        try:
            print("Enter done to finish items.")
            item = input("Enter item: ")
            if item.upper() == "DONE":
                print("\nDone was executed! Condition was true\n")
                break
            elif item.isdigit():
                raise ValueError
            else:
                kroger.add_items(item)
        except ValueError:
            print("\nEnter text only!\n")


    print(kroger)
    print("\n")
    show_options()


def show_options():
    print("0 - exit program")
    print("1 - enter a store with items")
    print("2 - print statement\n")


def main():
    print("Hello")
    show_options()

    while True:
        try:
            option = int(input("Select an option: "))
            if option == 1:
                print("Selected 1")
                init_Store()
            elif option == 2:
                print("Option two was ran")
            elif option == 0:
                break
            else:
                print("\nSelect an option from below!\n")
                show_options()
        except ValueError:
            print("Enter a number")




if __name__ == "__main__":
    main()