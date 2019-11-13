import unittest
from FantasyTracker.Directory import Directory


class TestDirectory(unittest.TestCase):
    def setUp(self): 
        self.directory = Directory()
    
    def test_Contructor_Initialization_Default(self):
        self.assertEqual(self.directory.week, 0)
        self.assertEqual(self.directory.path, 'Rankings/')
    
    def test_SetWeek_BetweenZeroAndSeventeen_IsBetweenZeroAndSeventeen(self):
        expectedWeek = 9
        # Act
        self.directory.setWeek(expectedWeek)
        # Assert
        self.assertEqual(self.directory.week, expectedWeek)
    
    def test_SetWeek_LessThanZero_ThrownValueError(self):
        with self.assertRaises(ValueError) as result:
            self.directory.setWeek(-1)
        
    def test_SetWeek_MoreThanSeventeen_ThrownValueError(self):
        with self.assertRaises(ValueError) as result:
            self.directory.setWeek(18)
    
    def test_SetWeek_WeekIsNotAnInt_ThrownValueError(self):
        with self.assertRaises(ValueError) as result:
            self.directory.setWeek("I'm not a number! I'm a string!")

if __name__ == '__main__':
    unittest.main()
