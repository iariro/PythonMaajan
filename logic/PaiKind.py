from enum import IntEnum

#/**
# * 牌種別列挙型。
# */
class PaiKind(IntEnum):
    一萬 = 0
    二萬 = 1
    三萬 = 2
    四萬 = 3
    五萬 = 4
    六萬 = 5
    七萬 = 6
    八萬 = 7
    九萬 = 8
    一筒 = 9
    二筒 = 10
    三筒 = 11
    四筒 = 12
    五筒 = 13
    六筒 = 14
    七筒 = 15
    八筒 = 16
    九筒 = 17
    一索 = 18
    二索 = 19
    三索 = 20
    四索 = 21
    五索 = 22
    六索 = 23
    七索 = 24
    八索 = 25
    九索 = 26
    東 = 27
    南 = 28
    西 = 29
    北 = 30
    白 = 31
    發 = 32
    中 = 33

#/**
# * 牌種別列挙型。
# */
class PaiKindShort(IntEnum):
    M1 = 0
    M2 = 1
    M3 = 2
    M4 = 3
    M5 = 4
    M6 = 5
    M7 = 6
    M8 = 7
    M9 = 8
    P1 = 9
    P2 = 10
    P3 = 11
    P4 = 12
    P5 = 13
    P6 = 14
    P7 = 15
    P8 = 16
    P9 = 17
    S1 = 18
    S2 = 19
    S3 = 20
    S4 = 21
    S5 = 22
    S6 = 23
    S7 = 24
    S8 = 25
    S9 = 26
    TON = 27
    NAN = 28
    SHA = 29
    PEI = 30
    HAKU = 31
    HATSU = 32
    CHUN = 33

    @classmethod
    def value_of(cls, target_name):
        for pai in PaiKindShort:
            if pai.name == target_name:
                return pai
