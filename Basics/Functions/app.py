# Functions

def hello_func():
    print("Hello Function!")

hello_func()

# Function with parameter
def hello_func_with_param(name):
    print("Hello, " + name)

hello_func_with_param("Vladislav")

# Function with return value
def hello_func_with_return(name):
    return "Hello, " + name

print(hello_func_with_return("Vladislav"))

# Function with default parameter
def hello_func_with_default_param(name="Vladislav"):
    return "Hello, " + name

print(hello_func_with_default_param())
print(hello_func_with_default_param("Vlad"))

# Function with multiple parameters
def hello_func_with_multiple_params(name, age):
    return "Hello, " + name + ". You are " + str(age) + " years old."

print(hello_func_with_multiple_params("Vladislav", 15))

# Function with keyword arguments
def hello_func_with_keyword_arguments(name, age):
    return "Hello, " + name + ". You are " + str(age) + " years old."

print(hello_func_with_keyword_arguments(age=15, name="Vladislav"))

# Function with arbitrary arguments
def hello_func_with_arbitrary_arguments(*args):
    return "Hello, " + args[0] + ". You are " + str(args[1]) + " years old."

print(hello_func_with_arbitrary_arguments("Vladislav", 15))

# Function with arbitrary keyword arguments
def hello_func_with_arbitrary_keyword_arguments(**kwargs):
    return "Hello, " + kwargs["name"] + ". You are " + str(kwargs["age"]) + " years old."

print(hello_func_with_arbitrary_keyword_arguments(name="Vladislav", age=15))

# Function with arbitrary arguments and keyword arguments
def hello_func_with_arbitrary_arguments_and_keyword_arguments(*args, **kwargs):
    return "Hello, " + args[0] + ". You are " + str(kwargs["age"]) + " years old."

print(hello_func_with_arbitrary_arguments_and_keyword_arguments("Vladislav", age=15))
