import re

#Aci iti pui linkul
s = "https://arrkeurope.jobbase.io/job/zk32awlnc9ifyfxr9x8a7wv3krgvzyo"

obj1 = re.findall("(\w+)://", s)

print(obj1)

#din cauza linku-lui special trebuia modificat www. cu arrkeurope
obj2 = re.findall("://arrkeurope.([\w\-\.]+)",s)

print(obj2)