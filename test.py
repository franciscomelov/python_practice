from tabnanny import check


s = "()[]{}"
s = "(]"
s = "()"

values = ["()", "[]", "{}"]

# counter = 0
# for pair in values:
#     if pair[0] in s:
#         check = s.count(pair[0]) == s.count(pair[1])

check = [s.count(pair[0]) == s.count(pair[1]) for pair in values]

print(all(check))

