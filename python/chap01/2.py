import unittest
from collections import Counter


def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)


def permutation_counter(str1, str2):
    d = dict(Counter(str1))

    for s in str2:
        if s not in d:
            return False
    return True



class Test(unittest.TestCase):
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_check_permutation(self):
        # true check
        for test_strings in self.dataT:
            result = check_permutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = check_permutation(*test_strings)
            self.assertFalse(result)

    def test_permutation_check(self):
        # true check
        for test_strings in self.dataT:
            result = permutation_counter(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = permutation_counter(*test_strings)
            self.assertFalse(result)




if __name__ == "__main__":
    unittest.main()
