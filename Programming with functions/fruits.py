def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    print(f"reversed: {fruit_list}")
    fruit_list.append("Orange")
    print(f"with orange: {fruit_list}")
    apple_index = fruit_list.index("apple")
    fruit_list.pop(apple_index)
    fruit_list.insert(apple_index, "cherry")
    print(f"cherry instead of apple: {fruit_list}")
    fruit_list.remove("banana")
    print(f"remove banana: {fruit_list}")
    last_item = fruit_list[-1]
    fruit_list.pop(-1)
    print(f"pop {last_item}: {fruit_list}")
    fruit_list.sort()
    print(f"sorted: {fruit_list}")
    fruit_list.clear()
    print(f"cleared: {fruit_list}")


    


def append_orange(list):
    pass

def switch_apple_for_cherry(list):
    pass

def pop_last(list):
    #print popped element
    pass

def sort_list(list):
    pass

def clear_list(list):
    pass

if __name__ == "__main__":
    main()