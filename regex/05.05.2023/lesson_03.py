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
text_sample_3 = "The line 01\nThe line 02\nThe three"



# ANCHOR

# \b - Word boundary
print("========== example 1", "Word boundary")
pattern = r"\b\w{3}\b"
pattern2 = r"(?m)(?i)\bthe\b"
regex_findall(pattern2, text_sample_3)

# $ - End of string
print("========== example 2", "End of string")
pattern = r"(?m)\d{2}$"
regex_findall(pattern, text_sample_3)

# character classes - \d, \w, \s
print("========== example 3", "character classes")
pattern_d = r"\d"
pattern_s = r"\s"
regex_findall(pattern_d, text_sample_3)
regex_findall(pattern_s, text_sample_3)
