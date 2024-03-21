from enum import IntEnum

#/**
# * 待ちのタイプ。
# */
class MachiType(IntEnum):
    Tanki = 0
    Ryanmen = 1
    Penchan = 2
    Kanchan = 3
    Shanpon = 4

class MachiTypeJp(IntEnum):
    単騎待ち = 0
    両面待ち = 1
    辺張待ち = 2
    嵌張待ち = 3
    双石並待ち = 4
