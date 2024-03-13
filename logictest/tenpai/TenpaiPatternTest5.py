from maajanlib.logictest.tenpai import TenpaiPatternTest, TenpaiData5

class TenpaiPatternTest5(TenpaiPatternTest.TenpaiPatternTest):
	def test501五面待ち暗刻ノベタン(self):
		self.executeTest(TenpaiData5.data501)

	def test502五面待ち２暗刻単騎(self):
		self.executeTest(TenpaiData5.data501)

	def test503五面待ち煙突(self):
		self.executeTest(TenpaiData5.data501)

	def test504五面待ち２煙突(self):
		self.executeTest(TenpaiData5.data501)

	def test505五面待ち一盃口ノベタン(self):
		self.executeTest(TenpaiData5.data501)

	def test506五面待ち４枚使い1(self):
		self.executeTest(TenpaiData5.data501)

	def test507五面待ち４枚使い2(self):
		self.executeTest(TenpaiData5.data501)

	def test508五面待ち４枚使い3(self):
		self.executeTest(TenpaiData5.data501)

	def test509五面待ち煙突５連続対子(self):
		self.executeTest(TenpaiData5.data501)

	def test510五面待ち一盃口(self):
		self.executeTest(TenpaiData5.data501)
