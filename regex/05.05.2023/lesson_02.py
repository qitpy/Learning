import re

# regex finding
def regex_search(pattern, text):
    match = re.search(pattern, text)
    print('result', match.group()) if match else print("no search found")

def regex_match(pattern, text):
    match = re.match(pattern, text)
    print('result', match.group()) if match else print("no match")

def regex_findall(pattern, text):
    match = re.findall(pattern, text)
    print('result', match) if match else print("no match")


text_sample_1 = "This a sample text with some number 12345. 33, 55 and some special characters !@#$%^&*()_+ and .some. other. number like 1234567890 44- 90"
text_sample_2 = "VanQuyet1999"
text_sample_3 = "The line 01\nThe line 02"

print("========== example 1", "Flag: i")
# Flag: (?i)
pattern = r"(?i)A\w{2}"
regex_findall(pattern, text_sample_1)

# Conditional regex
print("========== example 2", "Conditional regex")
pattern = r"b\w{1}|i\w{1}|g\w{1}"
regex_findall(pattern, text_sample_1)

# Square brackets - Character set
print("========== example 3", "Square brackets")
pattern = r"[big]\w{1}"
regex_findall(pattern, text_sample_1)

# Caret symbol - Negation
# The caret symbol (^) is used to check if a string NOT starts with a certain character.
# The caret is need to be the first character in the square brackets.
print("========== example 4", "Caret symbol")
pattern = r"[^big]\w{1}"
text = "MynameisJohgnbKei"
regex_findall(pattern, text)

# hyphen symbol - Range
# The hyphen symbol (-) is used to check if a string contains a range of characters.
print("========== example 5", "hyphen symbol")
pattern = r"[b-dx-z2-4]"
regex_findall(pattern, text_sample_1)

# Wildcard dot symbol - Any character
# The dot symbol (.) is used to check if a string contains any character. except new line
print("========== example 6", "dot symbol")
pattern = r"."
regex_findall(pattern, text_sample_2)
# incase want to specify dot symbol (\.)
pattern = r"\."
regex_findall(pattern, text_sample_1)

pattern = r"[.]"
regex_findall(pattern, text_sample_1)

# cautious symbol - (?s)
print("========== example 7", "new line symbol")
pattern = r"(?s)."
regex_findall(pattern, text_sample_3)

# \n - new line
print("========== example 8", "new line symbol")
pattern = r"\n"
regex_findall(pattern, text_sample_3)