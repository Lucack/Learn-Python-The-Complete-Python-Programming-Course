string = "Ubiquitous"
print(string[0:10])
print(string[3:0])
print(string[0:4])
print(string[3:5])

import re
print(dir(re))  # all functions by module re

string = "The night was cold and dark and there are no one there"
m = re.search("night",string)
print(m) #<re.Match object; span=(4, 9), match='night'>

st = m.start()
end = st + 5

print(st) #4
print(end) #5
print(string[st:end]) # night

str = "sadiogjas#od56$ghna14sCheese2544bw56yw4238vc7ht834Cake984u3yPizza"

position = re.search("Cheese",str)
print(position.start())
print(position.end())
print(str[position.start():position.end()])