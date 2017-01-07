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
from .hamcrest import *
import unittest

from axt.year2015 import Federal1040

class GivenNullFederal1040 (unittest.TestCase):

    def setUp (self):
        self.tax = Federal1040()

    def test_nothing (self):
        assert_that(self.tax, evaluates_to_false())

    def test_income_begins_at_zero (self):
        assert_that(self.tax.total_income, is_(equal_to(0)))

    def test_total_tax_begins_at_zero (self):
        assert_that(self.tax.total_tax, is_(equal_to(0)))
