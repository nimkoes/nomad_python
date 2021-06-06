def sum(x, y):
  return int(x) + int(y)

def difference(x, y):
  return int(x) - int(y)

def product(x, y):
  return int(x) * int(y)

def quotient(x, y):
  return int(x) / int(y)

def floored_quotient(x, y):
  return int(x) // int(y)

def reminder(x, y):
  return int(x) % int(y)

def negated(x):
  return -int(x)

print("========== sum ==========")
print(sum(12, 17))
print(sum(12, "17"))
print(sum("12", 17))
print(sum("12", "17"))

print("========== difference ==========")
print(difference(12, 17))
print(difference(12, "17"))
print(difference("12", 17))
print(difference("12", "17"))

print("========== product ==========")
print(product(12, 17))
print(product(12, "17"))
print(product("12", 17))
print(product("12", "17"))

print("========== quotient ==========")
print(quotient(12, 17))
print(quotient(12, "17"))
print(quotient("12", 17))
print(quotient("12", "17"))

print("========== floored_quotient ==========")
print(floored_quotient(12, 17))
print(floored_quotient(12, "17"))
print(floored_quotient("12", 17))
print(floored_quotient("12", "17"))

print("========== reminder ==========")
print(reminder(12, 17))
print(reminder(12, "17"))
print(reminder("12", 17))
print(reminder("12", "17"))

print("========== negated ==========")
print(negated(12))
print(negated("-17"))
