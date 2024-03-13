from logic.Pai import Pai
from logic.PaiKind import PaiKind, PaiKindShort
from logic.MachiPattern import MachiPattern

print('M1-9 S1-9 S1-9 TON NAN SHA PEI HAKU HATSU CHUN')
print('> ', end='')
line = input()
# line = 'M1 M1 M1 P2 P2 P2 S3 S5 TON TON TON NAN NAN'
tehai = [Pai(PaiKindShort.value_of(p)) for p in line.split()]
machiPattern = MachiPattern(tehai, True)
machi = machiPattern.getMachi()

if len(machi) > 0:
    print('loopCount={}'.format(machiPattern.loopCount))
    print('{}待ち'.format(machiPattern.machiElementCollection.toString()))
    print(' '.join([PaiKind(m).name for m in machi]) + "待ち")
