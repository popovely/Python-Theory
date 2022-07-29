# tuple : []로 감싸는 list의 형태에서 ()로 감싸기만 하면 tuple이다.
days = ("Mon", "Tue", "Wed", "Thur", "Fri")

# dictionary : 공통된 사항에 대해 관련 정보를 묶어놓은 것. key와 value로 이루어져 있다. {}로 감싼다.
popo = {
    "name": "Popo Lee",
    "age": 5,
    "dog": True,
    "fav_food": ["meat", "snack"]
}

print(popo)
print(popo["fav_food"])
popo["cute"] = True
print(popo)