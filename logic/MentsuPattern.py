
#/**
# * 面子パターン。
# * @author kumagai
# */
class MentsuPattern:
	skip = False
	loop = True
	loopCount = 0

	#/**
	# * 面子検索。
	# * @param tehai 手牌
	# * @param skip true=枝切りする／false=しない
	# */
	def makeMentsu0(self, tehai, skip):
		self.skip = skip

		use1 = [0] * len(tehai)
		use2 = [0] * len(tehai)

		self.makeMentsu(tehai, use1, use2, [], 0, 1, 0)

	#/**
	# * ３面子確定時イベント。
	# * @param tehai 手牌
	# * @param use 牌確定フラグ
	# * @return true=継続／false=検索処理打ち切り
	# * @throws Exception
	# */
	def onFind3Mentsu(self, tehai, use):
		print(tehai, use)

	#/**
	# * 再帰的に面子を検索する。
	# * @param tehai 手牌
	# * @param use1 チェック配列
	# * @param use2 面子確定配列
	# * @param mentsu 面子候補インデックス配列
	# * @param mentsuCount 確定した面子の数
	# * @param level 再帰呼び出しの深さ
	# * @param start チェック開始インデックス
	# */
	def makeMentsu(self, tehai, use1, use2, mentsu, mentsuCount, level, start):
		self.loopCount += 1

		if (level >= len(tehai)):
			# すべての牌を使用した。

			return

		if (level == len(tehai) - 3 * 1 + 1):
			# １３枚の場合level=11、１４枚の場合level=12。

			if ((13 - len(tehai)) / 3 + mentsuCount < 3):
				# まだ２面子しか確定していない。

				return
		elif (level == len(tehai) - 3 * 2 + 1):
			# １３枚の場合level=8、１４枚の場合level=9。

			if ((13 - len(tehai)) / 3 + mentsuCount < 2):
				# まだ１面子しか確定していない。

				return
		elif (level == len(tehai) - 3 * 3 + 1):
			# １３枚の場合level=5、１４枚の場合level=8。

			if ((13 - len(tehai)) / 3 + mentsuCount < 1):
				# まだ１面子も確定していない。

				return

		mentsu2 = None
		ppai = -1

		i = start
		while i < len(use1) and self.loop:
			if (use1[i] == 0 and (self.skip == False or tehai[i].kind != ppai)):
				# まだ使われていない。

				if len(mentsu) == 0:
					# １個目。

					use1[i] = level
					mentsu.append(i)
					self.makeMentsu(tehai, use1, use2, mentsu, mentsuCount, level + 1, i + 1)
					del mentsu[len(mentsu) - 1]
					use1[i] = 0
				elif (len(mentsu) == 1):
					# ２個目。

					use1[i] = level

					if (tehai[mentsu[0]].kind == tehai[i].kind or (tehai[i].kind < 26 and tehai[mentsu[0]].kind + 1 == tehai[i].kind)):
						# 対子または搭子。

						mentsu.append(i)
						self.makeMentsu(tehai, use1, use2, mentsu, mentsuCount, level + 1, i + 1)
						del mentsu[len(mentsu) - 1]

					use1[i] = 0
				elif (len(mentsu) == 2):
					# ３個目。

					kakutei = False

					if (tehai[mentsu[0]].kind == tehai[mentsu[1]].kind and tehai[mentsu[1]].kind == tehai[i].kind):
						# 刻子。

						kakutei = True
					elif (tehai[i].isShuupai() and tehai[mentsu[0]].kind + 1 == tehai[mentsu[1]].kind and tehai[mentsu[1]].kind + 1 == tehai[i].kind):
						# 順子。

						if (tehai[mentsu[0]].isSameColor(tehai[i])):
							# 同じ柄。

							kakutei = True

					if (self.skip):
						# 間引きOn。

						if (kakutei):
							# 面子確定。

							j=i+1
							while j<len(use1) and kakutei:
								if (use1[j] > 0):
									# その面子よりも右側ですでに面子が確定して
									# いる。

									kakutei = False
								j += 1

						if (kakutei):
							# 面子確定。

							if (mentsu2 != None):
								# すでに確定した別の面子がある。

								if (mentsu2.contains(mentsu.get(0)) or mentsu2.contains(mentsu.get(1)) or mentsu2.contains(i)):
									# すでに使われている。

									kakutei = False

					use1[i] = level

					if (kakutei):
						# 面子確定。

						mentsu.append(i)
						mentsu2 = mentsu[:]

						# ３面子以内である。
						# 「2223」を「3」単騎待ちとせず「22 + (1+)23(+4)」とす
						# るために確定は３面子以内に収めることとしている。

						use2[mentsu[0]] = level - 2
						use2[mentsu[1]] = level - 1
						use2[mentsu[2]] = level

						if ((13 - len(tehai)) / 3 + mentsuCount < 2):
							# ２面子以内である。

							self.makeMentsu(tehai, use1, use2, [], mentsuCount + 1, level + 1, 0)
						else:
							# ３面子を越えた。

							self.loop = self.onFind3Mentsu(tehai, use2)

						use2[mentsu[0]] = 0
						use2[mentsu[1]] = 0
						use2[mentsu[2]] = 0

						del mentsu[len(mentsu) - 1]

					use1[i] = 0

				ppai = tehai[i].kind
			i += 1
