import unittest
import readcountry as prog

class mytestcase(unittest.TestCase):
    def test_sum(self):
        total = prog.CountryAnalysis.total
        self.assertEqual(total,55756301.0)

    def test_mean(self):
        mean = prog.CountryAnalysis.meanValue
        self.assertEqual(mean,30)

if __name__ == '__main__':
    unittest.main()





