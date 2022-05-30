import re
  

filenames = ["index.html", "tema.xml", 
            "computer.txt", "text.jpg"]
  
for file in filenames:
    match = re.search("\.xml$", file)
  
    if match:
        print("The file ending with .xml is:",file)