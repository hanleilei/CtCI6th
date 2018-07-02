import unittest
from collections import Counter

# 两个坑，第一个：测试字符串有空格，最终结果需要忽略空格。第二个，判断出现一次的字母必须是零次或者一次

def pal_perm(string):
    c = dict(Counter([i for i in list(string.lower()) if i != ' ']))
    res = 0
    for i in c.values():
        if i % 2:
            res += 1
    return res <= 1


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
