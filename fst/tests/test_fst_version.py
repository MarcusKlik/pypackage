#  fst-format - Python package for ultra fast storage and retrieval of datasets
#
#  Copyright (C) 2019-present, Mark AJ Klik
#
#  This file is part of the fst-format Python package.
#
#  The fst-format Python package is free software: you can redistribute it
#  and/or modify it under the terms of the GNU Affero General Public License
#  version 3 as published by the Free Software Foundation.
#
#  The fst-format Python package is distributed in the hope that it will be
#  useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero
#  General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with the fst-format Python package. If not, see
#  <http://www.gnu.org/licenses/>.
#
#  You can contact the author at:
#  - fst-format source repository: https://github.com/fstpackage/fst-format

import fst

class Test_fst_version(object):

    def test_returns_string(self):
        v = fst.fst_version()
        assert isinstance(v, str)

    def test_correct_version(self):
        v = fst.fst_version()
        assert v == "0.0.1"
