
import string

import secrets

Import random

lttr = string.ascii_letters

dgts = string.digits

spcl = string.punctuation

slst = lttr + dgts + spcl

pslen = 10

while True:
  
pswrd = ''

for i in range(pslen):
  
pa += ''.join(secrets.choice(slst))

if (any(char in spcl for char in pswrd) and 
    
sum(char in dgts for char in pswrd)>=2):
  
Break 

print(pswrd)
