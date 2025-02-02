import unittest
import cwe_checker_testlib


class TestCwe782(unittest.TestCase):

    def setUp(self):
        self.target = '782'
        self.string = b'Exposed IOCTL with Insufficient Access Control'

    def test_cwe782_01_x64_gcc(self):
        expect_res = 1
        res = cwe_checker_testlib.execute_and_check_occurence(self.target, self.target, 'x64', 'gcc', self.string)
        self.assertEqual(res, expect_res)

    def test_cwe782_01_x64_clang(self):
        expect_res = 1
        res = cwe_checker_testlib.execute_and_check_occurence(self.target, self.target, 'x64', 'clang', self.string)
        self.assertEqual(res, expect_res)
