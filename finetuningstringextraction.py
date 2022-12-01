import re 
x= 'From stephen.marquard@uct.ac.za Sat 5 9:14:16 2008'
y=re.findall ('\S+@\S+',x)
print(y)

import re 
x= 'From stephen.marquard@uct.ac.za Sat 5 9:14:16 2008'
y=re.findall('^From (\S+@\S+)',x)
print(y)