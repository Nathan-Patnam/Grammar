#from ..nfa import build_nfa
import pytest
from grammar import Grammar


class TestDPDA(object):
    """
    @pytest.fixture(scope="function")
    def create_nfa(self):
        test_nfa = build_nfa("mocks/nfa_1.txt")
        test_nfa.run_machine("./mocks/nfa_input_1.txt",
                             "./mocks/outputs/nfa_output_1.txt")
        return test_nfa

    def test_get_states(self, create_nfa):
        states = set(["s2", "s1", "s3", "s4", "s5"])
        nfa_states = create_nfa.states
        assert states == nfa_states
    """

    @pytest.fixture(scope="function")
    def create_gramamr(self):
        grammar = Grammar("grammar.txt")
        return grammar

    def test_set_grammar_variables(self, create_gramamr):
        variables = set(["A", "B"])

        grammar_variables = create_gramamr.get_variables()
        assert variables == grammar_variables

    
