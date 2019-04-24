

#convert grammar to pushdown automota



class Grammar():
    def __init__(self, file_name):
        self.variables = set()
        self.terminals = set()
        self.start_variable = ""
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
        self.start_variable = line
    
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
        #add marker symbol to start of stack, '$' will be used to represent this
        self.push_marker_symbol()
        self.push_start_symbol()
        #push on start symbol


        #loop

        #remove marker symbol from end of stack, $ was used to represent this

        #accept

        pass

    def push_marker_symbol(self):
        self.stack.append("$")
    
    def push_start_symbol(self):
        self.stack.append(self.start_variable)
    
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
    
    def get_start_variable(self):
        return self.start_variable
    
    def get_grammer_rules(self):
        return self.grammer_rules
