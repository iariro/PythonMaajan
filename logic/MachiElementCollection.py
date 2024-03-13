from .PaiKind import PaiKind

#/**
# * 待ち要素情報のコレクション。
# */
class MachiElementCollection:
	machi_element_list = None

	def __init__(self):
		self.machi_element_list = []

	def get(self, i):
		return self.machi_element_list[i]

	def size(self):
		return len(self.machi_element_list)

	#/**
	# * 待ち要素情報を追加。重複追加チェック付き。
	# * @param machi 待ち要素情報
	# */
	def addElement(self, machi):
		find = False

		i = 0
		while i < self.size() and find == False:
			if (self.get(i).type == machi.type and self.get(i).size() == machi.size()):
				# 待ちのタイプ・個数ともに同じである。

				equal = True

				j = 0
				while j < self.get(i).size() and equal:
					equal &= self.get(i).get(j) == machi.get(j)
					j += 1

				find = equal
			i += 1

		if find == False:
			# 一致するものはなかった。

			self.machi_element_list.append(machi)

	#/**
	# * 内容比較。
	# * @param machiElementCollection 比較対象
	# * @return true=一致／false=不一致
	# */
	def equals2(self, machiElementCollection):
		equal = True

		if (self.size() == machiElementCollection.size()):
			# 待ち要素数は同じ。

			for i in range(0, self.size()):
				j = 0
				while j < machiElementCollection.size() and equal:
					if (self.get(i).type == machiElementCollection.get(j).type):
						# 待ちのタイプは同じ。

						if (self.get(i).size() == machiElementCollection.get(j).size()):
							# 要素内の牌の数は同じ。

							k = 0
							while k < self.get(i).size() and equal:
								equal = self.get(i).get(k) == machiElementCollection.get(j).get(k)
								k += 1
					j += 1
		else:
			# 待ち要素数は異なる。

			equal = False

		return equal

	#/**
	# * 内容文字列化。
	# * @return 内容文字列
	# */
	def toString(self):
		builder = ''

		for i in range(0, self.size()):
			if (i > 0):
				# 区切りを入れる箇所である。
				builder += "／"

			builder += '{}：{}'.format(self.machi_element_list[i].type.name, ' '.join([PaiKind(pl).name for pl in self.machi_element_list[i].pai_list]))

		return builder
