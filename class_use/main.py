class Fruit():
    message = "this is a fruit"


class Apple(Fruit):
    message = "this is an apple"


print(f"Fruit.message=[{Fruit.message}]")
print(f"Apple.message=[{Apple.message}]")
