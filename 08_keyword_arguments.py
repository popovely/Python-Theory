def minus(a, b):
    return a - b


result = minus(b=30, a=1)
print(result)


def say_hello(name, age, are_from, fav_food):
    return f"Hello {name}! You were born in {are_from} and you are {age} years old. You like {fav_food}"


hello = say_hello(name="popo", age="5", are_from="korea", fav_food="snack")
print(hello)
