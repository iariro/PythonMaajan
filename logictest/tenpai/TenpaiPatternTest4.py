from maajanlib.logictest.tenpai import TenpaiPatternTest, TenpaiData4

class TenpaiPatternTest4(TenpaiPatternTest.TenpaiPatternTest):
	def test401四面待ち三面張単騎複合(self):
		self.executeTest(TenpaiData4.data401)

	def test402四面待ち二筋両面待ち(self):
		self.executeTest(TenpaiData4.data402)

	def test403四面待ち一盃口形(self):
		self.executeTest(TenpaiData4.data403)

	def test404四面待ち４枚使い1(self):
		self.executeTest(TenpaiData4.data404)

	def test405四面待ち４枚使い2(self):
		self.executeTest(TenpaiData4.data405)

	def test406四面待ち２暗刻単騎(self):
		self.executeTest(TenpaiData4.data406)

	def test407四面待ち１０枚1(self):
		self.executeTest(TenpaiData4.data407)

	def test408四面待ち１０枚2(self):
		self.executeTest(TenpaiData4.data408)

	def test409四面待ち１０枚3(self):
		self.executeTest(TenpaiData4.data409)

	def test410四面待ち１０枚4(self):
		self.executeTest(TenpaiData4.data410)

	def test411四面待ち１０枚5(self):
		self.executeTest(TenpaiData4.data411)

	def test412四面待ち１３枚1(self):
		self.executeTest(TenpaiData4.data412)

	def test413四面待ち１３枚2(self):
		self.executeTest(TenpaiData4.data413)
