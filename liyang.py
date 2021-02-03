import re
line = 'this hdr-biz modhdrel server'
patt = r'hdr'
patten = re.compile(patt)
m = patten.findall(line)
print(len(m))