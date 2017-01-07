# Axt: automation tools for taxes in the United States
# Copyright 2017 Matt LaChance
#
# This file is part of Axt.
#
# Axt is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Axt is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Axt. If not, see <http://www.gnu.org/licenses/>.
from hamcrest import *
import unittest

from axt import hello

class WorkingEnvironmentTest (unittest.TestCase):

    def test_hello_str_exists (self):
        assert_that(hello, is_(equal_to("What's up my droogs")))
