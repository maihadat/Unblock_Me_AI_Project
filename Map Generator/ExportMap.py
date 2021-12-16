from ortools.sat.python import cp_model
import numpy as np

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables = variables
        self.__solution_count = 0
    
    def on_solution_callback(self):
        #result = []
        self.__solution_count += 1
        count = 0
        Map = np.zeros([6, 6])
        for i in range(4):
            for block in self.__variables[i]:
                count += 1
                for cell in block:
                    val = self.Value(cell)
                    i, j = Decrypt(val)
                    Map[i, j] = count
        count += 1
        for cell in self.__variables[4]:
            val = self.Value(cell)
            i, j = Decrypt(val)
            Map[i, j] = count
        print(Map)
        
    def solution_count(self):
        return self.__solution_count
    
def Decrypt(val):
    return val // 6, val % 6

def ColRowConstr():
    i = -1
    for col in range(6):
        for j in range(NumBlkOfCol[col]):
            i += 1
            model.AddLinearExpressionInDomain(BlockV2[i][0], cp_model.Domain.FromValues(list(range(col, 6*5 + col + 1, 6))))
    
    i = -1
    for row in range(6):
        for j in range(NumBlkOfRow[row]):
            i += 1
            model.AddLinearExpressionInDomain(BlockH2[i][0], cp_model.Domain.FromValues(list(range(row*6, row*6 + 6, 1))))
        
def BuildBlkV2(v2):
    for i in range(v2):
        BlockV2.append([])
        ModV2.append(model.NewIntVar(0, 5, 'DivV2[%d]' % i))
        BlockV2[i].append(model.NewIntVarFromDomain(cp_model.Domain.FromIntervals([[0, 5], [18, 29]]), 'BlockV2[%d, %d]' % (i, 0)))
        model.AddModuloEquality(ModV2[i], BlockV2[i][0], 6)
        
        for e in range(1, 2):
            BlockV2[i].append(model.NewIntVar(0, 35, 'BlockV2[%d, %d]'% (i, e)))
            model.AddModuloEquality(ModV2[i], BlockV2[i][e], 6)
        for e in range(1):
            model.Add(BlockV2[i][e] + 6 == BlockV2[i][e + 1])

def BuildBlkV3(v3):
    for i in range(v3):
        BlockV3.append([])
        ModV3.append(model.NewIntVar(0, 5, 'ModH3[%d]' % i))
        BlockV3[i].append(model.NewIntVar(0, 35, 'BlockV3[%d, %d]'% (i, 0)))
        model.Add(BlockV3[i][0] == 3 * 6 + ColV3)
        #BlockV3[i].append(model.NewIntVar(3 * 6 + ColV3,3 * 6 + ColV3, 'BlockV3[%d, %d]' % (i, 0)))
        
        for e in range(1, 3):
            BlockV3[i].append(model.NewIntVar(0, 35, 'BlockV3[%d, %d]'% (i, e)))
            model.AddModuloEquality(ModV3[i], BlockV3[i][e], 6)
        
        for e in range(2):
            model.Add(BlockV3[i][e] + 6 == BlockV3[i][e + 1]) 
            
def BuildBlkH2(h2):
    for i in range(h2):
        BlockH2.append([])
        DivH2.append(model.NewIntVar(0, 5, 'DivH2[%d]' % i))
        BlockH2[i].append(model.NewIntVarFromDomain(cp_model.Domain.FromIntervals([[0, 4], [6, 10], [18, 22], [24, 28], [30, 34]]), 'BlockH2[%d, %d]' % (i, 0)))
        model.AddDivisionEquality(DivH2[i], BlockH2[i][0], 6)
        
        for e in range(1, 2):
            BlockH2[i].append(model.NewIntVar(0, 35, 'BlockH2[%d, %d]'% (i, e)))
            model.AddDivisionEquality(DivH2[i], BlockH2[i][e], 6)
            
        for e in range(1):
            model.Add(BlockH2[i][e] + 1 == BlockH2[i][e + 1])
            
def BuildBlkH3(h3):
    for i in range(h3):
        BlockH3.append([])
        DivH3.append(model.NewIntVar(0, 5, 'DivH3[%d]' % i))
        #BlockH3[i].append(model.NewIntVar(0, 35, 'BlockH3[%d, %d]'% (i, 0)))
        BlockH3[i].append(model.NewIntVarFromDomain(cp_model.Domain.FromIntervals([list(range(RowH3*6 + 3, RowH3*6 + 5, 1))]), 'BlockH3[%d, %d]' % (i, 0)))
        model.AddDivisionEquality(DivH3[i], BlockH3[i][0], 6)
        
        for e in range(1, 3):
            BlockH3[i].append(model.NewIntVar(0, 35, 'BlockH3[%d, %d]'% (i, e)))
            model.AddDivisionEquality(DivH3[i], BlockH3[i][e], 6)
            
        for e in range(2):
            model.Add(BlockH3[i][e] + 1 == BlockH3[i][e + 1])

def BuildMainBlk():
    for e in range(2):
        MainBlk.append(model.NewIntVar(12, 13, 'MainBlk[%d]' % e))
    for e in range(1):
        model.Add(MainBlk[e] + 1 == MainBlk[e + 1])           

def AllDifConstr():
    for Block in BlockV2:
        for var in Block:
            AllVar.append(var)
    
    for Block in BlockV3:
        for var in Block:
            AllVar.append(var)
    
    for Block in BlockH2:
        for var in Block:
            AllVar.append(var)
    
    for Block in BlockH3:
        for var in Block:
            AllVar.append(var)
            
    for cell in MainBlk:
        AllVar.append(cell)
    
    model.AddAllDifferent(AllVar)
    
def SolvableConstr1():
    for i in range(v3):
        model.Add(18 <= BlockV3[i][0])
        model.Add(BlockV3[i][0] <= 23)    
    
def Print1Result():
    Map = np.zeros((6,6))
    count = 0
    status = solver.Solve(model)
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        for var in BlockV2:
            count += 1
            for value in var:
                val = solver.Value(value)
                i, j = Decrypt(val) 
                Map[i, j] = count
        
        for var in BlockV3:
            count += 1
            for value in var:
                val = solver.Value(value)
                i, j = Decrypt(val)
                Map[i, j] = count

        for var in BlockH2:
            count += 1
            for value in var:
                val = solver.Value(value)
                i, j = Decrypt(val)
                Map[i, j] = count
                
        for var in BlockH3:
            count += 1
            for value in var:
                val = solver.Value(value)
                i, j = Decrypt(val) 
                Map[i, j] = count

        count += 1
        for value in MainBlk:
            val = solver.Value(value)
            i, j = Decrypt(val) 
            Map[i, j] = count
        print(str(Map))
        
def GenAllMap():
    solution_printer = VarArraySolutionPrinter([BlockV2, BlockV3, BlockH2, BlockH3, MainBlk])
    solver.parameters.enumerate_all_solutions = True
    status = solver.Solve(model, solution_printer)

v2, v3, h2, h3, _ = Report[0]

for report in Report2:
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()
    
    BlockV2 = []
    BlockV3 = []
    BlockH2 = []
    BlockH3 = []
    MainBlk = []

    ModV2 = []
    ModV3 = []
    DivH2 = []
    DivH3 = []
    AllVar = []
    ColV3, RowH3 = report[2], report[3]
    
    #BlkConstr(v2, v3, h2, h3, ColV3, RowH3)
    NumBlkOfCol, NumBlkOfRow = report[0], report[1]
                      
    BuildBlkV2(v2)
    BuildBlkV3(v3)
    BuildBlkH2(h2)  
    BuildBlkH3(h3)               
    BuildMainBlk()

    AllDifConstr()
    ColRowConstr()
    SolvableConstr1()
    Print1Result()
    
#GenAllMap()