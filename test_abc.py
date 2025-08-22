# # def test_multi_context(playwright):

# #     browser = playwright.webkit.launch(headless=False)
# #     context1 = browser.new_context()
# #     context2 = browser.new_context()
# #     page1 = context1.new_page()
# #     page2 = context2.new_page()
# #     page1.goto("https://httpbin.org/")
# #     page2.goto("https://example.com/")
# #     assert page1.title() != page2.title()
# #     context1.close()
# #     context2.close()
# #     browser.close()


# # # from collections import Counter
# # # from random import randint
# # # import requests
# # # from playwright.sync_api import sync_playwright

# # # # Generate a list of random numbers and filter unique elements
# # # # arr = [i * randint(1, 10) for i in range(1, 20)]
# # # # print(arr)
# # # # count = Counter(arr)
# # # # arr[:] = [i for i in arr if count[i] == 1]
# # # # print(arr)

# # # # Send a POST request using requests library
# # # payload = {
# # #     "title": "foo",
# # #     "body": "bar",
# # #     "userId": 1
# # # }
# # # headers = {
# # #     "Content-Type": "application/json",
# # #     "Charset": "UTF-8"
# # # }
# # # # response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload, headers=headers)
# # # # print(response.json())
# # # # assert response.json()['title'] == 'foo'



# # # # Send a POST request using Playwright
# # # def test_api(playwright: sync_playwright):
# # #     api_req_context = playwright.request.new_context(base_url="https://jsonplaceholder.typicode.com")
# # #     response = api_req_context.post("/posts", data=payload, headers=headers)
# # #     assert response.status == 201
# # #     print(response.json())





# def logger(func):
#     def wrapper(*args,**kwargs):
#         print("Hello Worlds")
#         return func(*args,**kwargs)
#     return wrapper

# @logger
# def print_name():
#     print("Rahul")

# print_name()



# import pytest



# # add_two(10,

#Anagrams

test = "rahul"
test1 = "halur"

a1 = set(test)
a2 = set(test1)

if(a1==a2):
    print(a1,a2)
    print("yes anagrams")
