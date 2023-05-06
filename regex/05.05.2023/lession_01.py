import re

## example 1
print("========== example 1")
# 'r' - raw string
s = r"a\t\tb"
print(s)

## example 2
print("========== example 2")
# re.match ---> match at the beginning of the string
text = "42 is my lucky number"
pattern = r"\d+"
match = re.match(pattern, text)
print('\t', match.group(0), 'at index', match.start())

## example 3
text = "kk is my 56 lucky number"
print("========== example 3")
# re.search ---> search anywhere in the string
match = re.search(pattern, text)
print('\t', match.group(0), 'at index', match.start())

### example 4
text = "42 is my  55 lucky 66 77 number"
print("========== example 4")
# re.findall ---> find all matches
match = re.findall(pattern, text)
for i in match:
    print('\t', "match:", i)

### example 5
# re.finditer ---> find all matches and return an iterator
text = "Ny Postal Codes are 10001, 1002, 10003, 10004"
print("========== example 5")
match_iter = re.finditer(pattern, text)
for i in match_iter:
    print('\t', i.group(0), 'at index', i.start())

### example 6
# re.group ---> return the entire match or specific subgroup
print("========== example 6")
text = "Start Date: 20200920"

pattern = r"(\d{4})(\d{2})(\d{2})"
match = re.search(pattern, text)

if match:
    print('\t', match.group(0), 'at index', match.start())
    print('\t', match.groups())
else:
    print('\t', "no match")


### example 7
# name groups ---> (?P<name>pattern)
print("========== example 7")

text = "Start Date: 20200920"
pattern = r"(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})"

match = re.search(pattern, text)
print('\t', "groups",match.groups())
print('\t','match', match)
print('\t', 'year', match.group('year'))
print('\t', 'month', match.group('month'))
print('\t', 'day', match.group('day'))