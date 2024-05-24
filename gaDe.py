# DESCRIPTION:
# Introduction
# The GADERYPOLUKI is a simple substitution cypher used in scouting to encrypt messages. The encryption is based on short, easy to remember key. The key is written as paired letters, which are in the cipher simple replacement.

# The most frequently used key is "GA-DE-RY-PO-LU-KI".

#  G => A
#  g => a
#  a => g
#  A => G
#  D => E
#   etc.
def encode(message):
    s1 = "GADERYPOLUKI"
    s2 = "AGEDYROPULIK"
    return message.translate(str.maketrans(s1,s2)).translate(str.maketrans(s1.lower(),s2.lower()))
    
def decode(message):
    return encode(message)



  def basic_test_cases():
        test.assert_equals(encode("ABCD") , "GBCE", "Expected 'GBCE'")
        test.assert_equals(encode("GBCE") , "ABCD", "Expected 'ABCD'")
        test.assert_equals(encode("Gug hgs g cgt") , "Ala has a cat", "Expected 'Ala has a cat'")
        test.assert_equals(decode("agedyropulik") , "gaderypoluki", "Expected 'gaderypoluki'")
        test.assert_equals(decode("Ala has a cat") , "Gug hgs g cgt", "Expected 'Gug hgs g cgt'")
        test.assert_equals(decode("gaderypoluki") , "agedyropulik", "Expected 'agedyropulik'")