# Sexy primes are pairs of two primes that are 6 apart. In this kata, your job is to complete the function which returns true if x & y are sexy, false otherwise.

# Examples
# 5, 11   -->  true
# 61, 67  -->  true
# 7, 13   -->  true
# 5, 7    -->  false
# 1, 7    -->  false  (1 is not a prime)
# Note: x & y are always positive integers, but they are not always in order of precendence... For example you can be given either (5, 11) or (11, 5) - both are valid.


function sexy_prime(x, y){
  for (var i=2; i<x; ++i)
    if (x%i==0)
      return false;
  for (var i=2; i<y; ++i)
    if (y%i==0)
      return false;    
  if (y==1 ||x==1)
    return false;
  return Math.abs(x-y)==6
}