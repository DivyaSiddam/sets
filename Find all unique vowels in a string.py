s = "hello universe"
vowels = set("aeiou")
found = set()

for char in s:
    if char in vowels:
        found.add(char)

print("Unique vowels:", found)
