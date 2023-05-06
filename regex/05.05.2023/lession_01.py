import datetime
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
# while use finditer, we can use start() and end() to get the index of the match
text = "Ny Postal Codes are 10001, 1002, 10003, 10004"
print("========== example 5")
match_iter = re.finditer(pattern, text)
for i in match_iter:
    print('\t', i.group(), 'at index', i.start())

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

### example 8
# re.find and replace and sub
# note: sub(pr1, pr2, pr3):
## --> pr1: pattern
## --> pr2: replacement pattern / methods
## --> pr3: text
print("========== example 8")

text = "Start Date: 20200920, End Date: 20200921"
pattern = r"(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})"
replacement_pattern = r"\g<month>-\g<day>-\g<year>"
new_text = re.sub(pattern, replacement_pattern, text)
print('\t', 'new text:', new_text)

### example 9
# re.groupdict ---> return a dictionary of named groups
print("========== example 9")
text = "Start Date: 20200920, End Date: 20200921"
pattern = r"(?P<year>\d{4})(?P<month>\d{2})(?P<day>\d{2})"
match = re.search(pattern, text)

year, month, day = int(match.group('year')), int(match.group('month')), int(match.group('day'))

print('\t', 'match.groupdict():', match.groupdict())
print('\t', 'match.groups():', match.groups())
print('\t', 'match.group()', match.group())
print('\t', 'match.group(year)', match.group('year'))
print('\t', 'match', match)
print('\t', 'prettier', datetime.date(year, month, day).strftime('%b-%d-%Y'))


# example 10
# re.split ---> split a string by a pattern
# note: split(pattern, text)

pattern = r","
text = "a,b,c,d,e,f,g,h,i,j,k,l,m"

print('\t', "split", re.split(pattern, text))