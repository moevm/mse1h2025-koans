class GeneralGenerator:
    def __init__(self, seed):
        self.type_dict = {
            1: self.generate_condition_task(),
            2: self.generate_code_template(),
            3: self.generate_template_coderunner()
        }
        self.seed = seed
    def generate(self, type_of_generation, task_name, seed = ''):
        self.type_dict[type_of_generation](task_name, seed)
        
    def __get__(self):
        ...
    def generate_condition_task(self, task_name):
        ...
    def generate_code_template(self, task_name, seed):
        ...
    def generate_template_coderunner(self,task_name,seed):
        ...
    