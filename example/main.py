import sys
sys.path.append("../../optimization_algorithms/")
sys.path.append('../build')

from problems import *
from solve import solve_grad
from optalg.interface.nlp_traced import NLPTraced
import libry as ry

#[nlp, komo] = create_problem1_sosOnly(20)
[nlp, komo] = create_problem2_withConstraints(20)
problem = NLPTraced(nlp)

#x = solve_grad(problem)

sol = ry.NLP_Solver()
sol.setProblem(nlp) #can't yet take python-created problem..
sol.setOptions( sol.getOptions() .set_stopTolerance(1e-1) .set_stopGTolerance(1e-2) )
print(sol.getOptions().dict())
sol.solve()
#print(sol.getTrace_costs(), sol.getTrace_x())

print(nlp.report(2))
komo.view(True)
komo.view_play(True, .2)