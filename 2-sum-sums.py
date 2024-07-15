# sum is a common task to find the pair of integers in the array such that their sum equals to the target.

# array
# target = 7

# Pair is (2, 5)
# Task
# There is an array of unique integers.

# The task is to find the sum of all targets in the specific range [from, to), which has a pair in the array, such that sum of the pair equals to the target.

# Example
# Array = [2, 4, 6, 10], target range is [6, 10)

# target = 6  =>  (2, 4)
# target = 7  =>  no pair
# target = 8  =>  (2, 6)
# target = 9  =>  no pair

# So the result is: 6 + 8 = 14
# Notes
# Both elements of the pair must be unique
# Each target will be counted once, even though there may exist multiple pairs which add up to it
# Your solution will be tested for performance

using System.Collections.Generic;
using System.Linq;
  
public class TwoSum
{
  public int SumOfTwoSumTargets (int[] numbers, int from, int to) 
  {
    var set = new HashSet<int>();
    
    for (var i = 0; i < numbers.Length; i++)
    {
      for (var j = i + 1; j < numbers.Length; j++)
      {
        var s = numbers[i] + numbers[j];
        if (s >= from && s < to) set.Add(s);
      }
    }
    
    return set.Sum();
  }
}

# seconde solution
namespace SumSumTask
{
  using System;
  using System.Linq;
  
  public class TwoSum
  {
    public int SumOfTwoSumTargets (int[] numbers, int min, int max)
    {
      var sum = numbers.Where(x => x < max).SelectMany((x, i) => numbers[(i + 1)..], (x, y) => x + y);
      return Enumerable.Range(min, max - min).Intersect(sum).Sum();
    }
  }
}

namespace SumSumTask {
  using NUnit.Framework;
  using System;
  
  [TestFixture]
  public class AccountTest
  {
    [Test]
    public void ValueTest1()
    {
      TwoSum t = new TwoSum();
      var res = t.SumOfTwoSumTargets(new []{1,2}, 3, 4);
      Assert.AreEqual(3, res);
    }
  }
}
