import numpy as np
from scipy import sparse

def solve_naiveGrad(problem, alpha):
    print("** objective types (1=f, 2=sos, 3=ineq, 4=eq): ", problem.getFeatureTypes())
    x = problem.getInitializationSample()
    phi_x, J_x = problem.evaluate(x)
    f_x = np.dot(phi_x, phi_x)
    iter = 0
    while(True):
        #print(problem.report(3))
        #print(np.dot(phi,phi))
        Js = sparse.coo_matrix((J_x[:,2], (J_x[:,0], J_x[:,1])), shape=(phi_x.size, x.size))
        grad = 2*phi_x.T*Js;
        delta = - grad / np.linalg.norm(grad)
        while(True):
            y = x + alpha*delta
            phi_y, J_y = problem.evaluate(y)
            f_y = np.dot(phi_y, phi_y)
            if(f_y > f_x + 0.01*alpha*np.dot(delta, grad)): #reject
                alpha = 0.5 * alpha
            else:
                break

        if (np.linalg.norm(x - y) < 1e-5):
            break

        alpha = 1.2 * alpha
        x=y; phi_x=phi_y; J_x=J_y; f_x=f_y
        iter = iter + 1
        print('it:', iter, ' f_x=', f_x)
        if (iter>=2000):
            break

    return x
