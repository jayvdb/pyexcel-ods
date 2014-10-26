import os
import pyexcel
from pyexcel.ext import ods
from StringIO import StringIO
from base import create_sample_file1


class TestStringIO:

    def test_ods_stringio(self):
        odsfile = "cute.ods"
        create_sample_file1(odsfile)
        with open(odsfile, "rb") as f:
            content = f.read()
            r = pyexcel.Reader(("ods", content))
            result=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 1.1, 1]
            actual = pyexcel.utils.to_array(r.enumerate())
            assert result == actual
        if os.path.exists(odsfile):
            os.unlink(odsfile)


    def test_xls_output_stringio(self):
        data = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        io = StringIO()
        w = pyexcel.Writer(("ods",io))
        w.write_rows(data)
        w.close()
        r = pyexcel.Reader(("ods", io.getvalue()))
        result=[1, 2, 3, 4, 5, 6]
        actual = pyexcel.utils.to_array(r.enumerate())
        assert result == actual