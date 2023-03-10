import unittest
from check_pwd import check_pwd


class TestCase(unittest.TestCase):
    def test1(self):
        input = ""
        self.assertFalse(check_pwd(input))
    def test2(self):
        input = "0"
        self.assertFalse(check_pwd(input))
    def test3(self):
        input="00000000000000000000000"
        self.assertFalse(check_pwd(input))
    def test4(self):
        input="ADKSNDESKA"
        self.assertFalse(check_pwd(input))
    def test5(self):
        input ="adksndeska"
        self.assertFalse(check_pwd(input))
    
    def test6(self):
        input ="aabbDDseadsf4"
        self.assertFalse(check_pwd(input))

    def test7(self):
        input ="@@@@@@@@@@@@@@@@@"
        self.assertFalse(check_pwd(input))

if __name__ == "__main__":
    unittest.main()