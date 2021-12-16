from ortools.sat.python import cp_model

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0

        
    def on_solution_callback(self):
        result = []
        self.__solution_count += 1
        
        for v in self.__variables:
            print('%s=%i' % (v, self.Value(v)), end=' ')
            result.append(self.Value(v))
        print()
        Report.append(result)

    def solution_count(self):
        return self.__solution_count
    
    
def CreateNumTypeBlk(Report):
    n = 12#int(input())
    model = cp_model.CpModel()
    
    v2 = model.NewIntVar(3, 8, 'v2')
    v3 = model.NewIntVar(1, 1, 'v3')
    h2 = model.NewIntVar(3, 8, 'h2')
    h3 = model.NewIntVar(1, 1, 'h3')
    main = model.NewIntVar(1, 1, 'main')
    
    solution_printer = VarArraySolutionPrinter([v2, v3, h2, h3, main])
    # Constraint:
    model.Add(v2 + v3 + h2 + h3  == n - 1)
    model.Add(2*v2 + 3*v3 + 2*h2 + 3*h3 + 2*main <=30)
   
    solver = cp_model.CpSolver()
    solver.parameters.enumerate_all_solutions = True
    status = solver.Solve(model, solution_printer)
    print(solution_printer.solution_count())     
    
Report = []
CreateNumTypeBlk(Report)