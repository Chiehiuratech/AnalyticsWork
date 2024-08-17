from turtle import circle


car = {
    "car1" : "volvo",
    "car2" : "ford",
    "car3" : "toyota",
    "car_model" : "suv",
    "car_lenght" : 29.5,
    "car_color" : "pink",
    "car_color" : "blue"
}
#  assessig an item in a dictionary
car["car2"] = "honda"
make_dict = dict(name = "precious", age = 54, id = 1234)
print(make_dict)
#  using the get method
saved = car.get("car_color")
print("our out put is :", saved)
#  using the keys method
get_keys = car.keys()
print("get all my keys", get_keys)
# using the values method
get_values= car.values()
print(get_values)
# using the item method
get_items = car.items()
print(get_items)
# using the update method
car.update({"car1" : "camry"})
car.update({"car6" : "audi"})
#  using the loop method
for mydict in car.items():
    print(mydict)
# print(car)
child1 = {
    "name" : "john",
    "age" : 16
}
child2 ={
    "name" : "king",
    "age" : 17
}
child3 = {
    "name" : "james",
    "age" : 15
}
super_family = {
    "child" : child1,
    "child2" : child2,
    "child3" : child3
}

print(super_family["child"]["name"])
# print(car, type(car))