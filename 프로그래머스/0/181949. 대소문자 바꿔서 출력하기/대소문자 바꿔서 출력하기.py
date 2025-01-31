str = input()
result = ""
for text in str:
    if text.islower():
        result += text.upper()
    else:
        result += text.lower()

print(result)