from .PaiKind import PaiKind
from .MachiType import MachiTypeJp

#/**
# * 待ちの要素情報。
# */
class MachiElement:

	def get(self, i):
		return self.pai_list[i]

	def size(self):
		return len(self.pai_list)

	#/**
	# * オブジェクトを構築。
	# * @param type 待ちの種別
	# * @param use 牌使用フラグ
	# * @param nokori 残り牌
	# * @param pai1 牌１
	# * @param pai2 牌２
	# * @param paiCount 牌カウント
	# */
	def __init__(self, type, use, nokori, pai1=None, pai2=None, pai_count=None):
		self.pai_list = []
		self.type = type
		self.type_jp = MachiTypeJp(int(type))
		self.nokori = nokori

		if pai1 is not None:
			self.pai_list.append(pai1)
		if pai2 is not None:
			self.pai_list.append(pai2)

		if pai1 and PaiKind(pai1) in pai_count:
			# 含まれている。
			self.over1 = pai_count[PaiKind(pai1)] >= 4

		if pai2 and PaiKind(pai2) in pai_count:
			# 含まれている。
			self.over2 = pai_count[PaiKind(pai2)] >= 4

		self.use = use[:]

	#/**
	# * 待ちの要素情報を構築。
	# * @return 文字列化した内容
	# */
	def toString(self):
		return '{}の{}待ち'.format(','.join([PaiKind(p).name for p in self.pai_list]), self.type.name)
