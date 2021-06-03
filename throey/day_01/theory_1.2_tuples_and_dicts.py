days_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
days_tuple = ("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")

print(type(days_list))
print(type(days_tuple))

print("--------------------------------------")
print(days_list)
print(days_tuple)


myDictionary = {
  "key" : "value",
  "another" : "something",
  "age" : 21,
  "food" : ["Kimchi", "Bibimbob"],
  "hobby" : ("programming", "hang out"),
  "score" : 4.3
}

print(type(myDictionary))
print(myDictionary)
print()
print("===== add something =====")
print("key : handsome")
print("value : True")

myDictionary["handsome"] = True
print()
print(myDictionary)
print()
print("===== print key 'handsome' =====")
print(myDictionary["handsome"])