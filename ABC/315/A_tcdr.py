
EXCLUDE = ["a", "e", "i", "o", "u"]
S = input()

ans = ""
for c in S:
    if c in EXCLUDE:
        continue
    ans += c
print(ans)
