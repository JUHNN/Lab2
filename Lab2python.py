def display_main_menu(list):
    print("Enter some numbers separated by commas (e.g. 5,67,32)")

def get_user_input():
    x = input()
    str_list = x.split(",")
    float_list = []
    for string in str_list:
        float_num = float(string)
        float_list.append(float_num)
    return(float_list)

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()



def calc_avg(list):
    print("average")


def min_max(list):
    print("something")

def sort_temp(list):
    print("list")

def calc_median_temp(list):
    print("median")

if __name__ == "__main__":
    main()