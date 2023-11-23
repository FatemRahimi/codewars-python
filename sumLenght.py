# In this kata you must return a string value, where the first part is the sum of positive numbers and the second part is the number of negative numbers.
# Knowing that the first '0' is negative, the second is positive, the third is negative, and so on...


# For example :
# sumLength([-1,2,3,4,0,1,0,-2,0,-3])
# return '10 5' (10 = 1 + 2 + 3 + 4 and 5 = 3 + 2 => 3 negatives numbers + second 0 as negative)

function sumLength (arr) {
  const sum = arr.filter((x, i) => x > 0).reduce((a, b) => a + b, 0);
  let z = 0;
  const len = arr.filter((x, i) => x < 0 || (x == 0 && (z++) % 2 == 0)).length;
  return `${sum} ${len}`
}