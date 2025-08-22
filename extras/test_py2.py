# # import pytest


# # @pytest.fixture(scope="function")
# # def prework():
# #     print("Prework function executed.")
# #     yield  # This allows the test to run after the prework is executed
# #     print("Postwork function executed.")  # Optional cleanup after the test

# # def add(x, y):
# #     return x + y

# # @pytest.mark.smoke
# # def test_add(prework):
# #     assert add(2, 3) == 5
# #     print("Test executed successfully.")

# ml = [i for i in range(1,10,1) if i%2!=0 ]
# print(ml)

# json = [{"name":"rahul","class":12,"rollno":1},
#         {"name":"sachin","class":12,"rollno":2},    
#         {"name":"sourav","class":12,"rollno":3}]

# add = lambda x,y: x+y

# new_list = tuple(map(lambda x: add(x, 10), ml))
# print(new_list)

# l1 = [i for i in range(1,10,1) ]

# # newList = list(filter(lambda x:x%2==0, l1))
# # print(newList)

# print(l1[::-1])


class Car:
    @classmethod
    def print(cls):
        print("This is a car class")

Car.print()