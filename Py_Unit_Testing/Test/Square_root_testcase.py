# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 21/2/2021
# @Last Modified by: Yeshwanth
# @Last Modified time: 21/2/2021 12:30:53
# @Title: Square_root_testcase

import unittest
import square_root 

class SquareRoot(unittest.TestCase):
        
    def test_newton_square_root(self):
        self.assertEqual(square_root.square_root(144),12)
        self.assertEqual(square_root.square_root(64),8)
        self.assertEqual(square_root.square_root(10000),100)
        self.assertEqual(square_root.square_root(9),3)

if __name__ == "__main__":
    unittest.main()