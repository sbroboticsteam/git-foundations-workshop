def conflictTestFunction(param):
  num = 0
  num += 10
  param = num
  print("Value: " + str(num))
  return param
