s = raw_input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)

# Other failed approach
# print (input().title())
# 12abcd --> 12Abcd . Therefore, clearly undesirable


