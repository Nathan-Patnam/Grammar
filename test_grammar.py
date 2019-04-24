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

    
