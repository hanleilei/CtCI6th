import unittest

def unique_with_list_and_set(string):
    if len(string) > 128:
        return False

    return len(string) == len(set(string))

def is_unique(string): # no data structure
    string = sorted(string)

    for i in range(len(string) - 1 ):
        if string[i] == string[i+1]:
            return False
    return True


def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique_with_list_and_set(self):
        for test_string in self.dataT:
            actual = unique_with_list_and_set(test_string)
            self.assertTrue(actual)

        for test_string in self.dataF:
            actual = unique_with_list_and_set(test_string)
            self.assertFalse(actual)

    def test_is_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique(test_string)
            self.assertFalse(actual)

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
