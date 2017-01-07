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
from hamcrest.core.base_matcher import BaseMatcher

class HasTruthiness (BaseMatcher):

    def __init__ (self, expected):
        self.expected = expected

    def _matches (self, item):
        return self.__get_bool_for(item) == self.expected

    def describe_to (self, description):
        description.append_text("an object with {} truthiness".format(
                repr(self.expected)))

    def describe_mismatch (self, item, description):
        actual = self.__get_bool_for(item)

        if actual is None:
            description.append_text("no truthiness ") \
                    .append_description_of(item)

        else:
            description.append_text("was {} ".format(actual)) \
                    .append_description_of(item)

    def __get_bool_for (self, item):
        try:
            result = bool(item)
            if result is True or result is False:
                return result

        except:
            pass

def evaluates_to_true():
    return HasTruthiness(True)

def evaluates_to_false():
    return HasTruthiness(False)
