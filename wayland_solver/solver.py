class SolverException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class SolutionException(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class Solver:
    def __init__(self):
        return
    
    #To-Implement methods(Executed sequentially)
    def get_intro(self)->str:
        #Intro must be minimal Markdown
        raise SolverException("Not Implemented")

    def try_analysis(self)->bool:
        raise SolverException("Not Implemented")
    
    def get_analysis_report(self)->str:
        raise SolverException("Not Implemented")

    def get_solution(self)->bool:
        raise SolverException("Not Implemented")

    def is_solution_available(self)->bool:
        raise SolverException("Not Implemented")

    def get_solution_report(self)->str:
        #Solution Report must be minimal Markdown
        raise SolverException("Not Implemented")
    
    def set_solution(self, solution_idx):
        raise SolverException("Not Implemented")
    
    def backup_msg(self)->str:
        raise SolverException("Not Implemented")
    
    def try_backup(self)->bool:
        raise SolverException("Not Implemented")

    def try_apply(self)->bool:
        raise SolverException("Not Implemented")

    def show_logs(self):
        raise SolverException("Not Implemented")
    
    #Helper methods
    def get_root_privilege():
        
        return
    
class Solution:
    def __init__(self):
        raise SolutionException("Not Implemented")

    def backup_msg(self):
        raise SolutionException("Not Implemented")

    def backup(self):
        raise SolutionException("Not Implemented")

    def apply(self):
        raise SolutionException("Not Implemented")