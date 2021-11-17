#given a (the base) n (what we want to mod) and a binary string of the exponent this will 
#find the modularExponentiation of a^(exp) % n as long as the exponent is passed in as a binary string

def modularexpo(a, n, expBinString):
   result = 1
   for i in range (0, len(str(expBinString))):
     if str(expBinString)[i] == '1':
       result = (result ** 2) % n
       result = (result * a) % n
     else:
       result = (result ** 2) % n
   return result
