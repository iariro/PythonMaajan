from logic.Pai import Pai
from logic.PaiKind import PaiKind, PaiKindShort
from logic.MachiPattern import MachiPattern
import random

tehai = []
p = random.randint(1, 4)
while len(tehai) < 13:
    for i in range(0, random.randint(0, 4)):
        tehai.append(p)
    p += 1
    if p > 9:
        break
tehai = tehai[0:13]

line = ' '.join([f'M{p}' for p in tehai])
print(line)
tehai = [Pai(PaiKindShort.value_of(p)) for p in line.split()]
machiPattern = MachiPattern(tehai, True)
machi = machiPattern.getMachi()

if len(machi) > 0:
    print('loopCount={}'.format(machiPattern.loopCount))
    for m in machiPattern.machiElementCollection.sort():
        print(m.type)
    print(' '.join([PaiKind(m).name for m in machi]) + "待ち")
