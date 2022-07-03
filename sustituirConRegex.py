import re

mystr = 'hello world!'
dict_replace = {'hello': 'hi', 'world': 'python', '!': '.'}

regex = re.sub('|'.join(dict_replace.keys()), lambda match: dict_replace[match.string[match.start():match.end()]],mystr)

print(mystr)
print(dict_replace.keys())
print(dict_replace.values())
print(regex)