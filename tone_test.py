import unittest
import tones

class TestToneMethods(unittest.TestCase):

    def test1(self):
        tests = ['wo3',
                 'ni3 shi4 Zhong1guo2ren2',
                 'Ni3 jiao4 shen2me ming2zi',
                 'Wo3 zhi1 xiang3 chi11 fan4,654 shui4 jiao4.5',
                 'wo613',
                 '123yi1',
                 'wo*123',
                 'bo\\3',
                 'bo\\\\4',
                 'shen2me0',
                 'shen2me5',
                 'shen2me7']
        expected = ['wǒ',
                    'nǐ shì Zhōngguórén',
                    'Nǐ jiào shénme míngzi',
                    'Wǒ zhī xiǎng chī1 fàn,654 shuì jiào.5',
                    'wo613',
                    '123yī',
                    'wo*123',
                    'bo3',
                    'bo\\4',
                    'shénme',
                    'shénme',
                    'shénme7']
        for a, b in zip(tests, expected):
            self.assertEqual(tones.process_text(a), b)

if __name__ == '__main__':
        unittest.main()

