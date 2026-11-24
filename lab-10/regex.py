import re

# 10.2
txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR."
print("or")
print(re.findall("or", txt))

# 10.2.1
print(".")
print(re.findall(".", txt))
print("or.")
print(re.findall("or.", txt))

print(r"..\.")
print(re.findall(r"..\.", txt))

# 10.2.2
print("Hello\nWorld")
print(r"Hello\nWorld")

# 10.2.3
print(re.findall(r"\w", txt))
print(re.findall(r"\W", txt))

print(re.findall(r"\d", txt))
print(re.findall(r"\D", txt))

print(re.findall(r"\s", txt))
print(re.findall(r"\S", txt))

# 10.2.4
print(re.findall(r"[bcdfghjklmnpqrstvxz]", txt))

print(re.findall(r"[^aeiouy]", txt))

print(re.findall(r"[0-9a-f]", txt))

# 10.3
print(re.findall(r"\d+", txt))
print(re.findall(r"\w+", txt))
print(re.findall(r"\w*or\w+", txt))

# 10.3.1
print(re.findall(r"\w*\d", "abc123def456ghi"))
print(re.findall(r"\w*?\d", "abc123def456ghi"))

# 10.3.2
mtxt = "jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com."

print(re.findall(r"\w+@\w+", mtxt))
print(re.findall(r"\w+(?:\.\w+)*@\w+(?:\.\w+)+", mtxt))
print(re.findall(r"(?:^|[^@\w.])(\w+(?:\.\w+)*@\w+(?:\.\w+)+)(?![@\w.])", mtxt))

# 10.4
htmltxt = """
bla bla bla
<h1> My Rubric      </h1>
bla bla bla.
"""

print(re.findall(r"<h1>\s*.*\s*</h1>", htmltxt))
print(re.findall(r"<h1>\s*(.*)\s*</h1>", htmltxt))
print(re.findall(r"<h1>\s*(.*?)\s*</h1>", htmltxt))