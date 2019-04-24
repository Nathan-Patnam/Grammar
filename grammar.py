

#convert grammar to pushdown automota



class Grammar():
    def __init__(self, file_name):
        self.variables = set()
        self.terminals = set()
        self.start_state = ""
        self.build_file(file_name)
        
    
    def build_file(self, file_name):
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

    
    def remove_whitespace_and_newline(self, line):
        return line.strip().replace("\n", "")
        
    def convert_csv_line_to_list(self, line):
        return line.split(",")
    
    def get_variables(self):
        return self.variables
    
    def get_terminals(self):
        return self.terminals
    
    def get_start_state(self):
        return self.start_state