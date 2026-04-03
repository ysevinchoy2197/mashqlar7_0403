#6-misol
roy = [12, 5, 7, 20, 3, 15]
print(roy)

sonlar = list(filter(lambda el: el > 5, roy))
print(sonlar)

#7-misol
roy =  [12, 5, 7, 20, 3, 15]
print(roy)
sonlar = list(filter(lambda el: el < 10, roy))
print(sonlar)

#8-misol
roy = [3, 5, 9, 10, 12, 14]
print(roy)
sonlar = list(filter(lambda el: el % 3 == 0, roy))
print(sonlar)

#9-misol
roy = [6, 8, 12, 15, 18, 20]
print(roy)
sonlar = list(filter(lambda el: el % 2 == 0 and el % 3 == 0, roy))
print(sonlar)

#10-misol
roy = [0, 1, 2, 0, 3, 0, 4]
print(roy)
sonlar = list(filter(lambda el: el != 0, roy))
print(sonlar)
