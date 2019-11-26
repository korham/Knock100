import unittest
import tempfile
import os

import q10, q11, q12, q13, q14, q15, q16

class TestChapter2(unittest.TestCase):
    def setUp(self):
        tf = tempfile.NamedTemporaryFile(mode="r+", encoding="utf-8", delete=False)
        self.tf_name = tf.name
        tf.write("row1\tone\t一\n")
        tf.write("row2\ttwo\t二\n")
        tf.write("row3\tthree\t三\n")
        tf.write("row4\tfour\t四\n")
        tf.write("row5\tfive\t五\n")
        tf.write("row6\tsix\t六\n")
        tf.write("row7\tseven\t七\n")
        tf.close()

        out_tf = tempfile.NamedTemporaryFile(mode="r+", encoding="utf-8", delete=False)
        self.out_tf_name = out_tf.name
        out_tf.close()

    def tearDown(self):
        if os.path.exists(self.tf_name):
            os.remove(self.tf_name)
        if os.path.exists(self.out_tf_name):
            os.remove(self.out_tf_name)

    def test_q10(self):
        self.assertEqual(7, q10.count_row(self.tf_name))
        
    def test_q11(self):
        q11.make_file_tab_replaced(self.tf_name, self.out_tf_name)
        with open(self.out_tf_name, encoding="utf-8") as out_tf:
            self.assertEqual("row1 one 一\n", out_tf.readline())
            self.assertEqual("row2 two 二\n", out_tf.readline())
            self.assertEqual("row3 three 三\n", out_tf.readline())
            self.assertEqual("row4 four 四\n", out_tf.readline())
            self.assertEqual("row5 five 五\n", out_tf.readline())
            self.assertEqual("row6 six 六\n", out_tf.readline())
            self.assertEqual("row7 seven 七\n", out_tf.readline())
            self.assertFalse(out_tf.readline())

    def test_q12(self):
        q12.make_file_cut_col(self.tf_name, self.out_tf_name, 0)
        with open(self.out_tf_name, encoding="utf-8") as out_tf:
            out_tf.seek(0)
            self.assertEqual("row1\n", out_tf.readline())
            self.assertEqual("row2\n", out_tf.readline())
            self.assertEqual("row3\n", out_tf.readline())
            self.assertEqual("row4\n", out_tf.readline())
            self.assertEqual("row5\n", out_tf.readline())
            self.assertEqual("row6\n", out_tf.readline())
            self.assertEqual("row7\n", out_tf.readline())
            self.assertFalse(out_tf.readline())
    
    def test_q13(self):
        try:
            left = tempfile.NamedTemporaryFile(mode="r+", encoding="utf-8", delete=False)
            left.write("one\n")
            left.write("two\n")
            left.write("three\n")
            left.close()
            right = tempfile.NamedTemporaryFile(mode="r+", encoding="utf-8", delete=False)
            right.write("一\n")
            right.write("二\n")
            right.write("三\n")
            right.close()
            q13.make_file_paste(left.name, right.name, self.out_tf_name)
        except:
            raise
        finally:
            if os.path.exists(left.name):
                os.remove(left.name)
            if os.path.exists(right.name):
                os.remove(right.name)

        with open(self.out_tf_name, encoding="utf-8") as out_tf:
            out_tf.seek(0)
            self.assertEqual("one\t一\n", out_tf.readline())
            self.assertEqual("two\t二\n", out_tf.readline())
            self.assertEqual("three\t三\n", out_tf.readline())
            self.assertFalse(out_tf.readline())

    def test_q13_different_length(self):
        try:
            left = tempfile.NamedTemporaryFile(mode="r+", encoding="utf-8", delete=False)
            left.write("one\n")
            left.write("two\n")
            left.write("three\n")
            left.close()
            right = tempfile.NamedTemporaryFile(mode="r+", encoding="utf-8", delete=False)
            right.write("一\n")
            right.write("二\n")
            right.close()
            q13.make_file_paste(left.name, right.name, self.out_tf_name)
        except:
            raise
        finally:
            if os.path.exists(left.name):
                os.remove(left.name)
            if os.path.exists(right.name):
                os.remove(right.name)
            
        with open(self.out_tf_name, encoding="utf-8") as out_tf:
            out_tf.seek(0)
            self.assertEqual("one\t一\n", out_tf.readline())
            self.assertEqual("two\t二\n", out_tf.readline())
            self.assertEqual("three\t\n", out_tf.readline())
            self.assertFalse(out_tf.readline())

    def test_q14(self):
        num = 2
        result = q14.get_head_rows(self.tf_name, num)
        self.assertEqual(num, len(result))
        self.assertEqual("row1\tone\t一\n", result[0])
        self.assertEqual("row2\ttwo\t二\n", result[1])

    def test_q15(self):
        num = 2
        result = q15.get_tail_rows(self.tf_name, num)
        self.assertEqual(num, len(result))
        self.assertEqual("row6\tsix\t六\n", result[0])
        self.assertEqual("row7\tseven\t七\n", result[1])

    def test_q16(self):
        num = 3
        out_dir = os.path.dirname(self.tf_name)
        try:
            q16.make_splitted_files(self.tf_name, out_dir, num)
            self.assertTrue(os.path.exists(self.tf_name + "aa"))
            self.assertTrue(os.path.exists(self.tf_name + "ac"))
            with open(self.tf_name + "aa", encoding="utf-8") as aa, \
            open(self.tf_name + "ac", encoding="utf-8") as ac:
                self.assertEqual(3, len(aa.readlines()))
                self.assertEqual(1, len(ac.readlines()))            
        except:
            raise
        finally:
            if os.path.exists(self.tf_name + "aa"):
                os.remove(self.tf_name + "aa")
            if os.path.exists(self.tf_name + "ab"):
                os.remove(self.tf_name + "ab")
            if os.path.exists(self.tf_name + "ac"):
                os.remove(self.tf_name + "ac")

if __name__ == '__main__':
    unittest.main()