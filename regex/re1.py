import re

pattern = re.compile('search')
string = "search this inside this text please!"


a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match( string )
print(d)