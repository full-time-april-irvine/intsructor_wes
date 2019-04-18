my_list = ["user1", "user2", "user3", "user4"]

user = {
    'user_id': 1,
    'favorite_color': "mint",
    'first_name': "Wes"
}

users = [
    {
        'user_id': 1,
        'favorite_color': "mint",
        'first_name': "Wes"
    }
]

print(users[0]["user_id"])

session = {}
session['favorite_color'] = "mint"
session['user_id'] = 1
session['first_name'] = "Wes"

# def some_function():
#     print("running the function")
#     # end the function
#     # returns the code execution to the caller
#     # DOES NOT PRINT ANYTHING
#     # returns the actual value to the caller's location
#     return 10
#     print("after the return")

# some_number = some_function()
# print("after the function")
# print(some_number)