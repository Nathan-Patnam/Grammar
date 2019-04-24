

#convert grammar to pushdown automota



class Grammar():
    def __init__(self, file_name):
        self.name = ""
        self.variables = set()
        self.build_file(file_name)
        
    
    def build_file(self, file_name):
        f = open(file_name, "r")
        lines = f.readlines()
        line_number = 1
        for line in lines:
            if line_number == 1:
                self.set_grammar_variables(line)
            
            line_number += 1

    def set_grammar_variables(self, line):
        line = self.remove_whitespace_and_newline(line)
        variables = self.convert_csv_line_to_list(line)
        self.variables = set(variables)
    

    
    def remove_whitespace_and_newline(self, line):
        return line.strip().replace("\n", "")
        
    def convert_csv_line_to_list(self, line):
        return line.split(",")
    
    def get_variables(self):
        return self.variables
