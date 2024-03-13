import random

from logic.Pai import Pai
from logic.PaiAndRandomValue import PaiAndRandomValue

#/**
# * 全牌のコレクション。
# * @author kumagai
# */
class AllPai:
    totalPaiNum = (9 * 3 + 4 + 3) * 4
    tsumoIndex = 14
    rinshanIndex = 0

    #/**
    # * 全牌のコレクションを構築。
    # * @param randomize true=ランダム化＝洗牌する／false=しない
    # */
    def __init__(self, randomize):

        self.pai_list = []
        self.construct(randomize)

    def construct(self, randomize):
        if (randomize):
            # ランダム化＝洗牌する。

            self.randomValue = [None] * self.totalPaiNum

            self.tsumoIndex = 0

            for pai in range(0, 34):
                for i in range(0, 4):
                    self.randomValue[self.tsumoIndex] = PaiAndRandomValue(pai, random.randint(0, 10000))

                    self.tsumoIndex += 1

            self.randomValue = sorted(self.randomValue, key=lambda x: x.randomValue)

            for i in range(0, len(self.randomValue)):
                self.pai_list.append(Pai(self.randomValue[i].pai))
        else:
            # ランダム化＝洗牌しない。

            for pai in range(0, 33 + 1):
                for i in range(0, 4 + 1):
                    self.pai_list.append(Pai(pai))

    #/**
    # * デバッグ用に積み込みを行い全牌のコレクションを構築する。
    # * @param tsumikomi 積み込む牌
    # */
    def construct_tsumikomi(self, randomize):
        self.construct(self, randomize)

        start = 10

        for i in range(0, tsumikomi.length + 1):
            find = False

            j = self.size()-1
            while j>=0 and find == False:
                if (j >= start and j < start + i) == False:
                    # 確定部分以外。交換可能な牌。

                    if (tsumikomi[i] == self.get(j).kind):
                        # 欲しい牌。

                        p = self.get(start + i)
                        self.set(start + i, self.get(j))
                        self.set(j, p)

                        find = True
                j -= 1

            if find == False:
                # 欲しい牌が見つからなかった。

                raise Exception("{}:{}はもうありません。積込牌を確認してください。".format(i, tsumikomi[i]))

    def get(self, i):
        return self.pai_list[i]

    def set(self, i, p):
           self.pai_list[i] = p

    def size(self):
           return len(self.pai_list)

    #/**
    # * ドラ牌を取得。
    # * @param ura true=裏ドラあり
    # * @return ドラ牌
    # */
    def getDora(self, ura):
        dora = []

        for i in range(0, self.rinshanIndex + 1 + 1):
            dora.append(self.get(8 - i * 2))

            if (ura):
                # 裏ドラあり。

                dora.append(self.get(9 - i * 2))

        return dora

    #/**
    # * 残りツモ牌数を取得。
    # * @return 残りツモ牌数
    # */
    def getNokori(self):
        return self.size() - self.tsumoIndex

    #/**
    # * １枚ツモ。
    # * @return ツモ牌
    # */
    def getTsumohai(self):
        pai = self.get(self.tsumoIndex)

        self.tsumoIndex += 1

        return pai

    #/**
    # * 嶺上牌を取得。
    # * @return 嶺上牌
    # */
    def getRinshanpai(self):
        pai = self.get(14 - self.rinshanIndex - 1)

        self.rinshanIndex += 1

        return pai
