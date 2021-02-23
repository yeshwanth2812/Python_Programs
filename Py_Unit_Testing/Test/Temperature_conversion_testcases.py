# -*- coding: utf-8 -*-
# @Author: Yeshwanth
# @Date: 21/2/2021
# @Last Modified by: Yeshwanth
# @Last Modified time: 21/2/2021 12:30:53
# @Title: Temperature_conversion_Testcases
import unittest
from PyUnit_Test_Programs.main import Temperature_conversion

class Temperature_conversion(unittest.TestCase):

    def test_temperature_conversion(self):

        self.assertEqual(temperature_conversion.get_temperature_conversion('45F',45,'F'),7)
        self.assertEqual(temperature_conversion.get_temperature_conversion('320f',320,'f'),160)
        self.assertEqual(temperature_conversion.get_temperature_conversion('99c',99,'c'),210)
        self.assertEqual(temperature_conversion.get_temperature_conversion('0C',0,'C'),32)
       

if __name__ == "__main__":
    unittest.main()
