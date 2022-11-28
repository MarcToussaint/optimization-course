import numpy as np
import sys
sys.path.append('../build')

import libry as ry

def problem_sqr(x):
    y = np.array(x)
    y[0] = y[0] - 1.
    J = np.eye(y.size)
    return y,J

def create_problem1_sosOnly(timeSlices=20):
    C = ry.Config()
    C.addFile('../../rai-robotModels/scenarios/pandasTable.g')
    f = C.addFrame('box','table')
    f.setRelativePosition([0,0,.1])
    f.setShape(ry.ST.sphere, size=[.02])
    f.setColor([1,1,0])
    #C.view()

    komo = ry.KOMO()
    komo.setModel(C, True)
    komo.setTiming(1., timeSlices, 5., 2)
    komo.add_qControlObjective([], 2, 1e-0)
    komo.addObjective([1.], ry.FS.positionDiff, ['r_gripper', 'box'], ry.OT.sos, [1e1]);
    komo.addObjective(times=[1.], feature=ry.FS.qItself, type=ry.OT.sos, scale=[1e2], order=1);
    print(komo.reportProblem())
    nlp = komo.get_nlp()
    return [nlp, komo]

def create_problem2_withConstraints(timeSlices=20):
    C = ry.Config()
    C.addFile('../../rai-robotModels/scenarios/pandasTable.g')
    f = C.addFrame('boxR','table')
    f.setRelativePosition([.15,0,.1])
    f.setShape(ry.ST.sphere, size=[.02])
    f.setColor([1,1,0])
    f = C.addFrame('boxL','table')
    f.setRelativePosition([-.15,0,.1])
    f.setShape(ry.ST.sphere, size=[.02])
    f.setColor([1,1,0])
    #C.view(True)

    komo = ry.KOMO()
    komo.setModel(C, True)
    komo.setTiming(1., timeSlices, 5., 2)
    komo.add_qControlObjective([], 2, 1e-0)
    komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq);
    komo.addObjective([], ry.FS.jointLimits, [], ry.OT.ineq);
    komo.addObjective([1.], ry.FS.positionDiff, ['r_gripper', 'boxL'], ry.OT.eq, [1e1]);
    komo.addObjective([1.], ry.FS.positionDiff, ['l_gripper', 'boxR'], ry.OT.eq, [1e1]);
    komo.addObjective(times=[1.], feature=ry.FS.qItself, type=ry.OT.eq, scale=[1e1], order=1);
    print(komo.reportProblem())
    nlp = komo.get_nlp()
    return [nlp, komo]
