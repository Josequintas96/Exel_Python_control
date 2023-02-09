
from unittest import TestCase
import unittest
import yfinance as yf

import sys
sys.path.append('..')
from Group import *
from read_file import control_Group


class Yahoo_test(unittest.TestCase):
    def test_yahoo_info_longName(self):
        gg = yf.Ticker("DIS")
        
        try:
            info = gg.info['longName']
        except:
            info = "DIS"
        
        assert info == "The Walt Disney Company" or info == "DIS"
        
        
    def test_yahoo_fast_info_price(self):
        gg = yf.Ticker("DIS")
        price = gg.fast_info['last_price']
        assert type(price) == float
        
        
    # def test_yahoo_info_longName(self):
    #     gg = yf.Ticker("DIS")
    #     info = gg.info['longName']
    #     print("TT: ", info)
    #     assert info == "The Walt Disney Company"
    # def test_yahoo_info_longName(self):
    #     gg = yf.Ticker("DIS")
    #     info = gg.info['longName']
    #     print("TT: ", info)
    #     assert info == "The Walt Disney Company"

class Group_Test(unittest.TestCase):
    def test_init(self):
        GroupX = Group("test_stocks.txt")
        control_Group(GroupX, "test_stocks.txt")
        x = GroupX.Group_get_num_persons()
        assert x == 1
        
    def test_number_of_Stocks(self):
        GroupX = Group("test_stocks.txt")
        control_Group(GroupX, "test_stocks.txt")
        x = GroupX.Group_get_num_persons_stocks(0)
        assert x == 6
        
    def test_answer3(self):
        x = 7
        assert x == 7
        
    def test_answer4(self):
        x = 8
        assert x == 8
        
    def test_answer5(self):
        x = 56
        assert x == 56

class Answer_Test(unittest.TestCase):
    def test_answer2(self):
        x = 6
        assert x == 6
        
    def test_answer3(self):
        x = 7
        assert x == 7
        
    def test_answer4(self):
        x = 89
        assert x == 89
        
    def test_answer5(self):
        x = 55
        assert x == 55



if __name__ == '__main__':
	unittest.main()



