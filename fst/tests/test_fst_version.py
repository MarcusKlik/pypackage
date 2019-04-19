
import fst

class Test_fst_version(object):

    def test_returns_string(self):
        v = fst.fst_version()
        assert isinstance(v, str)

    def test_correct_version(self):
        v = fst.fst_version()
        assert v == "0.0.1"
