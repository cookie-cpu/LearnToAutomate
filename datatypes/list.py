print(list(range(0, 100, 5)))

supplies = ['pen','pencil','stapler','folder']

for i in range(len(supplies)):
  print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

cat = ['small','fluffy','mr whiskers']
size = cat[0]
coat = cat[1]
name = cat[2]

size, color, also_name = cat
print(name)
print(also_name)

