import sys
import re

pattern = r'(\w)(\1+)'
for line in sys.stdin:
    line = line.rstrip()
    str = re.sub(pattern, r'\1', line)
    print(str)
