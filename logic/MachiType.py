from enum import IntEnum

#/**
# * 待ちのタイプ。
# */
class MachiType(IntEnum):
    Tanki = 0
    Penchan = 1
    Kanchan = 2
    Ryanmen = 3
    Shanpon = 4

class MachiTypeJp(IntEnum):
    単騎待ち = 0
    辺張待ち = 1
    嵌張待ち = 2
    両面待ち = 3
    双石並待ち = 4
