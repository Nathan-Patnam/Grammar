#from ..nfa import build_nfa
import pytest
from grammar import Grammar


class TestDPDA(object):


    @pytest.fixture(scope="function")
    def create_gramamr(self):
        grammar = Grammar("grammar.txt")
        return grammar

    def test_set_grammar_variables(self, create_gramamr):
        variables = set(["A", "B"])
        grammar_variables = create_gramamr.get_variables()
        assert variables == grammar_variables

    def test_set_grammar_terminals(self, create_gramamr):
        terminals = set(["0", "1", "#"])
        grammar_terminals = create_gramamr.get_terminals()
        assert terminals == grammar_terminals
    
    def test_get_stack(self, create_gramamr):
        stack = []
        grammar_stack = create_gramamr.get_stack()
        assert stack == grammar_stack
    
    def test_set_state_state(self, create_gramamr):
        start_state = "A"
        grammer_start_state = create_gramamr.get_start_variable()
        assert start_state == grammer_start_state
    
    def test_set_grammer_rules(self, create_gramamr):
        rules = {
            "A": ["0A1", "B", "0A11"],
            "B":["#"]
        }
        grammer_rules = create_gramamr.get_grammer_rules()
        assert rules == grammer_rules
    

    def test_stack_contents_on_empty_string(self, create_gramamr):
        expression = ""
        stack  = ["$", "A"]

        create_gramamr.run_machine(expression)
        grammar_stack = create_gramamr.get_stack()
        assert stack == grammar_stack
    
    """
    def test_reject_string(self, create_gramamr):
        expression = ""
        will_expression_accept = False

        grammer_accept_string = create_gramamr.run_machine(expression)
        assert will_expression_accept == grammer_accept_string
    """
