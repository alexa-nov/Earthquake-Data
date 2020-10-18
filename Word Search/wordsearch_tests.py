import unittest
from wordsearch_funcs import *

class TestCases(unittest.TestCase):

#Convert input string into list of strings
    def test_format_words_1(self):
        words_str = "UNIX CALPOLY GCC SLO CPE COMPILE VIM TEST"
        self.assertEqual(format_words(words_str), ['UNIX', 'CALPOLY', 'GCC', 'SLO', 'CPE', 'COMPILE', 'VIM', 'TEST'])

    def test_format_words_2(self):
        words_str = "CHICKEN DOG CAT BEAR RABBIT ZEBRA MOUSE RACCOON"
        self.assertEqual(format_words(words_str), ['CHICKEN', 'DOG', 'CAT', 'BEAR', 'RABBIT', 'ZEBRA', 'MOUSE', 'RACCOON'])

#Convert puzzle into list of strings by row
    def test_format_rows_1(self):
        puzzle_str = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
        self.assertEqual(format_rows(puzzle_str), ['WAQHGTTWEE', 'CBMIVQQELS', 'APXWKWIIIL', 'LDELFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU'])

    def test_format_rows_2(self):
        puzzle_str = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        self.assertEqual(format_rows(puzzle_str), ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR'])

#Convert puzzle into list of strings by reverse row
    def test_format_rev_rows_1(self):
        puzzle_str = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
        self.assertEqual(format_rev_rows(puzzle_str), ['EEWTTGHQAW', 'SLEQQVIMBC', 'LIIIWKWXPA', 'VPIPXFLEDL', 'NMAVMTDNOP', 'BOGQYOSDEO', 'TCMMGKCQGL', 'MZUCAOLSCY', 'ZYCXSGMDVX', 'UNFXINUIUU'])

    def test_format_rev_rows_2(self):
        puzzle_str = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        self.assertEqual(format_rev_rows(puzzle_str), ['BAINRBRAOE', 'HBRBEARBEZ', 'RNOOCCARRA', 'CEHCRRBCAA', 'AKBOZOBANC', 'ACNBBRINOB', 'AIARBCTREE', 'RHRCIRECBA', 'OCCROROIOB', 'RAEKRKAAOB'])

#Converts puzzle into list of strings by column
    def test_format_col_1(self):
        puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'APXWKWIIIL', 'LDELFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
        self.assertEqual(format_col(puzzle), ['WCALPOLYXU', 'ABPDOEGCVU', 'QMXENDQSDI', 'HIWLDSCLMU', 'GVKFTOKOGN', 'TQWXMYGASI', 'TQIPVQMCXX', 'WEIIAGMUCF', 'ELIPMOCZYN', 'ESLVNBTMZU'])

    def test_format_col_2(self):
        puzzle = ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR']
        self.assertEqual(format_col(puzzle), ['EZAACBEABB', 'OERANOEBOO', 'ABRCANRCIA', 'RRABBITEOA', 'BACRORCRRK', 'RECRZBBIOR', 'NBOCOBRCRK', 'IROHBNARCE', 'ABNEKCIHCA', 'BHRCAAAROR'])

#Converts puzzle into list of strings by reverse column
    def test_format_rev_col_1(self):
        puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'APXWKWIIIL', 'LDELFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
        self.assertEqual(format_rev_col(puzzle), ['UXYLOPLACW', 'UVCGEODPBA', 'IDSQDNEXMQ', 'UMLCSDLWIH', 'NGOKOTFKVG', 'ISAGYMXWQT', 'XXCMQVPIQT', 'FCUMGAIIEW', 'NYZCOMPILE', 'UZMTBNVLSE'])

    def test_format_rev_col_2(self):
        puzzle = ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR']
        self.assertEqual(format_rev_col(puzzle), ['BBAEBCAAZE', 'OOBEONAREO', 'AICRNACRBA', 'AOETIBBARR', 'KRRCRORCAB', 'ROIBBZRCER', 'KRCRBOCOBN', 'ECRANBHORI', 'ACHICKENBA', 'RORAAACRHB'])

#Converts puzzle into list of strings by diagonal rows
    def test_format_diagonal_1(self):
        puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'APXWKWIIIL', 'LDELFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
        self.assertEqual(format_diagonal(puzzle), ['WBXLTYMUYU', 'CPEDOGCCN', 'ADNSKAXF', 'LODCOSX', 'PEQLGI', 'OGSMN', 'LCDU', 'YVI', 'XU', 'U', 'AMWFMQMZZ', 'QIKXVGCM', 'HVWPAOT', 'GQIIMB', 'TQIPN', 'TEIV', 'WLL', 'ES', 'E'])

    def test_format_diagonal_1(self):
        puzzle = ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR']
        self.assertEqual(format_diagonal(puzzle), ['EERBOBRRCR', 'ZRCBRBCCA', 'AAAICIRE', 'ANNTROK', 'CORERR', 'BECOK', 'EBIA', 'AOA', 'BO', 'B', 'OBARZBAHO', 'ARCRONIR', 'RACCBCA', 'BEOHKA', 'RBOEA', 'NRNC', 'IBR', 'AH', 'B'])


#Checks Forward
    def test_forward_1(self):
        puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'APXWKWIIIL', 'LDELFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
        words = ['UNIX', 'CALPOLY', 'GCC', 'SLO', 'CPE', 'COMPILE', 'VIM', 'TEST']
        self.assertEqual(forward(puzzle,words), [['UNIX', '(FORWARD)', 9, 3], ['SLO', '(FORWARD)', 7, 2]])

    def test_forward_2(self):
        puzzle = ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR']
        words = ['CHICKEN', 'DOG', 'CAT', 'BEAR', 'RABBIT', 'ZEBRA', 'MOUSE', 'RACCOON']
        self.assertEqual(forward(puzzle,words), [['ZEBRA', '(FORWARD)', 1, 0], ['RACCOON', '(FORWARD)', 2, 2]])

#Checks Backward
    def test_backward_1(self):
        puzzle_str = "WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
        words = ['UNIX', 'CALPOLY', 'GCC', 'SLO', 'CPE', 'COMPILE', 'VIM', 'TEST']
        self.assertEqual(backward(puzzle_str,words), [['VIM', '(BACKWARD)', 1, 4]])
    
    def test_backward_2(self):
        puzzle_str = "EOARBRNIABZEBRAEBRBHARRACCOONRAACBRRCHECCNABOZOBKABONIRBBNCAEERTCBRAIAABCERICRHRBOIORORCCOBOAAKRKEAR"
        words = ['CHICKEN', 'DOG', 'CAT', 'BEAR', 'RABBIT', 'ZEBRA', 'MOUSE', 'RACCOON']
        self.assertEqual(backward(puzzle_str,words), [['BEAR', '(BACKWARD)', 1, 6]])

#Checks Upward
    def test_upward_1(self):
        puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'APXWKWIIIL', 'LDELFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
        words = ['UNIX', 'CALPOLY', 'GCC', 'SLO', 'CPE', 'COMPILE', 'VIM', 'TEST']
        self.assertEqual(upward(puzzle,words), [['COMPILE', '(UP)', 6, 8]])

    def test_upward_2(self):
        puzzle = ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR']
        words = ['CHICKEN', 'DOG', 'CAT', 'BEAR', 'RABBIT', 'ZEBRA', 'MOUSE', 'RACCOON']
        self.assertEqual(upward(puzzle,words), [['CHICKEN', '(UP)', 8, 8]])

#Checks Downward
    def test_downward_1(self):
        puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'APXWKWIIIL', 'LDELFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
        words = ['UNIX', 'CALPOLY', 'GCC', 'SLO', 'CPE', 'COMPILE', 'VIM', 'TEST']
        self.assertEqual(downward(puzzle,words), [['CALPOLY', '(DOWN)', 1, 0]])

    def test_downward_2(self):
        puzzle = ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR']
        words = ['CHICKEN', 'DOG', 'CAT', 'BEAR', 'RABBIT', 'ZEBRA', 'MOUSE', 'RACCOON']
        self.assertEqual(downward(puzzle,words), [['RABBIT', '(DOWN)', 1, 3]])

#Checks Diagonal
    def test_diagonal_1(self):
        puzzle = ['WAQHGTTWEE', 'CBMIVQQELS', 'APXWKWIIIL', 'LDELFXPIPV', 'PONDTMVAMN', 'OEDSOYQGOB', 'LGQCKGMMCT', 'YCSLOACUZM', 'XVDMGSXCYZ', 'UUIUNIXFNU']
        words = ['UNIX', 'CALPOLY', 'GCC', 'SLO', 'CPE', 'COMPILE', 'VIM', 'TEST', 'SMN', 'PAOT', 'LL']
        self.assertEqual(diagonal(puzzle,words), [['GCC', '(DIAGONAL)', 6, 5], ['CPE', '(DIAGONAL)', 1, 0], ['SMN', '(DIAGONAL)', 7, 2], ['PAOT', '(DIAGONAL)', 3, 6], ['LL', '(DIAGONAL)', 1, 8]])

    def test_diagonal_2(self):
        puzzle = ['EOARBRNIAB', 'ZEBRAEBRBH', 'ARRACCOONR', 'AACBRRCHEC', 'CNABOZOBKA', 'BONIRBBNCA', 'EERTCBRAIA', 'ABCERICRHR', 'BOIORORCCO', 'BOAAKRKEAR']
        words = ['CHICKEN', 'DOG', 'CAT', 'BEAR', 'RABBIT', 'ZEBRA', 'MOUSE', 'RACCOON']
        self.assertEqual(diagonal(puzzle,words), [])


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
