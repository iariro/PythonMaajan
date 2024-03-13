
#/**
# * 七対子の待ち判定。
# * @author kumagai
# */
class ChiitoitsuCheck:
	#/**
	# * 七対子の待ち判定。
	# * @param tehai 手牌
	# * @return 待ち牌
	# */
	def getMachi(tehai):
		ret = []

		toitsu = {}

		for i in range(0, len(tehai)):
			if tehai[i].kind not in toitsu:
				# 初めての牌。
				toitsu[tehai[i].kind] = 0
			toitsu[tehai[i].kind] += 1

		if len(toitsu) == 7:
			count = 0

			for pai in toitsu:
				if (toitsu.get(pai) == 2):
					# 対子。
					count += 1

			if (count == 6):
				# 対子は６個。
				for pai in toitsu:
					if (toitsu.get(pai) == 1):
						# 残りの１個。
						ret.append(pai)
		return ret
