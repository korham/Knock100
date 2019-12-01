import re

pattern = r"(?P<posinega>[\+\-])(?P<hour>\d{2})(?P<minute>\d{2})"

input = "Sun 10 May 2015 13:54:36 +0700"
m = re.search(pattern, input)
print(m.group("posinega"))
print(m.group("hour"))
print(m.group("minute"))
