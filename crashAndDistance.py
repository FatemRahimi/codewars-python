# Kata

# Home
# Report home for your next assignment
# TRAINING
# Practice
# Complete challenging Kata to earn honor and ranks. Re-train to hone technique
# Freestyle Sparring
# Take turns remixing and refactoring others code through Kumite
# COMMUNITY
# Leaderboards
# Achieve honor and move up the global leaderboards
# Chat
# Join our Discord server and chat with your fellow code warriors
# Discussions
# View our Github Discussions board to discuss general Codewars topics
# ABOUT
# Docs
# Learn about all of the different aspects of Codewars
# FatemRahimi Avatar
# 5 kyu
# 444
# 7 kyu
# We've crashed on a distance planet in our galaxy! When do leap years occur here?
# 8593% of 148425 of 864cave.on
# JavaScript
# TRAINNEXT KATA
# Details
# Solutions
# Forks (3)
# Discourse (24)
# Collect|
# DESCRIPTION:
# Our spaceship has crashed on an unknown planet many light years away from earth. Thankfully we were able to send out a distress signal right before the crash. Help will be here shortly but we need to gather as much information about this planet as we can before we're rescued.

# Before our control panels were destroyed, we were able to gather the duration of this planet's orbit around it's planetary system's star.

# Among other things, we need to determine if a given year is a leap year on this planet.

# Your Task:

# Given the duration of the planet's orbit (in days) and a specific year on this planet, determine if the given year is a leap year here.

# For example:

# On Earth, a single rotation around the sun takes 365.25 days. Therefore, each year takes 365 days but every forth year is a leap year and takes 366 days. The next leap year on Earth will occur in 2020.

# Notes: To make things easier, the period of the leap years will always be a power of 2. Good luck!

# PUZZLES
# SIMILAR KATA:
# 7 kyu
# Leap Years
# 2096690% of 2,26528,455BattleRattle1 Issue Reported
# 6 kyu
# Leap year (with restrictions)
# 9590% of 84234suic
# 8 kyu
# Cat years, Dog years
# 71614492% of 4,72652,252dinglemouse
# 7 kyu
# Cat Years, Dog Years (2)
# 802390% of 6402,552dinglemouse
# MORE BY AUTHOR:
# Check out these other kata created by cave.on

# 5 kyu
# Ratio of Bouncy Numbers
# 19493% of 63204cave.on
# 5 kyu
# Integer Right Triangles
# 31795% of 49149cave.on
# STATS:
# Created	May 10, 2018
# Published	May 10, 2018
# Warriors Trained	1944
# Total Skips	32
# Total Code Submissions	2328
# Total Times Completed	864
# JavaScript Completions	425
# Python Completions	401
# C Completions	82
# Total Stars	8
# % of votes with a positive feedback rating	93% of 148
# Total "Very Satisfied" Votes	128
# Total "Somewhat Satisfied" Votes	18
# Total "Not Satisfied" Votes	2
# Total Rank Assessments	9
# Average Assessed Rank	
# 7 kyu
# Highest Assessed Rank	
# 7 kyu
# Lowest Assessed Rank	
# 8 kyu
# Ad
# Fulfil your AI needs with Nvidia Tesla v100 (16GB) & v100s (32GB) GPUs
# Ads via Carbon
# CONTRIBUTORS
# cave.on Avatar
# myjinxin2015 Avatar
# Blind4Basics Avatar
# rowcased Avatar
# FArekkusu Avatar
# hobovsky Avatar
# dfhwze Avatar
# Ad
# Developer Productivity: A guide to finding flow
# Find out to harness your flow for more higher productivity.
# © 2023 CodewarsAboutAPIBlogPrivacyTermsCode of ConductContact
function isLeapYear(d, y) {
  return d*y%1===0;
}
test
const Test = require('@codewars/test-compat');

describe("Basic Tests", function(){
  it("should return if the given year is a leap year", function() {
    Test.assertEquals(isLeapYear(365.25, 2018), false, '2018 is not a leap year on Earth');
    Test.assertEquals(isLeapYear(365.25, 2020), true,  '2020 is a leap year on Earth');
    Test.assertEquals(isLeapYear(124.5,   102), true,  '102 is a leap year on Earth');
    Test.assertEquals(isLeapYear(124.125, 102), false, '102.125 is a leap year on Earth');
  });
});



