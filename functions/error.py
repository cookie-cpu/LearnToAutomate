def div42by(db):
  try:
    return 42 / db
  except ZeroDivisionError:
    print("Error: you tried to divide by zero")

print(div42by(2))
print(div42by(12))
print(div42by(0)) # divide by zero error
print(div42by(1))