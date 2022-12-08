import sys
sys.path.append('../../optimization_algorithms/')
#sys.path.append('../build')

#import libry as ry
from robotic import ry
from problems import *
from solve import *
#from optalg.interface.nlp_traced import NLPTraced

#-- four benchmarks so far:
#[nlp, komo] = create_problem1_sosOnly(20)
#[nlp, komo] = create_problem2_withConstraints(20)
[nlp, komo] = create_problem3_handoverSkeleton(1)
#[nlp, komo] = create_problem3_handoverSkeleton(10)

#-- naive grad doesn't really work
#solve_naiveGrad(nlp, alpha = 1e-2)
#komo.view(True)
#komo.view_play(True, .2)

#-- solver (AugLag) implemented in rai
sol = ry.NLP_Solver()
sol.setProblem(nlp)
sol.setOptions( stopTolerance=1e-2 )
print('[main] solver options:', sol.getOptions().dict())
ret = sol.solve()
print('[main]', ret)
#print(sol.getTrace_costs(), sol.getTrace_x())

#-- display results
#print(nlp.report(2))
komo.view(True)
komo.view_play(True, .2)
