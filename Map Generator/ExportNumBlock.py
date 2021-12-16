from ortools.sat.python import cp_model

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables, limit):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0
        self.__solution_limit = limit
        
    def on_solution_callback(self):
        self.__solution_count += 1
        result2 = [[self.Value(v) for v in self.__variables[0][0]], [self.Value(v) for v in self.__variables[0][1]], \
                   self.Value(self.__variables[1][0]),\
                   self.Value(self.__variables[1][1])]
        Report2.append(result2)
        #print(result2)
        if self.__solution_count >= self.__solution_limit:
            print('Stop search after %i solutions' % self.__solution_limit)
            self.StopSearch()
    def solution_count(self):
        return self.__solution_count
    
    
def CreateNumTypeBlk2(Report):
    model = cp_model.CpModel()
    NumBlkOfCol2 = []
    NumBlkOfRow2 = []
    #for i in range()
    RowH3 = model.NewIntVar(0, 5, 'RowH3')
    ColV3 = model.NewIntVar(0, 5, 'ColV3')
    
    v2, _, h2, _, _ = Report[0]
    for i in range(6):
        NumBlkOfCol2.append(model.NewIntVar(0, 2, 'NumBlkOfCol[%d]' % i))
        
    for i in range(6):
        NumBlkOfRow2.append(model.NewIntVar(0, 2, 'NumBlkOfRow[%d]' % i)) 
  
    solution_printer = VarArraySolutionPrinter([[NumBlkOfCol2, NumBlkOfRow2],[ColV3, RowH3]], 1000)
    model.Add(sum(NumBlkOfCol2) == v2)
    model.Add(sum(NumBlkOfRow2) == h2)
    for i in range(6):
        test1 = model.NewBoolVar('test1')
        model.Add(NumBlkOfCol2[i] == 0).OnlyEnforceIf(test1)
        model.Add(NumBlkOfCol2[i] != 0).OnlyEnforceIf(test1.Not())
        #model.Add(ColV3 == i).OnlyEnforceIf(test1)
        model.Add(ColV3 != i).OnlyEnforceIf(test1.Not())
        
        
        test2 = model.NewBoolVar('test2')
        model.Add(NumBlkOfRow2[i] == 0).OnlyEnforceIf(test2)
        model.Add(NumBlkOfRow2[i] != 0).OnlyEnforceIf(test2.Not())
        #model.Add(RowH3 == i).OnlyEnforceIf(test2)
        model.Add(RowH3 != i).OnlyEnforceIf(test2.Not())
    model.Add(RowH3 != 2)    
    solver = cp_model.CpSolver()
    solver.parameters.enumerate_all_solutions = True
    status = solver.Solve(model, solution_printer)    
    
Report2 = []  
CreateNumTypeBlk2(Report)