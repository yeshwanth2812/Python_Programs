# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 21/2/2021
# @Last Modified by: Yeshwanth
# @Last Modified time: 21/2/2021 12:30:53
# @Title: ToBinary_Testcase

import unittest
import decimal_to_binary 

class Binary(unittest.TestCase):
        
    def test_newton_square_root(self):
        self.assertEqual(decimal_to_binary.binary(100),1100100)
        self.assertEqual(decimal_to_binary.binary(24),11000)
        self.assertEqual(decimal_to_binary.binary(130),10000010)

if __name__ == "__main__":
    unittest.main()