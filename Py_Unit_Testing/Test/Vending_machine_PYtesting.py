# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 21/2/2021
# @Last Modified by: Yeshwanth
# @Last Modified time: 21/2/2021 12:30:53
# @Title: Vending machine test case

import unittest
import Vending_machine

class Vending_Machine(unittest.TestCase):

    def test_currency_count(self):

        self.assertEqual(Vending_machine.currency_count(200),("100 : 2,"))
        self.assertEqual(Vending_machine.currency_count(5),("5 : 1,"))
        self.assertEqual(Vending_machine.currency_count(85),("50 : 1,20 : 1,10 : 1,5 : 1,"))
if __name__ == "__main__":
    unittest.main()        