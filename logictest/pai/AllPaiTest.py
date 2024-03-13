import unittest
from logic.AllPai import AllPai

class AllPaiTest(unittest.TestCase):
    def testAllPai(self):
        allPai = AllPai(True)
        self.assertEqual(136, allPai.size())

    def testGetRandom1(self):
        allPai = AllPai(True)

        for pai in allPai.pai_list:
            print('{} '.format(pai.kind), end='')
        print("")

        self.assertEqual(136, allPai.size())

        paiNumTable = {}

        for p in allPai.pai_list:
            if p.kind not in paiNumTable:
                paiNumTable[p.kind] = 0
            paiNumTable[p.kind] += 1

        for i in range(0, 34):
            self.assertEqual(4, paiNumTable.get(i))
