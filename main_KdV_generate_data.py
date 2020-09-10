import sys
import numpy as np
from scipy.fft import rfftfreq, rfft, irfft


class KdVSolverBaseClass():

    def __init__(self, t, x, delta, nSkip=1):
        self.nSkip = nSkip
        self.delta = delta
        self.dt = t[1]-t[0]
        self.t = t
        self.x = x
        self.k = rfftfreq(x.size,d=x[1]-x[0])*2*np.pi
        self._t = []
        self._u = []

    def solve(self, u):
        self._t.append(self.t[0])
        self._u.append(u)
        uk = rfft(u)
        for i in range(1,self.t.size):
           uk = self.singleStep(uk)
           if i%self.nSkip==0:
             self._u.append(irfft(uk))
             self._t.append(self.t[i])
        return np.asarray(self._t), np.asarray(self._u)

    def singleStep(self):
        raise NotImplementedError


class KdVIntegratingFactorSolver(KdVSolverBaseClass):

    def singleStep(self, uk):

        # -- DECLARE CONVENIENT ABBREVIATIONS
        dt, k, delta  = self.dt, self.k, self.delta
        g = 1j*k*k*k*delta*delta

        # -- DERIVATIVE OF AUXILIARY FIELD 
        _dUkdt = lambda dt, uk: -0.5j*k*np.exp(-g*dt)*rfft(irfft(np.exp(g*dt)*uk)**2)

        # -- AUX. FIELD TO ORIGINAL FIELD BACKTRANSFORMATION 
        _a2o = lambda Uk: Uk*np.exp(g*dt)

        # -- 4TH ORDER RK METHOD FOR t-STEPPING AUX FIELD
        def _RK4(uk):
            k1 = _dUkdt(0., uk)
            k2 = _dUkdt(dt/2, uk + dt*k1/2)
            k3 = _dUkdt(dt/2, uk + dt*k2/2)
            k4 = _dUkdt(dt, uk + dt*k3)
            return uk + dt*(k1 + 2*k2 + 2*k3 + k4)/6

        # -- ADVANCE FIELD
        return _a2o(_RK4(uk))


def main_generate_data():

    # -- INITIALIZE SIMULATION PARAMTERS
    xMin, xMax, Nx = 0., 2., 512        # x-domain discretization 
    tMin, tMax, Nt = 0., 6., 30000      # t-domain discretization 
    nSkip = 10                          # step increment for field recording
    delta = 0.022                       # KdV parameter

    # -- INITIALIZE COMPUTATIONAL DOMAIN
    x = np.linspace(xMin, xMax, Nx, endpoint=False)
    t = np.linspace(tMin, tMax, Nt, endpoint=True)

    # -- INITIALIZE SOLVER
    KdVSolver = KdVIntegratingFactorSolver(t, x, delta, nSkip)

    # -- SET INITIAL CONDITION 
    ux0  = np.cos(x*np.pi)

    # -- PROPAGATE FIELD
    _t, uxt = KdVSolver.solve(ux0)

    # -- SAVE RECORDED FIELD
    np.savez_compressed('KdV_raw_data.npz', t=_t, x=x, uxt=uxt, delta=delta)


def main_show_figures():

    # -- INITIALIZE SIMULATION PARAMTERS
    xMin, xMax, Nx = 0., 2., 512        # x-domain discretization 
    tMin, tMax, Nt = 0., 6., 30000      # t-domain discretization 
    nSkip = 10                          # step increment for field recording
    delta = 0.022                       # KdV parameter

    # -- INITIALIZE COMPUTATIONAL DOMAIN
    x = np.linspace(xMin, xMax, Nx, endpoint=False)
    t = np.linspace(tMin, tMax, Nt, endpoint=True)

    # -- INITIALIZE SOLVER
    KdVSolver = KdVIntegratingFactorSolver(t, x, delta, nSkip)

    # -- SET INITIAL CONDITION 
    ux0  = np.cos(x*np.pi)

    # -- PROPAGATE FIELD
    _t, uxt = KdVSolver.solve(ux0)

    # -- DIRECT POSTPROCESSING 
    from pp_figure_02 import generate_figure as pp_fig2
    pp_fig2(x, _t, uxt)



if __name__=="__main__":
    main_generate_data()
    #main_show_figures()

