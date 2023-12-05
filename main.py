from Store import Store

def init_Store():
    name = input("Enter a name: ")
    kroger = Store(name)

    while True:
        try:
            print("Enter done to finish items.")
            item = input("Enter item: ")
            if item.upper() == "DONE":
                print("Done was executed! Condition was true")
                break
            else:
                kroger.add_items(item)
        except ValueError:
            print("bad input")


    print(kroger)

def main():
    print("Hello")
    init_Store()

if __name__ == "__main__":
    main()