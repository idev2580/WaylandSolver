from wayland_solver.solver import Solver

#Simple Electron-wayland problem solver as an example.
class ElectronSolver(Solver):
    CONF_DIR_LIST = [
        '~/.config'
    ]
    INTRO = '''
    # Electron Wayland Problem Solver
    This is a problem solver for electron based program on wayland.
    Below is a brief list of electron-based programs.

    - Visual Studio Code
    - Slack
    - balenaEtcher
    - Freetube

    Please make sure that you are having problems for those programs,
    with following signs.

    - IME not working
    - Xwayland used(Blurry text, No Scaling, Touch problems)
    '''

    #Implementaion of ISolver methods
    def __init__(self):
        self.is_config_file_found:bool = False
        self.is_configured_well:bool   = False
        self.possible_solutions:list = []
        self.selected_solution:int = -1
        self.log:str = ""
        return
    
    def get_intro(self)->str:
        return ElectronSolver.INTRO

    def try_analysis(self)->bool:
        #Find for config files

        #Read config files

        return
    
    def get_analysis_report(self)->str:
        #Show how it configured

        return

    def get_solution(self)->bool:
        #Find for Solution
        if(self.is_config_file_found):
            if(self.is_configured_well):
                #No other solutions available
                return True
        
        #Use electron-flags.conf

        return True
    
    def is_solution_available(self)->bool:
        return

    def get_solution_report(self)->str:
        sol_report:str = "# Possible Solutions\n"
        number = 1
        for i in possible_solutions_details:
            sol_report += "{}. {}\n".format(number, i)
            number += 1
        return sol_report
    
    def set_solution(self, solution_idx):
        return
    
    def backup_msg(self)->str:

        return
    
    def try_backup(self)->bool:
        #If there was a config file, backup

        return

    def try_apply(self)->bool:

        return

    def show_logs(self):

        return

class ElectronConfigFixSolution(Solution):
    def _get_backup_file_name(self, filename):
        return filename+".backup"

    def __init__(self, fileDir:str):
        self.conf_file:str = fileDir
        return
    
    def backup_msg(self):
        return "Backup {} into {}".format(self.conf_file, self._get_backup_file_name(self.conf_file))

    def backup(self):
        return

    def apply(self):
        return