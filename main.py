from Store import Store

def init_Store():
    name = input("Enter a name: ")
    h = Store(name)

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
                h.add_items(item)
        except ValueError:
            print("\nEnter text only!\n")


    return h

def display_list(store):
    # returns the name of the store object
    print(store.name)

def show_options():
    print("0 - exit program123")
    print("1 - enter a store with items")
    print("2 - print statement\n")

def question_user():
    # Throw the while true loop in the main here
    # figure out how to recall the store object and its attributes either in the main or keep it in this function
    # second comment raises question as to how to the object for other fuction user
    # implement a database
    print(f'undefined function')

def main():
    print("Changing the header here what happens next")
    show_options()
    store = None

    while True:
        try:
            option = int(input("Select an option: "))

            if option == 1:
                print("Selected 1")
                store = init_Store()
                #init_Store()
            elif option == 2:
                if store:
                    #store = init_Store
                    display_list(store)
                    print("Option two was ran")
                else:
                    print("No store entered!!")
            elif option == 0:
                break
            else:
                print("\nSelect an option from below!\n")
                show_options()
        except ValueError:
            print("Enter a number")




if __name__ == "__main__":
    main()