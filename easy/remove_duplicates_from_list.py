"""Write a program to remove Duplicates: Remove duplicates from a list."""


def remove_duplicates_using_set(input_list):
    updated_list = list(set(input_list))
    return updated_list


def remove_duplicates_using_loop(input_list):
    updated_list = []
    for i in input_list:
        if i not in updated_list:
            updated_list.append(i)
    return updated_list


def main():
    input_1 = input("Enter list of numbers separated by spaces:")
    input_list = input_1.split(sep=' ')
    print('Input list :', input_list)
    updated_list_using_set = remove_duplicates_using_set(input_list)
    updated_list_using_loop = remove_duplicates_using_loop(input_list)
    print(updated_list_using_loop.sort() == updated_list_using_set.sort())
    print('Updated list using set:', updated_list_using_set)
    print('Updated list using loop:', updated_list_using_loop)


if __name__ =="__main__":
    main()
