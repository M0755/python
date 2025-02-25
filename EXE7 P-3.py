names=set()
names.update(["mahir","mayan","jainil","diyan"])
print(names)
if "mahir" in names:
    names.remove("mahir")
    names.add("mahir mankad")

print(names)
names.discard("mahir mankad")
names.discard("jainil")

print(names)
