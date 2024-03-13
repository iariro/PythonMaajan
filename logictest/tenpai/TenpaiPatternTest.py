import datetime
import unittest
from maajanlib.logic.Pai import Pai
from maajanlib.logic.PaiKind import PaiKind
from maajanlib.logic.MachiPattern import MachiPattern
from maajanlib.logic.ChiitoitsuCheck import ChiitoitsuCheck
from maajanlib.logic.KokushimusouCheck  import KokushimusouCheck 

class TenpaiPatternTest(unittest.TestCase):
	def executeTest(self, data, dump=True):
		data1 = [Pai(d) for d in data[0]]
		data2 = data[1][:]

		if dump:
			print(' '.join([PaiKind(p.kind).name for p in data1]))

		time1 = datetime.datetime.now()
		machiPattern = MachiPattern(data1, True)
		machi = machiPattern.getMachi()
		span = datetime.datetime.now() - time1

		if len(machi) > 0:
			print('loopCount={} {}msec'.format(machiPattern.loopCount, span))

			if (dump):
				print('{}待ち'.format(machiPattern.machiElementCollection.toString()))
		else:
			if (len(machi) <= 0):
				# ４面子＋１雀頭ではない。
				machi = ChiitoitsuCheck.getMachi(data1)

			if (len(machi) <= 0):
				# ４面子＋１雀頭・七対子ではない。
				machi = KokushimusouCheck.getMachi(data1)

			if (len(machi) > 0):
				print(' '.join([m.name for m in machi]) + "待ち")
			else:
				print("待ちなし")

		self.assertEqual(len(data2), len(machi))

		for i in range(0, len(data2)):
			self.assertEqual(data2[i], machi[i])

		if type(self).__name__ not in ('TenpaiPatternTestChiitoitsu', 'TenpaiPatternTestKokushimusou'):
			for i in range(0, len(machi)):
				find = False

				for machiElement in machiPattern.machiElementCollection.machi_element_list:
					find |= machi[i] in machiElement.pai_list

				self.assertTrue(find)
