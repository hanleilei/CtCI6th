import unittest
# similiar with leetcode: https://leetcode.com/problems/string-compression/description/

def string_compression(chars):
    c = chars[0]
    counter = 1
    if len(chars) == 1:
        return chars
    for i in range(1, len(chars)):
        if chars[i] == chars[i-1]:
            counter += 1
        else:
            c = c + str(counter) + chars[i]
            counter = 1
    if counter > 1:
        return c + str(counter)
    else:
        return c



class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
