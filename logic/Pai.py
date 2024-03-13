
#**
#* 牌オブジェクト。
#* @author kumagai
#*/
class Pai:
	kind = 0
	akadora = False

	#**
	#* 牌情報を構築。
	#* @param kind 牌種別
	#*/
	def __init__(self, kind):
		self.kind = kind
		self.akadora = False

	#**
	#* 数牌であるかを取得。
	#* @return true=数牌である／false=数牌ではない
	#*/
	def isShuupai(self):
		return self.kind <= 26

	#**
	#* 字牌であるかを取得。
	#* @return true=字牌である／false=字牌ではない
	#*/
	def isJihai(self):
		return self.kind >= 27

	#**
	#* 中張牌であるかを取得。
	#* @return true=中張牌である／false=中張牌ではない
	#* @throws Exception
	#*/
	def isChunchanpai(self):
		if (self.isShuupai()):
			# 数牌である。

			return self.getNumber() >= 2 and self.getNumber() <= 8
		else:
			# 数牌ではない。

			return False

	#**
	#* 数牌１・７であるかを取得。
	#* @return true=数牌１・７である／false=数牌１・７ではない
	#* @throws Exception
	#*/
	def isChantaShuntsuAtama(self):
		if (self.isShuupai()):
			# 数牌である。

			return self.getNumber() == 1 or self.getNumber() == 7
		else:
			# 数牌ではない。

			raise Exception("数牌ではありません。")

	#**
	#* 幺九牌であるかを取得。
	#* @return true=幺九牌である／false=幺九牌ではない
	#*/
	def isYaochuupai(self):
		if (self.isShuupai()):
			# 数牌である。

			return self.kind ==  0 or \
				   self.kind ==  9 or \
				   self.kind == 18 or \
				   self.kind ==  8 or \
				   self.kind == 17 or \
				   self.kind == 26
		else:
			# 字牌である。

			return True

	#**
	#* 風牌であるかを取得。
	#* @return true=風牌である／false=風牌ではない
	#*/
	def isKazehai(self):
		return self.kind >= 27 and self.kind <= 30

	#**
	#* 三元牌であるかを取得。
	#* @return true=三元牌である／false=三元牌ではない
	#*/
	def isSangenpai(self):
		return self.kind >= 31

	#**
	#* 老頭牌であるかを取得。
	#* @return true=老頭牌である／false=老頭牌ではない
	#*/
	def isRaotoupai(self):
		if (self.isShuupai()):
			# 数牌である。

			return self.kind ==  0 or \
				   self.kind ==  9 or \
				   self.kind == 18 or \
				   self.kind ==  8 or \
				   self.kind == 17 or \
				   self.kind == 26
		else:
			# 字牌である。

			return False

	#**
	#* 数牌の数を１～９で取得。
	#* @return 数牌の数
	#* @throws Exception
	#*/
	def getNumber(self):
		if (self.isShuupai()):
			# 数牌である。

			return self.kind % 9 + 1
		else:
			# 字牌である。

			raise Exception("数牌ではありません。")

	#**
	#* 数牌の１を取得。
	#* @return 数牌の１
	#* @throws Exception
	#*/
	def getIchi(self):
		if (self.isShuupai()):
			# 数牌である。

			return self.kind - self.kind % 9
		else:
			# 字牌である。

			raise Exception("数牌ではありません。")

	#**
	#* 次の色の同じ数字かを判定。
	#* @param pai 牌
	#* @return true=次の色の同じ数字
	#*/
	def isSameNumberInNextColor(self, pai):
		if (self.kind <= 17):
			# 一萬～九筒である。

			return self.kind + 9 == pai.kind
		else:
			# 一索以降である。

			return False

	#**
	#* 順子であるかを判定。
	#* @param pai1 牌１
	#* @param pai2 牌２
	#* @return true=順子である／false=順子ではない
	#*/
	def isShuntsu(self, pai1, pai2):
		return self.kind + 1 == pai1.kind and pai1.kind + 1 == pai2.kind

	#**
	#* 同じ色の数牌かを判定。
	#* @param pai 比較対象
	#* @return true=同じ色／false=同じ色ではない
	#*/
	def isSameColor(self, pai):
		if (self.isShuupai()):
			# 数牌である。

			return self.kind // 9 == pai.kind // 9
		else:
			# 数牌ではない。

			raise Exception("数牌ではありません")

	#**
	#* 比較。
	#* @param obj 比較対象
	#* @return 1/0/-1/
	#*/
	def compareTo(self, pai):
		if (self.kind > pai.kind):
			# 大きい。

			return 1
		elif (self.kind < pai.kind):
			# 小さい。

			return -1
		else:
			# 同じ。

			return 0

	#**
	#* 内容を比較。
	#* @param pai 比較対象
	#* @return true=同じ／false=異なる
	#*/
	def equals2(self, pai):
		return self.kind == pai.kind

	#**
	#* ハッシュコード取得。
	#* @return ハッシュコード
	#*/
	def getHashCode(self):
		return 0

	#**
	#* ドラ牌取得。
	#* @return ドラ牌
	#*/
	def getDora(self):
		if (self.isShuupai()):
			# 数牌。

			return Pai(self.kind - (self.kind % 9) + (self.kind + 1) % 9)
		elif (iself.sKazehai()):
			# 風牌。

			return Pai(27 + (self.kind + 1 - 27) % 4)
		else:
			# 三元牌。

			return Pai(31 + (self.kind + 1 - 31) % 3)
