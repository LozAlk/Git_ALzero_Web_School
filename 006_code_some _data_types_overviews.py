# ------------------------------
# type()
# All Data in python is Object
# ------------------------------
#
print(type(10))  # int => Integer
print(type(100))  # int => Integer
print(type(-50))  # # int => Integer

print(type(100.9))  # float =>Floating point number
print(type(1.4060869854))  # float =>Floating point number
print(type(-100.875843579))  # float =>Floating point number


print(type(" hello python"))  # str => String

print(
    type(
        [
            1,
            2,
            3,
            4,
            5,
        ]
    )
)

# list =>List

print(type((1, 2, 3, 4, 5)))  # tuple=> Tuple

print(type({"one": 1, "two": 2, "three": 3}))  # dict => Dictionary

print(type(2 == 2))  # bool => Bollean
