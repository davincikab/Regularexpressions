import re

pattern = r"123"
string = "123Kenya"

# Matching at the start of string
match = re.match(pattern, string)
# print(match.group())

# Match the regex anywhere in the string
pattern_2 = r"Kenya"
string_2 = "Welcome to Kenya. It is Kenya"

match_2 = re.search(pattern_2,string_2)
print(match_2.group(0))

# Using search to specify begining of a string: retunr the first matched instance
pattern_3 = r"^Kenya"
string_3 = "Kenya ni yetu"
match_3 =  re.search(pattern_3,string_2)
print(match_3)

#Using findall: returns an list of match
match_4 = re.findall(pattern_2,string_2)
print(match_4)

# Working with pre compiled patterns
string_5 = "Welcome to 1942"
ppatern = re.compile(r"(.*\d+)")
matches = ppatern.search(string_5)
print(matches.group(0))
print(matches.group(1))
