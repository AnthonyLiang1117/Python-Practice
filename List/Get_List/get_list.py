def main():
    # delete the pass statement below and write your code here!
    list = []
    while True:
        value = input("Enter a value: ")
        if value == "":
            break
        list.append(value)
    print("Here's the list:")
    print(list)

if __name__ == "__main__":
    main()
