# ----------------------------------------------------
# -- Advanced_Lessons => Unit Testing With Unittest --
# ----------------------------------------------------
# Test Runner 
# - The Module That Run The Unit Testing (unittest,Pytest)
# ---------------------------------------------------------
# Test Case 
# - Smallest Uint Of Testing
# It Use Asserts Methods To Check For Actions And Responses
# Test Suite 
# - Collection Of Multiple Tests Or Actions And Responses
# Test Report 
# A Full Report Contains The Failure Or Succeed
# --------------------------------------------------
# Unittest 
# - Add Tests Into Classes As Methods 
# - A Full Report Contains The Failure Or Succeed 
# https://docs.python.org/3/library/unittest.html
#  -------------------------------------------------




# assert 3 * 8 == 24, "Should Be 24"


# def test_case_one():
#     assert 5 * 10 ==50, "Should Be 50"

# def test_case_tow():
#     assert 5 * 50 ==250, "Should Be 250" 


# if __name__ == "__main__":
#     test_case_one()
#     test_case_tow()

#     print("All Tests Passed")



import unittest

class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(100 > 97, "Should Be True")

    def test_two(self):
        self.assertEqual(2 + 2, 4, "Should Be Equal to 4")
        
    def test_three(self):
        self.assertGreater(100,101,"Should Be True")

if __name__ == "__main__":
    unittest.main()
