# ANS.  8.
import math


def Operations(Value):

    Logarithmic = math.log(Value)

    exponential = math.exp(Value)

    Power_function = math.pow(Value, 2)

    Square_root = math.sqrt(Value)

    return {
        "Logarithmic": Logarithmic,
        "Exponential": exponential,
        "Power_function": Power_function,
        "Square_root": Square_root,
    }


Result = Operations(49)
print(Result)


# ANS.  9.
def fun(name):
    x = name.split()
    first_name = x[0]
    last_name = x[1]

    return {"first_name": first_name, "last_name": last_name}


Name = fun("Ashish Das")
print(Name)
