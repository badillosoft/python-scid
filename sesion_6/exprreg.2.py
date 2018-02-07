import re

pattern = "\w+"

text = "[1] oye @juan dice @ana21 que @pp8 quiere comer con @jaz.\n[2] dile a @pp8 que @#! y que voy a ir con @paco por pizza."

for m in re.finditer(pattern, text):
    word = m.group(0)
    i = m.start(0)
    print("{}: {}".format(i, word))