from logic.PaiKind import PaiKind

#/**
# * 国士無双判定。
# */
class KokushimusouCheck:
	#/**
	# * 国士無双判定。
	# * @param tehai 手牌
	# * @return 待ち牌
	# */
	def getMachi(tehai):
		yaochuu1 = []
		yaochuu1.append(PaiKind.一萬)
		yaochuu1.append(PaiKind.九萬)
		yaochuu1.append(PaiKind.一筒)
		yaochuu1.append(PaiKind.九筒)
		yaochuu1.append(PaiKind.一索)
		yaochuu1.append(PaiKind.九索)
		yaochuu1.append(PaiKind.東)
		yaochuu1.append(PaiKind.南)
		yaochuu1.append(PaiKind.西)
		yaochuu1.append(PaiKind.北)
		yaochuu1.append(PaiKind.白)
		yaochuu1.append(PaiKind.發)
		yaochuu1.append(PaiKind.中)

		yaochuu2 = yaochuu1[:]

		for i in range(0, len(tehai)):
			if PaiKind(tehai[i].kind) in yaochuu1 and PaiKind(tehai[i].kind) in yaochuu2:
				# 幺九牌である。
				yaochuu2.remove(PaiKind(tehai[i].kind))
			else:
				# 幺九牌ではない。
				return []

		if (len(yaochuu2) == 1):
			# あと１個。
			return yaochuu2
		elif (len(yaochuu2) == 0):
			# 全部ある。
			return yaochuu1
		else:
			# まだ達していない。
			return []
