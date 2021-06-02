days = "MON,TUE,WED,THU,FRI,SAT,SUN"
print(days)

day_one = "MON"
day_two = "TUE"
day_three = "WED"
day_four = "THU"
day_five = "FRI"
day_six = "SAT"
day_seven = "SUN"
print(day_three)

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
print(days)
print(type(days))


days_week = ["MON", "TUE", "WED", "THU", "FRI"]
days_weekend = ["SAT", "SUN"]

print("MON" in days_week)
print("MON" in days_weekend)
print("TUE" not in days_week)
print("TUE" not in days_weekend)

print("------------------------------------------------------------------------------------")

print(days_week + days_weekend)
print(2 * days_week)
print(days_weekend * 3)

print("------------------------------------------------------------------------------------")

print(days_week[-1], days_week[0], days_week[1])
print(days_week[2 : 3])
print(days_week[0:4:2])

print("------------------------------------------------------------------------------------")

print(len(days_week), len(days_weekend))
print(min(days_week), max(days_week))
print(min(days_weekend), max(days_weekend))

print("------------------------------------------------------------------------------------")

print(days_week.index("THU", 0))
print(days_week.index("THU", 1))
print(days_week.index("THU", 2))
print(days_week.index("THU", 0, 4))
print(days_week.index("THU", 1, 4))
print(days_week.index("THU", 2, 4))

print("------------------------------------------------------------------------------------")

print(days_week.count("FRI"))
print(days_week.count("NIMKOES"))

print("------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------")

print(days_week)
print(days_weekend)


days_week = ["MON", "TUE", "WED", "THU", "FRI"]
days_weekend = ["SAT", "SUN"]

print("01 : ", days_week)

days_week[0] = "nimkoes"
print("02 : ", days_week)

days_week[0 : 2] = ["MY", "TEST", "DATA", "INPUT"]
print("03 : ", days_week)

del days_week[2 : 3]
print("04 : ", days_week)

days_week[1:5:2] = ["ANOTHER", "SAMPLE"]
print("05 : ", days_week)

del days_week[1:6:2]
print("06 : ", days_week)

days_week.append("ADD")
print("07 : ", days_week)

days_week.clear()
print("08 : ", days_week)


days_week = ["MON", "TUE", "WED", "THU", "FRI"]
print("09 : ", days_week)

days_week.extend(days_week)
print("10 : ", days_week)

days_week *= 2
print("11 : ", days_week)

days_week.insert(0, "ADD_FIRST")
print("12 : ", days_week)

days_week.pop(2)
print("13 : ", days_week)

days_week.remove("MON")
print("14 : ", days_week)

days_week.reverse()
print("15 : ", days_week)
