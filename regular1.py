import re

pattern = r"123"
string = "123Kenya"

# Matching at the start of string
match = re.match(pattern, string)
print(match.group())

# Match the regex anywhere in the string
pattern_2 = r"Kenya"
string_2 = "Welcome to Kenya. It is Kenya"
match2 = re.search(pattern_2,string_2)
print(match2.group())