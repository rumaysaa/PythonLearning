"""
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
"""

def sentence(phrase):
    interrogatives = ("how","why","what")
    if phrase.startswith(interrogatives):
        return f"{phrase.capitalize()}?"
    else:
        return f"{phrase.capitalize()}."

list = []
while(True):
    inp = input("Say something:")
    if inp == '\end':
        break
    else:
        for_str = sentence(inp)
        list.append(for_str)

string = ' '.join(list)
print(string)

