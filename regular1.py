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

# Flags: re.I,re.M, re.X
match_5 = re.search(r"bc", "AABC", flags=re.IGNORECASE)

# Replace a string using a re.sub
string_6 = "Working with python is great.Python is great."
match_6 = re.sub(r'python','JavaScript', string_6, flags=re.IGNORECASE)
print(match_6)

#  Workig with groups
match_7 = re.sub(r't([0-9])([0-9])',r't\2\1',"t10 t43 t56")
print(match_7)

# Replacing using functions
items = ['zero', 'one', 'two']
match_8 = re.sub(r"a\[([0-3])\]", lambda match: items[int(match.group(1))], "Items: a[0], a[1] and a[2]")
print(match_8)


match_9 = re.sub(r"([abc])", lambda string: string.group(1).upper(), "abc, kabc")
print(match_9)

# Non overlapping matches: findall or finditer
results = re.finditer(r"t([0-9]{0,3})", "t10 t43 t56")
print([result.group(1) for result in results])

# Checking allowed characters
def is_allowed(string):
    results = re.search(r"[^0-9a-zA-Z]", string)
    return not bool(results)

print(is_allowed("09Homeishome"))

# Split a string according to character match
new_string = re.split(r",", "David, Njeri")
print(new_string)

# Named Grouping
my_name = re.search(r"My name is (?P<name>[a-zA-Z].+)", "My name is Daudi Njeri")
print(my_name.groups())

# Non capturring groups (?:)
match_10 = re.match(r"(\d+)(\+(\d+))?", "22+33")
match_non_group = re.match(r"(\d+)(?:\+(\d+))?", "22+33")
print(match_10.groups())
print(match_non_group.groups())

#Escapaing special characters
special_match = re.search(r"(\[abc\])", "12[abc]45")
special_match2 = re.search(re.escape(r"[abc]"),"12[abc]45")
print(special_match.group())
print(special_match2.group())

# Matching regex on specific locations in string
import regex as re
rx = re.compile(r"""
    \([^()]*\)(*SKIP)(*FAIL)
    | "David"
    """, re.VERBOSE)
string_name = "My name is David (I am David)"
name = rx.findall()
print(name)
