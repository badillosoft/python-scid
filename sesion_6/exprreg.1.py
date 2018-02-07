import re

pattern = "@(\w{3,})"

text = "[1] oye @juan dice @ana21 que @pp8 quiere comer con @jaz.\n[2] dile a @pp8 que @#! y que voy a ir con @paco por pizza."

for m in re.finditer(pattern, text):
    user = m.group(1)
    i = m.start(1)
    print("{}: {}".format(i, user))