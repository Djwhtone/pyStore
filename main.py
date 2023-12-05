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

def main():
    print("Hello")
    init_Store()

if __name__ == "__main__":
    main()