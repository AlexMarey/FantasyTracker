import unittest
from FantasyTracker.Directory import Directory


class TestDirectory(unittest.TestCase):
    def setUp(self): 
        self.directory = Directory()
    
    def test_Contructor_Initialization_Default(self):
        self.assertEqual(self.directory.week, 0)
        self.assertEqual(self.directory.path, 'Rankings/')
    
    def test_SetWeek_LessThanZero_IsNegativeOne(self):
        # Act
        self.directory.setWeek(-1)
        # Assert
        self.assertEqual(self.directory.week, -1)
        
    def test_SetWeek_MoreThanSeventeen_IsNegativeOne(self):
        # Act
        self.directory.setWeek(18)
        # Assert
        self.assertEqual(self.directory.week, -1)
    
    def test_SetWeek_BetweenZeroAndSeventeen_IsBetweenZeroAndSeventeen(self):
        # Act
        self.directory.setWeek(9)
        # Assert
        self.assertEqual(self.directory.week, 9)
    
    def test_SetWeek_WeekIsNotAnInt_ThrownException(self):
        # Assert
        with self.assertRaises(ValueError) as result:
            self.directory.setWeek("I'm not a number! I'm a string!")

        

if __name__ == '__main__':
    unittest.main()
