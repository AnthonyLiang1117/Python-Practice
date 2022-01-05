SAMPLE_LIST = ['a', 'b', 'c', 'd', 'e']
MAX_LENGTH = 3

def shorten(lst, max_len):
    # delete the pass statement below and write your code here!
    while len(lst) > max_len:
        popped = lst.pop()
        print(popped)

def main():
    shorten(SAMPLE_LIST, MAX_LENGTH)

if __name__ == "__main__":
    main()
