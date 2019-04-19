
import fst

class Test_fst_version(object):

    def test_returns_string(self):
        v = fst.fst_version()
        assert isinstance(v, str)
