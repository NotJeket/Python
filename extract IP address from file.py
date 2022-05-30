import re
  
# tine Txt-ul aproape de script.
with open('test2.txt') as fh:
  string = fh.readlines()
    
pattern =re.compile('''((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)
{3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)''')
  

valid =[]
invalid=[]
  

for line in string:
    line = line.rstrip()
    result = pattern.search(line)
  
    
    if result:
      valid.append(line)
  
     
    else:
      invalid.append(line)
  

print("Valid IPs")
print(valid)
print("Invalid IPs")
print(invalid)