# Axt: automation tools for taxes in the United States
# Copyright 2017 Matt LaChance
#
# This file is part of Axt.
#
# Axt is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# Axt is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with Axt. If not, see <http://www.gnu.org/licenses/>.
from hamcrest.core.base_matcher import BaseMatcher

class ComposedAssertion (BaseMatcher):

    def _matches (self, item):
        self.particular_matcher = None
        for matcher in self.assertion(item):
            self.particular_matcher = matcher

            if matcher.matches(item):
                continue

            return False

        return True

    def describe_to (self, description):
        self.particular_matcher.describe_to(description)

    def describe_mismatch (self, item, description):
        self.particular_matcher.describe_mismatch(item, description)
