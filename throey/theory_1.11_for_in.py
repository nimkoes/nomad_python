days = ("Mon", "Tue", "Wed", "Thu", "Fri")

print("모든 요소를 출력하는 경우")
for day in days :
  print(day)


print("\nTue 까지만 출력하고 종료하고 싶은 경우")
for day in days :
  if day == "Wed" :
    break
  else :
    print(day)

print("\n문자열도 배열 취급이 된다 !")
for letter in "my text message" :
  print(letter)