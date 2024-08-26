from .Pai import Pai
from .PaiKind import PaiKind, PaiKindShort
from .MachiPattern import MachiPattern
import random

def generate_chiniso_tenpai():
    num_conv = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,4]

    while True:
        tehai = []
        p = random.randint(1, 4)
        while len(tehai) < 13:
            r = random.randint(0, len(num_conv)-1)
            for i in range(0, num_conv[r]):
                tehai.append(p)
            p += 1
            if p > 9:
                break
        tehai = tehai[0:13]

        line = ' '.join([f'M{p}' for p in tehai])
        tehai = [Pai(PaiKindShort.value_of(p)) for p in line.split()]
        machiPattern = MachiPattern(tehai, True)
        machi = machiPattern.getMachi()

        if len(tehai) == 13 and len(machi) > 0:
            break
    return tehai, line, machiPattern

if __name__ == '__main__':
    tehai, line, machiPattern = generate_chiniso_tenpai()
    print(line)
    print('loopCount={}'.format(machiPattern.loopCount))
    for m in machiPattern.machiElementCollection.sort():
        pass#print(m.type)
    print(' '.join([PaiKind(m).name for m in machi]) + "待ち")
