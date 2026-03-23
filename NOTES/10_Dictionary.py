my_dict = {"name": "Alice", "age": 30} # stores in unique key:value pairs
print(my_dict["age"]) # access value using key

info = {"name": "Alice", "age": 25, "course": "Python"}
info["location"] = "New York" # Adding a new key-value pair
info["age"] = 26 # Modifying an existing value

print("Updated Student Info:", info)

info = {"name": "Alice", "age": 25, "course": "Python"}

del info["course"] # remove a specific pair
rage = info.pop("age") # remove and retrieve a specific pair
info.clear() # clear all elements

print("Updated Student Info:", info)
print("Removed Age:", rage)

info = {"name": "Alice", "age": 25, "course": "Python"}

for key in info: # iterating with keys
    print("Key:", key)

for value in info.values(): # iterating with values
    print("Value:", value)

for key, value in info.items(): # iterate with pairs
    print("Key:", key, ", Value:", value)

person = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "rating": 1550,
    "nationality": "Indian"
}

list_1 = list(person.keys()) # to print keys &
list_2 = list(person.values()) # values separately

print(list_1)
print(list_2)

print("name" in info) # gives True if key exists
print("location" in info) # otherwise False

print(info.get("age")) # gives value if key exists
print(info.get("location")) # otherwise None

nested_dict = {
    "person1": {"name": "Alice", "age": 30}, # Nested Dictionary (2D)
    "person2": {"name": "Bob", "age": 25}
}
nested_dict["person1"]["age"] = 35 # update element
nested_dict["person2"]["location"] = "New York" # add element
nested_dict["person3"] = {"name": "Charlie", "age": 28} # add key:value pair
print(nested_dict)