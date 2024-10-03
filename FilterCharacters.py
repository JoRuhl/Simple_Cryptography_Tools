#This code solves rail fence type ciphers where lines have been intercalated. Enter the
#enciphered string as your encodedstring, and the readout will separate alternating characters to something readable. The second half of the code enciphers using
#the same method. Enter your plaintext as the plainstring and the output will be the enciphered text. This can be used as an in-house verification check. 
#Sample strings have been entered, run the module to see outputs.


encodedstring="fno.rw imkoirpee doina .roarigl/ wfieknic/eR aciilp_hfeernsc:eh_tctippsh:e/re"
newstring=""

for i in range(len(encodedstring)):
  if i%2 ==0:
    newstring+= encodedstring[i]
for j in range(len(encodedstring)):
  if j%2!=0:
    newstring+= encodedstring[j]
print(newstring)

plainstring= "for more on rail fence ciphers:https://en.wikipedia.org/wiki/Rail_fence_cipher"

if len(plainstring)//2 == 0:
    toprail = plainstring[:len(plainstring)//2]
    bottomrail = plainstring[len(plainstring)//2:]
else:    
    toprail = plainstring[:len(plainstring)//2 +1]
    bottomrail = plainstring[len(plainstring)//2+1:]

encipheredstring = ""

for i in range(len(bottomrail)):
    encipheredstring += toprail[i] + bottomrail[i]
if len(plainstring)//2!=0:
    encipheredstring+= toprail[-1]

print(encipheredstring)
