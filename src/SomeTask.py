from Task import Task
from StoreTask import StoreTask

class SomeTask(Task):
    def __init__(self, description):
        super().__init__()
        self.description = description
        
    def generate_condition_task(self,seed):
        ...
    
    def generate_code_tempalte(self,seed):
        ...
        
    def generate_template_coderunner(self,seed):
        ...
        


