# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 21/2/2021
# @Last Modified by: Yeshwanth
# @Last Modified time: 21/2/2021 12:30:53
# @Title: Monthly_payment_Testcase

import unittest  
import Monthly_payment 

class MonthlyPayment(unittest.TestCase):

    def test_monthly_payment(self):
        self.assertEqual(monthly_payment.get_monthly_payment(96000,2,1), 4041.8)
        self.assertEqual(monthly_payment.get_monthly_payment(2000,1,2),168.48)
        self.assertNotEqual(monthly_payment.get_monthly_payment(9000,1.5,10),1996)

if __name__ == "__main__":
    unittest.main()