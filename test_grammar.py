#from ..nfa import build_nfa
import pytest
from grammar import Grammar


class TestDPDA(object):

    @pytest.fixture(scope="function")
    def create_gramamr(self):
        grammar = Grammar("grammar.txt")
        return grammar

    def test_set_grammar_variables(self, create_gramamr):
        variables = set(["S", "T"])
        grammar_variables = create_gramamr.get_variables()
        assert variables == grammar_variables

    def test_set_grammar_terminals(self, create_gramamr):
        terminals = set(["a", "b"])
        grammar_terminals = create_gramamr.get_terminals()
        assert terminals == grammar_terminals

    def test_get_stack(self, create_gramamr):
        stack = []
        grammar_stack = create_gramamr.get_stack()
        assert stack == grammar_stack

    def test_set_state_state(self, create_gramamr):
        start_state = "S"
        grammer_start_state = create_gramamr.get_start_variable()
        assert start_state == grammer_start_state

    def test_set_grammer_rules(self, create_gramamr):
        rules = {
            "S": ["aTb", "b"],
            "T": ["Ta", "@"]
        }
        grammer_rules = create_gramamr.get_grammer_rules()
        assert rules == grammer_rules

    def test_stack_contents_on_empty_string(self, create_gramamr):
        expression = ""
        stack = ["$", "S"]

        create_gramamr.run_machine(expression)
        grammar_stack = create_gramamr.get_stack()
        assert stack == grammar_stack

    def test_self_loops_contents(self, create_gramamr):
        loop_contents = {
            "@": {
                "S": "b",
                "T":"@"
            },
            "a": {
                "a": "@"
            },
            "b": {
                "b": "@"
            }
        }
        
        grammar_loop = create_gramamr.get_loop()
        assert loop_contents == grammar_loop
    
    def test_sequence_is_not_terminal(self, create_gramamr):
        combination = "c"
        is_combination_a_terminal = False
        assert is_combination_a_terminal == create_gramamr.is_combination_a_terminal(combination)

    def test_sequence_is_terminal(self, create_gramamr):
        combination = "a"
        is_combination_a_terminal = True
        assert is_combination_a_terminal == create_gramamr.is_combination_a_terminal(
            combination)

    """
    def test_reject_string(self, create_gramamr):
        expression = ""
        will_expression_accept = False

        grammer_accept_string = create_gramamr.run_machine(expression)
        assert will_expression_accept == grammer_accept_string
    """
