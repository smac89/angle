
from parser_test_helper import *


class ConditionTest(ParserBaseTest):

    def test_block(self):
        assert_result_is(1,"p begin 1.times do 1 end end")