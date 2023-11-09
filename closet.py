

# Simply find the closest value to zero from the list. Notice that there are negatives in the list.

# List is always not empty and contains only integers. Return None if it is not possible to define only one of such values. And of course, we are expecting 0 as closest value to zero.

# Examples:

# [2, 4, -1, -3]  => -1
# [5, 2, -2]      => None
# [5, 2, 2]       => 2
# [13, 0, -6]     => 0


function closest(arr){
  let set = new Set(arr);
  let min = Infinity;
  
  for (let i of set) {
    if (Math.abs(i) < Math.abs(min)) { min = i; }
  }
  
  if (min !== 0 && set.has(min * -1)) { return null; }
  return min;
}