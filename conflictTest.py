def conflictTestFunction(param):
  num = param
  num += 10
  param = num
  print("Value: " + str(num))
  return param
