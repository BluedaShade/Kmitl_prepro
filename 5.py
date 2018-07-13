""" Prepro """
def main():
    """ Main function """
    num = int(input())
    item_list = []
    for _ in range(num):
        item = input().lower()
        if item == "addictive substances" or item == "cigarettes" or item == "weapons" \
        or item == "alcohol" or item == "illegal items":
            continue
        item_list.append(item)

    for i in item_list:
        print(i)
main()
