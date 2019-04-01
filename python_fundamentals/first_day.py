# print("hello world")

# int
my_int = 10
# float
my_float = 10.5
# str
my_string = "hello world"
# bool
my_bool = True
# list
my_list = ["one", "two", 3]
# dict
my_dict = {
    "eye_color": "blue"
}
# tuple
my_tuple = (1, 2, 3, 4)
# None



# print(str(10) + "hello world")

# for(var i = 0; i < 10; i++) {
#     console.log(i);
# }

# for pizza in my_list:
#     print(pizza)
#     print("hello")

# for i in range(10, 0, -1):
#     print(i)

def run_me(arg1, arg2, arg3):
    print(arg3)

# run_me(arg3 = 1, arg1 = 3, arg2 = 5)

def push_front(lst, val):
    lst.append(None)
    for i in range(len(lst) - 1, 0, -1):
        lst[i] = lst[i - 1]
    lst[0] = val
    return lst

# print(push_front([2, 3, 4], 1))

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

errors = ['First name must be 2 characters long', 'Last name must be 2 characters long']
# errors = []
if errors:
    for error in errors:
        print(error)

print(bool(errors))