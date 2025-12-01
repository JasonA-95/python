name = "Alan Turing"
age = 42
age_type = type(age)
print(age_type)
job = "mathematician"
person = {
    "name": "Alan Turing",
    "age": 42,
    "job": "mathematician"
}
text = "Hello. My name is {}, i am {} and i am {}.".format(person["name"], person["age"], person["job"])
print(text)

