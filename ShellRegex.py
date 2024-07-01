
import re

d = "4223 pts/0 00:00:03 emacs"
m = ("pts??s+?", "[es]+", "s.+s+", "[emacs]+", "emacs*?", "0+0?")
print (d)
for item in m:
    print(item + " : " + re.search(item, d).group())

