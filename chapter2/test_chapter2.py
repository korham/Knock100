import unittest
import tempfile
import os
import string

import q10, q11, q12, q13, q14, q15, q16, q17, q18, q19

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

    def test_q12_delimiter(self):
        tf = tempfile.NamedTemporaryFile(mode="r+", encoding="utf-8", delete=False)
        out_tf = tempfile.NamedTemporaryFile(mode="r+", encoding="utf-8", delete=False)
        tf.write("1,one,a\n")
        tf.write("2,two,b\n")
        tf.write("3,three,c\n")
        tf.close()
        out_tf.close()
        try:
            q12.make_file_cut_col(tf.name, out_tf.name, 2, ",")
            with open(out_tf.name, encoding="utf-8") as o:
                o.seek(0)
                self.assertEqual("a\n", o.readline())
                self.assertEqual("b\n", o.readline())
                self.assertEqual("c\n", o.readline())
                self.assertFalse(o.readline())
        except:
            raise
        finally:
            if os.path.exists(tf.name):
                os.remove(tf.name)
            if os.path.exists(out_tf.name):
                os.remove(out_tf.name)


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

    # 分割しようとすると接尾辞が不足する("zz"まで使い切る）ケース
    def test_q16_too_many_rows(self):
        num = 3
        suffix_list = [s1+s2 for s1 in string.ascii_lowercase for s2 in string.ascii_lowercase]
        too_many = tempfile.NamedTemporaryFile(mode="r+", encoding="utf-8", delete=False)
        for i in range((num*len(suffix_list))+1):
            too_many.write("row\ttest\t" +str(i) + "\n")
        too_many.close()
        out_dir = os.path.dirname(too_many.name)
        try:
            with self.assertRaises(Exception):
                q16.make_splitted_files(too_many.name, out_dir, num)
        except:
            raise
        finally:
            if os.path.exists(too_many.name):
                os.remove(too_many.name)
            for suffix in suffix_list:
                if os.path.exists(too_many.name + suffix):
                    os.remove(too_many.name + suffix)

    def test_q17(self):
        q17_tf = tempfile.NamedTemporaryFile(mode="r+", encoding="utf-8", delete=False)
        q17_tf.write("A\t1\n")
        q17_tf.write("A\t2\n")
        q17_tf.write("B\t3\n")
        q17_tf.write("B\t4\n")
        q17_tf.write("C\t5\n")
        q17_tf.write("D\t6\n")
        q17_tf.write("E\t7\n")
        q17_tf.write("D\t8\n")
        q17_tf.write("C\t9\n")
        q17_tf.write("C\t10\n")
        q17_tf.close()
        try:
            result = q17.sort_uniq(q17_tf.name)
            self.assertEqual({"A", "B", "C", "D", "E"}, result)
        except:
            raise
        finally:
            if os.path.exists(q17_tf.name):
                os.remove(q17_tf.name)


    def test_q18(self):
        col = 2
        q18_tf = tempfile.NamedTemporaryFile(mode="r+", encoding="utf-8", delete=False)
        q18_tf.write("A\ta\t10\n")
        q18_tf.write("B\tb\t40\n")
        q18_tf.write("C\tc\t20\n")
        q18_tf.write("D\td\t60\n")
        q18_tf.write("E\te\t70\n")
        q18_tf.write("F\tf\t50\n")
        q18_tf.write("G\tg\t30\n")
        q18_tf.close()
        try:
            result = q18.sort_reverse(q18_tf.name, col)
            self.assertEqual(["E\te\t70\n",
                              "D\td\t60\n",
                              "F\tf\t50\n",
                              "B\tb\t40\n",
                              "G\tg\t30\n",
                              "C\tc\t20\n",
                              "A\ta\t10\n"], result)
        except:
            raise
        finally:
            if os.path.exists(q18_tf.name):
                os.remove(q18_tf.name)

    def test_q19(self):
        tf = tempfile.NamedTemporaryFile(mode="r+", encoding="utf-8", delete=False)
        tf.write("A\t1\n")
        tf.write("A\t2\n")
        tf.write("B\t3\n")
        tf.write("B\t4\n")
        tf.write("C\t5\n")
        tf.write("D\t6\n")
        tf.write("E\t7\n")
        tf.write("D\t8\n")
        tf.write("C\t9\n")
        tf.write("C\t10\n")
        tf.close()
        try:
            result = q19.count_sort(tf.name, 0, "\t")
            self.assertEqual(["3 C\n", "2 A\n", "2 B\n", "2 D\n", "1 E\n"], result)
        except:
            raise
        finally:
            if os.path.exists(tf.name):
                os.remove(tf.name)

if __name__ == '__main__':
    unittest.main()