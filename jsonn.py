import json as js
# x = '{"name" : "john" , "age" : 10, "city" : "kaduna"}'
# y = js.loads(x)
# print(y)

my_dict = {
    "name" : "judas",
    "age" : 15,
    "city" : "lagos"
}
son_dict = js.dumps(my_dict)
print(son_dict)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(js.dumps(x , indent= 4, separators =(".","="), sort_keys= True))