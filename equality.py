from lang_handler import var_handlers
import sys
class Equality(var_handlers):
    def __ne__(self, other):
        return not self.__eq__(other)
    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
               self.__dict__ == other.__dict__