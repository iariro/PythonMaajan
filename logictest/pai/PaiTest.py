import unittest
from logic.Pai import Pai

class PaiTest(unittest.TestCase):
	def test01Shuupai(self):
		self.assertTrue(Pai(0).isShuupai())
		self.assertTrue(Pai(11).isShuupai())
		self.assertTrue(Pai(26).isShuupai())
		self.assertFalse(Pai(31).isShuupai())

	def test2Jihai(self):
		self.assertFalse(Pai(0).isJihai())
		self.assertFalse(Pai(11).isJihai())
		self.assertFalse(Pai(26).isJihai())
		self.assertTrue(Pai(31).isJihai())

	def test3Chunchanpai(self):
		self.assertFalse(Pai(0).isChunchanpai())
		self.assertTrue(Pai(11).isChunchanpai())
		self.assertFalse(Pai(26).isChunchanpai())
		self.assertFalse(Pai(31).isChunchanpai())

	def test4Yaochuupai(self):
		self.assertTrue(Pai(0).isYaochuupai())
		self.assertFalse(Pai(11).isYaochuupai())
		self.assertTrue(Pai(26).isYaochuupai())
		self.assertTrue(Pai(31).isYaochuupai())

	def test5Number(self):
		self.assertEqual(1, Pai(0).getNumber())
		self.assertEqual(3, Pai(11).getNumber())
		self.assertEqual(9, Pai(26).getNumber())

	def test6Number(self):
		try:
			Pai(31).getNumber()

			self.fail()
		except:
			pass

	def test7IsSameNumberInNextColor(self):
		self.assertTrue(Pai(2).isSameNumberInNextColor(Pai(11)))
		self.assertFalse(Pai(2).isSameNumberInNextColor(Pai(12)))
		self.assertFalse(Pai(2).isSameNumberInNextColor(Pai(20)))

		self.assertTrue(Pai(11).isSameNumberInNextColor(Pai(20)))

	def test8IsSameColor(self):
		self.assertTrue(Pai(2).isSameColor(Pai(8)))
		self.assertFalse(Pai(2).isSameColor(Pai(11)))
