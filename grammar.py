

#convert grammar to pushdown automota



class Grammar():
    def __init__(self, file_name):
        self.variables = set()
        self.terminals = set()
        self.start_state = ""
        self.stack = []
        self.grammer_rules = {}
        self.build_grammer_from_file(file_name)
        
    
    def build_grammer_from_file(self, file_name):
        f = open(file_name, "r")
        lines = f.readlines()
        line_number = 1
        for line in lines:
            if line_number == 1:
                self.set_grammar_variables(line)
            elif line_number == 2:
                self.set_grammar_terminals(line)
            elif line_number == 3:
                self.set_grammer_start_state(line)
            else:
                self.add_grammer_rule(line)
            
            line_number += 1

    def set_grammar_variables(self, line):
        line = self.remove_whitespace_and_newline(line)
        variables = self.convert_csv_line_to_list(line)
        self.variables = set(variables)

    def set_grammar_terminals(self, line):
        line = self.remove_whitespace_and_newline(line)
        terminals = self.convert_csv_line_to_list(line)
        self.terminals = set(terminals)
    def set_grammer_start_state(self, line):
        line = self.remove_whitespace_and_newline(line)
        self.start_state = line
    
    def add_grammer_rule(self, line):
        line = self.remove_whitespace_and_newline(line)
        variable_to_terminal = line.split("->")
        variable = variable_to_terminal[0]
        terminal = variable_to_terminal[1]
        if variable in self.grammer_rules:
            self.grammer_rules[variable].append(terminal)
        else:
            self.grammer_rules[variable] = [terminal]
        #going to have to be solved non-determinastically
    
    def run_machine(self, input):
        #add start symbol to start of stack

        #loop

        #remove start symbol from end of stack

        #accept

        pass

    
    def remove_whitespace_and_newline(self, line):
        return line.strip().replace("\n", "")
        
    def convert_csv_line_to_list(self, line):
        return line.split(",")
    
    def get_variables(self):
        return self.variables
    
    def get_terminals(self):
        return self.terminals

    def get_stack(self):
        return self.stack
    
    def get_start_state(self):
        return self.start_state
    
    def get_grammer_rules(self):
        return self.grammer_rules
