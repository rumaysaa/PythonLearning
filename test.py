
def mean(value):
    if (type(value) == dict):
        mean = (sum(value.values())) / (len(value))
    else:
        mean = sum(value) / len(value)
    return mean
list = [45,23,65]
d = {"a":24,"b":11,"c":66}

print(mean(list))
print(mean(d))



