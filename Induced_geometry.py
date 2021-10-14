'''
Use:
from Induced_geometry import *
import numpy as np 
from sympy import * 
from sympy.physics.mechanics import *
init_vprinting()
'''

class Induced_geometry:
    
    def __init__(self,g,var):
        self.dimension = len(g)
        self.variables = var
        self.metric_tensor = Matrix(g)
        self.inverse_metric_tensor = self.metric_tensor.inv()
        self.christoffel_symbol = self.__get_christoffel_symbol()
        self.riemann_tensor = self.__get_riemann_tensor() 
        self.ricci_tensor = self.__get_ricci_tensor()
        self.ricci_scalar = self.__get_ricci_scalar()
        self.einstein_tensor = self.__get_einstein_tensor()
                     
    def __get_christoffel_symbol(self):
        n = self.dimension
        G = self.metric_tensor
        Gi = self.inverse_metric_tensor
        var = self.variables
        Γ = np.empty((n,n,n),dtype=object)
        for α in range(n):
            for β in range(n):
                for γ in range(n):
                    Γ[α,β,γ] = 0
                    for δ in range(n):
                        Γ[α,β,γ] = Γ[α,β,γ] + Gi[α,δ] * ( diff(G[δ,γ],var[β]) + diff(G[δ,β],var[γ]) - diff(G[β,γ],var[δ]) ) / 2
                        Γ[α,β,γ] = Γ[α,β,γ].simplify() 
        return Γ
    
    def __get_riemann_tensor(self):
        n = self.dimension
        R_c = np.empty((n,n,n,n),dtype=object)
        Γ = self.christoffel_symbol
        var = self.variables
        for α in range(n):
            for β in range(n):
                for γ in range(n):
                    for δ in range(n):
                        R_c[δ,α,β,γ] = 0
                        for ϵ in range(n):
                            R_c[δ,α,β,γ] = R_c[δ,α,β,γ] + Γ[ϵ,α,γ]*Γ[δ,ϵ,β] - Γ[ϵ,α,β]*Γ[δ,ϵ,γ]                        
                        R_c[δ,α,β,γ] = R_c[δ,α,β,γ] + diff(Γ[δ,α,γ],var[β]) - diff(Γ[δ,α,β],var[γ])
                        R_c[δ,α,β,γ] = R_c[δ,α,β,γ].simplify()
        return R_c        
    
    def __get_ricci_tensor(self):
        n = self.dimension
        R_t = np.empty((n,n),dtype=object)
        R_c = self.riemann_tensor
        for α in range(n):
            for β in range(n):
                R_t[α,β] = 0
                for λ in range(n):
                    R_t[α,β] = R_t[α,β] + R_c[λ,α,λ,β]
                R_t[α,β] = R_t[α,β].simplify()
        return R_t        
    
    def __get_ricci_scalar(self):
        R = 0
        Gi = self.inverse_metric_tensor
        R_t = self.ricci_tensor
        n = self.dimension
        for α in range(n):
            for β in range(n):
                R = R + Gi[α,β]*R_t[α,β]
        return R.simplify()
    
    def __get_einstein_tensor(self):
        n = self.dimension
        R_t = self.ricci_tensor
        R = self.ricci_scalar
        G = self.metric_tensor
        n = self.dimension
        G_t = np.empty((n,n),dtype=object)
        for α in range(n):
            for β in range(n):
                G_t[α,β] = R_t[α,β] - G[α,β]*R/2
                G_t[α,β] = G_t[α,β].simplify()
        return G_t     