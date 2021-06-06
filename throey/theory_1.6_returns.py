def without_input_without_output():
  print("hi")

def without_input_with_output():
  return "output"

def with_input_without_output(input):
  print(input)

def with_input_with_output(input):
  return input


def return_sample():
  print("do something")
  return 10
  print("meaningless print code")

return_sample()

sample_result = return_sample()
print("result 1 :",sample_result)
print("result 2 :",return_sample())