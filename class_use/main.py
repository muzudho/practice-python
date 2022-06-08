class Fruit():
    _name = "fruit1"

    @classmethod
    @property
    def message(clazz):
        return f"this is a {clazz._name}"

    @staticmethod
    def message_s():
        return f"this is a {Fruit._name}"


class Apple(Fruit):
    _name = "apple1"


print(f"Fruit._message   =[{Fruit._name}]")
print(f"Fruit.message    =[{Fruit.message}]")
print(f"Fruit.message_s()=[{Fruit.message_s()}]")
print(f"Apple._message   =[{Apple._name}]")
print(f"Apple.message    =[{Apple.message}]")
print(f"Apple.message_s()=[{Apple.message_s()}]")

"""
Result
------

Fruit._message   =[fruit1]
Fruit.message    =[this is a fruit1]
Fruit.message_s()=[this is a fruit1]
Apple._message   =[apple1]
Apple.message    =[this is a apple1]
Apple.message_s()=[this is a fruit1]
"""
