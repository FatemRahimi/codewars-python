# DESCRIPTION:
# You're playing to scrabble. But counting points is hard.

# You decide to create a little script to calculate the best possible value.

# The function takes two arguments :

# `points` : an array of integer representing for each letters from A to Z the points that it pays
# `words` : an array of strings, uppercase

# You must return the index of the shortest word which realize the highest score.
# If the length and the score are the same for two elements, return the index of the first one.


from string import ascii_uppercase as uppercase

def get_best_word(points, words):
    points = dict(zip(uppercase, points))
    
    score = lambda word: sum(points[c] for c in word)
    
    return words.index(sorted(sorted(words, key=len), key=score, reverse=True)[0])


points = (1,3,3,2,1,4,2,4,1,8,10,1,2,1,1,3,8,1,1,1,1,4,10,10,10,10)
import codewars_test as test
from solution import get_best_word

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(get_best_word(points, ["WHO","IS","THE","BEST","OF","US"]), 0)
        test.assert_equals(get_best_word(points, ["AABCDEF", "WHO","IS","THE","BEST","OF","US"]), 1)
        test.assert_equals(get_best_word(points, ["NOQ","TXAY","S","OM","ESFT","CJUKQ","QL","QO","ASTK","Y"]), 5)
        test.assert_equals(get_best_word(points, ["N","AO","TQGZW","P","OBTP","CLWXB","Y","JQGFJ","Q","RP","OC","MRQCZ","ZWN","ZRT","OIRYH","GWPMSZP","LQRYUKQ","LBM","LFEI","VHUX","RTALLIC","JEMUPS","XUW","X","ZLXFMWS","LFAGR","HJ","RTUAI","JRBNG","ZUYSC","CIEYV","FUY","B","EJS","CINBTQS","JEAC","JX","LLILSEK","W","KLUV"]), 16)
        test.assert_equals(get_best_word(points, ["SVWLIDP","FCPKTHW","EREMN","NFEF","PQ","FSC","ZYPOSXJ","BOR","YCGG","RC","DVPE","VAOE","OIGK","OTQE","REJFUFD","FVBCSSB","VHJ","BEC","MWZQ","WX","L","ZPCB","JKLHE","RYFTY","NKP","ID","O","KA","VRXX","NTDB","OERKPC","YFLUI","SKQCJ","PXDSW","ITYWD","TC","LOIDQEJ","NE","YND","VJHOCEC","RPRANZ","BQ","STM","RGVBFW","SMWUYLW","KT","SXHY","XCE","T","SC","UDJU","CHDR","UGXNQ","CQOOBA","O","NWW","V","L","BAQ","AZN","LBTR","N","QSURR","KADPH","M","LCBEAKM","ZHEVXS","F","TVAIQCY","MF","KCI","YQ","RCG","AKYPCP","WJXG","RQXOI","SJI","TWXZ","J","HIKCGHV","EAAXGG","AETSH","EO","BUET","TDIQCO","TKL","FJCRY","ZHAJLK","OLMCVA","F"]), 6)
        test.assert_equals(get_best_word(points, ["RBBL","ZJ","ZOFXE","LMBFCFX","O","JG","SYRYE","VXG","EU","DAIFZR","BQUNZHH","WKO","TFPHPLX","SWLG","CY","JYQNDSM","ITPS","B","UVSDMWR","LCPS"]), 15)
        test.assert_equals(get_best_word(points, ['LGVMJDW', 'HSPASA', 'CFHMVZNGH', 'ESKSKB', 'JDO', 'BQJUECZ', 'BB', 'IVVLXBC', 'ZRENSWMG']), 5)