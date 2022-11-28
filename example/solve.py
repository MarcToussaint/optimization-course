import numpy as np
from scipy import sparse

def solve_grad(problem):
    print("** objective types (1=f, 2=sos, 3=ineq, 4=eq): ", problem.getFeatureTypes())
    x = problem.getInitializationSample()
    alpha = 1e-2;

    for i in range(0, 100):
        phi, J = problem.evaluate(x)
        #print(problem.report(3))
        #print(np.dot(phi,phi))
        Js = sparse.coo_matrix((J[:,2], (J[:,0], J[:,1])), shape=(phi.size, x.size))
        y = x - alpha * phi.T*Js #J[0].T

        if (np.linalg.norm(x - y) < 1e-5):
            break;
        x = y

    return x
