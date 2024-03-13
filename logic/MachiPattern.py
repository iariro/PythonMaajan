from .AllPai import AllPai
from .MachiElement import MachiElement
from .MachiElementCollection import MachiElementCollection
from .MachiType import MachiType
from .MentsuPattern import MentsuPattern

#/**
# * 待ちパターン。
# * @author kumagai
# */
class MachiPattern(MentsuPattern):
	# boolean all;

	paiCount = None
	JudgeCount = 0
	machi = None
	machiElementCollection = None

	#/**
	# * 待ち牌のコレクションを構築する。
	# * @param tehai 手牌
	# * @param all true=すべて検索／false=初めの１個のみ検索する
	# */
	def __init__(self, tehai, all):

		self.machiElementCollection = MachiElementCollection()

		self.all = all
		self.machi = [False] * AllPai.totalPaiNum
		self.paiCount = {} # 牌の数をカウント。

		for i in range(0, len(tehai)):
			if (tehai[i].kind not in self.paiCount):
				# 初めての牌。
				self.paiCount[tehai[i].kind] = 0
			self.paiCount[tehai[i].kind] += 1

		self.makeMentsu0(tehai, all)

	#/**
	# * @see kumagai.Maajan.logic.MentsuPattern#onFind3Mentsu(java.util.ArrayList, int[])
	# */
	def onFind3Mentsu(self, tehai, use):
		self.JudgeCount += 1

		nokori = []

		for i in range(0, len(tehai)):
			if (use[i] <= 0):
				# 面子確定してない牌である。
				nokori.append(tehai[i])

		if (len(nokori) == 4):
			# 残り４枚。

			dec = False
			inc = False

			if (nokori[0].equals2(nokori[1]) and nokori[1].equals2(nokori[2]) and nokori[2].kind + 1 == nokori[3].kind):
				# 2223 == 22 + (1+)23(+4)
				# 1112 == 111 + 2(+2) == 11 + 12 (+3)
				# 8889 == 888 + 9(+9) == 88 + (7+)89

				if (nokori[3].isShuupai() and nokori[2].isSameColor(nokori[3])):
					# 同じ柄の数牌である。

					# 端の牌ではない。
					dec = nokori[2].isChunchanpai()

					# 端の牌ではない。
					inc = nokori[3].isChunchanpai()

					self.machi[nokori[3].kind] = True
					self.machiElementCollection.addElement(MachiElement(MachiType.Tanki, use, nokori, pai1=nokori[3].kind, pai_count=self.paiCount))

					if (dec and inc):
						# 両面待ち。

						self.machi[nokori[2].kind - 1] = True
						self.machi[nokori[3].kind + 1] = True
						self.machiElementCollection.addElement(MachiElement(MachiType.Ryanmen, use, nokori, pai1=nokori[2].kind - 1, pai2=nokori[3].kind + 1, pai_count=self.paiCount))

					elif (dec):
						# 辺張待ち。

						self.machi[nokori[2].kind - 1] = True
						self.machiElementCollection.addElement(MachiElement(MachiType.Penchan, use, nokori, pai1=nokori[2].kind - 1, pai_count=self.paiCount))

					elif (inc):
						# 辺張待ち。

						self.machi[nokori[3].kind + 1] = True
						self.machiElementCollection.addElement(MachiElement(MachiType.Penchan, use, nokori, pai1=nokori[3].kind + 1, pai_count=self.paiCount))

			elif (nokori[0].kind + 1 == nokori[1].kind and nokori[1].kind == nokori[2].kind and nokori[2].kind == nokori[3].kind):
				# 2333 == (1+)23(+4) + 33
				# 1222 == (1+)1 + 222
				# 1222 == 12(+3) + 22
				# 8999 == (7+)89 + 99

				if (nokori[1].isShuupai() and nokori[0].isSameColor(nokori[1])):
					# 同じ柄の数牌である。

					# 端の牌ではない。
					dec = nokori[0].isChunchanpai()

					# 端の牌ではない。
					inc = nokori[1].isChunchanpai()

					self.machi[nokori[0].kind] = True
					self.machiElementCollection.addElement(MachiElement(MachiType.Tanki, use, nokori, pai1=nokori[0].kind, pai_count=self.paiCount))

					if (dec and inc):
						# 両面待ち。

						self.machi[nokori[0].kind - 1] = True
						self.machi[nokori[1].kind + 1] = True
						self.machiElementCollection.addElement(MachiElement(MachiType.Ryanmen, use, nokori, pai1=nokori[0].kind - 1, pai2=nokori[1].kind + 1, pai_count=self.paiCount))

					elif (dec):
						# 辺張待ち。

						self.machi[nokori[0].kind - 1] = True
						self.machiElementCollection.addElement(MachiElement(MachiType.Penchan, use, nokori, pai1=nokori[0].kind - 1, pai_count=self.paiCount))

					elif (inc):
						# 辺張待ち。

						self.machi[nokori[1].kind + 1] = True
						self.machiElementCollection.addElement(MachiElement(MachiType.Penchan, use, nokori, pai1=nokori[1].kind + 1, pai_count=self.paiCount))

			elif (nokori[0].kind + 2 == nokori[1].kind and nokori[1].kind == nokori[2].kind and nokori[2].kind == nokori[3].kind):
				# 1333 == 1(+1) + 333 == 1(+2+)3 + 33

				if (nokori[1].isShuupai() and nokori[0].isSameColor(nokori[1])):
					# 同じ柄の数牌である。

					self.machi[nokori[0].kind] = True
					self.machi[nokori[0].kind + 1] = True

					self.machiElementCollection.addElement(MachiElement(MachiType.Tanki, use, nokori, pai1=nokori[0].kind, pai_count=self.paiCount))
					self.machiElementCollection.addElement(MachiElement(MachiType.Kanchan, use, nokori, pai1=nokori[0].kind + 1, pai_count=self.paiCount))

			elif (nokori[0].kind == nokori[1].kind and nokori[1].kind == nokori[2].kind and nokori[2].kind + 2 == nokori[3].kind):
				# 1113 == 111 + 3(+3) == 11 + 1(+2+)3

				if (nokori[1].isShuupai() and nokori[2].isSameColor(nokori[3])):
					# 同じ柄の数牌である。

					self.machi[nokori[3].kind] = True
					self.machi[nokori[2].kind + 1] = True
					self.machiElementCollection.addElement(MachiElement(MachiType.Tanki, use, nokori, pai1=nokori[3].kind, pai_count=self.paiCount))
					self.machiElementCollection.addElement(MachiElement(MachiType.Kanchan, use, nokori, pai1=nokori[2].kind + 1, pai_count=self.paiCount))

			elif (nokori[0].kind + 1 == nokori[1].kind and nokori[1].kind == nokori[2].kind and nokori[2].kind + 1 == nokori[3].kind):
				# 1223

				if (nokori[3].isShuupai() and nokori[0].isSameColor(nokori[3])):
					# 同じ柄の数牌である。

					self.machi[nokori[2].kind] = True
					self.machiElementCollection.addElement(MachiElement(MachiType.Tanki, use, nokori, pai1=nokori[2].kind, pai_count=self.paiCount))

			elif (nokori[0].kind + 1 == nokori[1].kind and nokori[1].kind + 1 == nokori[2].kind and nokori[2].kind + 1 == nokori[3].kind):
				# 1234

				if (nokori[3].isShuupai() and nokori[0].isSameColor(nokori[3])):
					# 同じ柄の数牌である。

					self.machi[nokori[0].kind] = True
					self.machi[nokori[3].kind] = True
					self.machiElementCollection.addElement(MachiElement(MachiType.Tanki, use, nokori, pai1=nokori[0].kind, pai_count=self.paiCount))
					self.machiElementCollection.addElement(MachiElement(MachiType.Tanki, use, nokori, pai1=nokori[3].kind, pai_count=self.paiCount))

			elif (nokori[0].kind == nokori[1].kind and nokori[1].kind == nokori[2].kind and nokori[2].kind != nokori[3].kind):
				# 1119

				self.machi[nokori[3].kind] = True
				self.machiElementCollection.addElement(MachiElement(MachiType.Tanki, use, nokori, pai1=nokori[3].kind, pai_count=self.paiCount))

			elif (nokori[0].kind != nokori[1].kind and nokori[1].kind == nokori[2].kind and nokori[2].kind == nokori[3].kind):
				# 1999

				self.machi[nokori[0].kind] = True
				self.machiElementCollection.addElement(MachiElement(MachiType.Tanki, use, nokori, pai1=nokori[0].kind, pai_count=self.paiCount))

			elif (nokori[0].kind + 2 == nokori[1].kind and nokori[2].kind == nokori[3].kind):
				# 1399

				if (nokori[1].isShuupai() and nokori[0].isSameColor(nokori[1])):
					# 同じ柄の数牌である。

					self.machi[nokori[0].kind + 1] = True
					self.machiElementCollection.addElement(MachiElement(MachiType.Kanchan, use, nokori, pai1=nokori[0].kind + 1, pai_count=self.paiCount))

			elif (nokori[0].kind == nokori[1].kind and nokori[2].kind + 2 == nokori[3].kind):
				# 9913 == 99 + 1(+2+)3

				if (nokori[3].isShuupai() and nokori[2].isSameColor(nokori[3])):
					# 同じ柄の数牌である。

					self.machi[nokori[2].kind + 1] = True
					self.machiElementCollection.addElement(MachiElement(MachiType.Kanchan, use, nokori, pai1=nokori[2].kind + 1, pai_count=self.paiCount))

			elif (nokori[0].kind + 1 == nokori[1].kind and nokori[2].kind == nokori[3].kind):
				# 2399

				if (nokori[1].isShuupai() and nokori[0].isSameColor(nokori[1])):
					# 端の牌ではない。
					dec = nokori[0].isChunchanpai()

					# 端の牌ではない。
					inc = nokori[1].isChunchanpai()

					if (dec and inc):
						# 両面待ち。

						self.machi[nokori[0].kind - 1] = True
						self.machi[nokori[1].kind + 1] = True
						self.machiElementCollection.addElement(MachiElement(MachiType.Ryanmen, use, nokori, pai1=nokori[0].kind - 1, pai2=nokori[1].kind + 1, pai_count=self.paiCount))

					elif (dec):
						# 辺張待ち。

						self.machi[nokori[0].kind - 1] = True
						self.machiElementCollection.addElement(MachiElement(MachiType.Penchan, use, nokori, pai1=nokori[0].kind - 1, pai_count=self.paiCount))

					elif (inc):
						# 辺張待ち。

						self.machi[nokori[1].kind + 1] = True
						self.machiElementCollection.addElement(MachiElement(MachiType.Penchan, use, nokori, pai1=nokori[1].kind + 1, pai_count=self.paiCount))

			elif (nokori[0].kind == nokori[1].kind and nokori[2].kind + 1 == nokori[3].kind):
				# 9923

				if (nokori[3].isShuupai() and nokori[2].isSameColor(nokori[3])):
					# 同じ柄の数牌である。

					# 端の牌ではない。
					dec = nokori[2].isChunchanpai()

					# 端の牌ではない。
					inc = nokori[3].isChunchanpai()

					if (dec and inc):
						# 両面待ち。

						self.machi[nokori[2].kind - 1] = True
						self.machi[nokori[3].kind + 1] = True
						self.machiElementCollection.addElement(MachiElement(MachiType.Ryanmen, use, nokori, pai1=nokori[2].kind - 1, pai2=nokori[3].kind + 1, pai_count=self.paiCount))

					elif (dec):
						# 辺張待ち。

						self.machi[nokori[2].kind - 1] = True
						self.machiElementCollection.addElement(MachiElement(MachiType.Penchan, use, nokori, pai1=nokori[2].kind - 1, pai_count=self.paiCount))

					elif (inc):
						# 辺張待ち。

						self.machi[nokori[3].kind + 1] = True
						self.machiElementCollection.addElement(MachiElement(MachiType.Penchan, use, nokori, pai1=nokori[3].kind + 1, pai_count=self.paiCount))

			elif (nokori[0].kind + 1 == nokori[1].kind and nokori[1].kind + 1 == nokori[2].kind and nokori[2].kind != nokori[3].kind):
				# 1239

				if (nokori[2].isShuupai() and nokori[0].isSameColor(nokori[2])):
					# 同じ柄の数牌である。

					self.machi[nokori[3].kind] = True
					self.machiElementCollection.addElement(MachiElement(MachiType.Tanki, use, nokori, pai1=nokori[3].kind, pai_count=self.paiCount))

			elif (nokori[1].kind + 1 == nokori[2].kind and nokori[2].kind + 1 == nokori[3].kind):
				# 9123

				if (nokori[3].isShuupai() and nokori[1].isSameColor(nokori[3])):
					# 同じ柄の数牌である。

					self.machi[nokori[0].kind] = True
					self.machiElementCollection.addElement(MachiElement(MachiType.Tanki, use, nokori, pai1=nokori[0].kind, pai_count=self.paiCount))

			elif (nokori[0].kind == nokori[1].kind and nokori[1].kind != nokori[2].kind and nokori[2].kind == nokori[3].kind):
				# 1199

				self.machi[nokori[0].kind] = True
				self.machi[nokori[2].kind] = True
				self.machiElementCollection.addElement(MachiElement(MachiType.Shanpon, use, nokori, pai1=nokori[0].kind, pai2=nokori[2].kind, pai_count=self.paiCount))

		if (all):
			# すべて見つける。

			return True
		else:
			# １つでも見つければ終了とする。

			for i in range(0, len(self.machi)):
				if (self.machi[i]):
					# 見つけた。

					return False

			return True

	#/**
	# * 待ち牌取得。
	# * @return 待ち牌
	# */
	def getMachi(self):
		machi = []

		for i in range(0, len(self.machi)):
			if (self.machi[i]):
				# 待ちである。

				if i in self.paiCount:
					# 含まれている。

					if (self.paiCount.get(i) < 4):
						# ４枚使われていない。
						machi.append(i)
				else:
					# 含まれていない。
					machi.append(i)

		return machi
