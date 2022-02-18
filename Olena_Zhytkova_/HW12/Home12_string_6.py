import re

pattern_upper=r'([A-Z]+)'
pattern_lower=r'([a-z]+)'
text=input('Enter the text: ')


match_upper=re.search(pattern_upper,text)
match_lower=re.search(pattern_lower,text)

print(f'This text contains Uppercase letters {match_upper[0]} from position {match_upper.start(0)}')
print(f'This text contains Lower letters {match_lower[0]} from position {match_lower.start(0)}')