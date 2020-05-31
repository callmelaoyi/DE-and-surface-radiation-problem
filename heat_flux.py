import numpy as np

class J(object):
    def __init__(self, t1,t2, t3, 
                epsilon1, epsilon2, epsilon3,
                r_divide = 20, l_divide = 70, longth=4):
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.epsilon1 = epsilon1
        self.epsilon2 = epsilon2
        self.epsilon3 = epsilon3
        self.r_divide = r_divide
        self.l_divide = l_divide
        self.longth = longth
        self.r = 1
        # 角系数矩阵初始化
        self.X12 = self.x12()
        self.X13 = self.x13()
        self.X21 = self.x21()
        self.X22 = self.x22()
        self.X23 = self.x21()
        self.X32 = self.x12()
        self.X31 = self.x13()


    def solve(self):
        J1 = np.zeros((self.r_divide, 1))
        J2 = np.zeros((self.l_divide, 1))
        J3 = np.zeros((self.r_divide, 1))
        
        # self.J1 = J1
        # self.J2 = J2
        # self.J3 = J3
        while not self.test(J1, J2, J3):
            J1, J2, J3 = self.update(J1, J2, J3)
        return J1, J2, J3

    def test(self, J1, J2, J3):
        # J 误差
        J2_next= self.update(J1, J2, J3)[1]
        isEq = abs(J2[self.l_divide//2] - J2_next[self.l_divide//2])
        return isEq < 1e-4

    
    def update(self, J1, J2, J3):
        J1_next = self.epsilon1*self.t1**4                                          + (1-self.epsilon1)*np.dot(self.X12, J2) + (1-self.epsilon1)*np.dot(self.X13, J3)
        J2_next = self.epsilon2*self.t2**4 + (1-self.epsilon2)*np.dot(self.X21, J1) + (1-self.epsilon2)*np.dot(self.X22, J2) + (1-self.epsilon2)*np.dot(self.X23, J3)
        J3_next = self.epsilon3*self.t3**4 + (1-self.epsilon3)*np.dot(self.X31, J1) + (1-self.epsilon3)*np.dot(self.X32, J2)
        return J1_next, J2_next, J3_next
    
    def x12(self):
        # x12 是一个 20*70 的矩阵
        X12 = np.zeros((self.r_divide, self.l_divide))
        for i in range(self.r_divide):
            for j in range(self.l_divide):
                r = (i+1)/self.r_divide
                l = self.longth*(j+1)/self.l_divide
                X12[i][j] = 8*l*(4*l**2+r**2-1)/((4*l**2+r**2+1)**2-4*r**2)**1.5
        X12 = X12*self.longth/self.l_divide
        return X12


    def x13(self):
        X13 = np.zeros((self.r_divide, self.r_divide))
        for i in range(self.r_divide):
            for j in range(self.r_divide):
                r1 = (i+1)/self.r_divide
                r3 = (j+1)/self.r_divide
                R = r3/r1
                l = 2*self.longth/r1
                X13[i][j] = (1/r1)*(2*R*l**2*(l**2+R**2+1))/((l**2+R**2+1)**2-4*R**2)**1.5
        X13 = X13/self.r_divide
        return X13
    

    def x21(self):
        X21 = np.zeros((self.l_divide, self.r_divide))
        for i in range(self.l_divide):
            for j in range(self.r_divide):
                l = self.longth*(i+1)/self.l_divide
                r = (j+1)/self.r_divide
                X21[i][j] = 4*l*(4*l**2+r**2-1)*r/((4*l**2+r**2+1)**2-4*r**2)**1.5
        X21 = X21/self.r_divide
        return X21
    
    def x22(self):
        X22 = np.zeros((self.l_divide, self.l_divide))
        for i in range(self.l_divide):
            for j in range(self.l_divide):
                x = self.longth*(i+1)/self.l_divide
                y = self.longth*(j+1)/self.l_divide
                a = abs(x-y)
                X22[i][j] = 1 - a*((2*a**2)+3)/(a**2+1)**1.5/2
        X22 = X22*self.longth/self.l_divide
        return X22


def heat_flux_solve(t1=0.5, t2=1, t3=0.5,
                    epsilon1=0.9, epsilon2=0.9, epsilon3= 0.9,
                    r_divide=20, l_divide=70):
    # 求 角系数矩阵
    J1, J2, J3 = J(t1, t2, t3, epsilon1, epsilon2, epsilon3,
                   r_divide,  l_divide).solve()
    Q1 = (epsilon1/(1-epsilon1))*(t1**4-J1)
    Q2 = (epsilon2/(1-epsilon2))*(t2**4-J2)
    Q3 = (epsilon3/(1-epsilon3))*(t3**4-J3)
    return Q1, Q2, Q3






if __name__ == "__main__":
    
    hf1=heat_flux_solve(t1=0.5, t2=1, t3=0.5,
                    epsilon1=0.9, epsilon2=0.9, epsilon3= 0.9,
                    r_divide=20, l_divide=30)[1]
    hf2=heat_flux_solve(t1=0.5, t2=1, t3=0.5,
                    epsilon1=0.9, epsilon2=0.9, epsilon3= 0.9,
                    r_divide=20, l_divide=50)[1]
    hf3=heat_flux_solve(t1=0.5, t2=1, t3=0.5,
                    epsilon1=0.9, epsilon2=0.9, epsilon3= 0.9,
                    r_divide=20, l_divide=70)[1]
    hf4=heat_flux_solve(t1=0.5, t2=1, t3=0.5,
                    epsilon1=0.9, epsilon2=0.9, epsilon3= 0.9,
                    r_divide=20, l_divide=90)[1]
    hf5=heat_flux_solve(t1=0.5, t2=1, t3=0.5,
                    epsilon1=0.9, epsilon2=0.9, epsilon3= 0.9,
                    r_divide=20, l_divide=150)[1]
    
    



'''
def J_solve(t1, t2, t3, epsilon1, 
            epsilon2, epsilon3,
            r_divide = 20, l_divide = 70):
    J1 = np.zeros((r_divide, 1))
    J2 = np.zeros((l_divide, 1))
    J3 = np.zeros((r_divide, 1))
    while not J_test(J1, J2, J3):
        J1, J2, J3 = J_update(J1, J2, J3)
    return J1, J2, J3


def J_test(J1, J2, J3):
    pass

def J_update(J1, J2, J3):
    pass
'''



