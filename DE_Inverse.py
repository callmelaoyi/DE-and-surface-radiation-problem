import heat_flux
from sko.DE import DE
# from sko.DE_ori import DE_ori
import numpy as np
import pandas as pd
from sko.DE_gai import DE_gai


Q_real = heat_flux.heat_flux_solve()

# 温度实验迭代
def obj_func(x):
    Q_et = heat_flux.heat_flux_solve(x[0], 1, x[1])
    shiyingdu0 = np.sum(np.square(Q_et[0]-Q_real[0]))
    shiyingdu1 = np.sum(np.square(Q_et[1]-Q_real[1]))
    shiyingdu2 = np.sum(np.square(Q_et[2]-Q_real[2]))
    shiyingdu = shiyingdu0 + shiyingdu1 + shiyingdu2
    return shiyingdu


def temprature_main():
    t1_generation = []
    t3_generation = []
    for i in range(9):
        F = 0.1*(i+1)
        de = DE(func=obj_func, n_dim=2, size_pop=100, max_iter=100, lb=[0, 0 ],
                ub=[1, 1], F = F)
        best_x, best_y, t_best = de.run()
        
            
        print('best_x:', best_x, '\n', 'best_y:', best_y)
        Q_best = heat_flux.heat_flux_solve(best_x[0], 1, best_x[1])[1]
        t1_generation.append(t_best[:,0])
        t3_generation.append(t_best[:,1])
        df = pd.DataFrame(best_x)
        df.to_csv('/biyesheji/交叉因子为'+str(F)+'.csv')
    save_t1 = pd.DataFrame(t1_generation)
    save_t3 = pd.DataFrame(t3_generation)
    save_t1.to_csv('/biyesheji/t1_data.csv')
    save_t3.to_csv('/biyesheji/t3_data.csv')


# 发射率和温度实验
def obj_func2(x):
    Q_et = heat_flux.heat_flux_solve(x[0], 1, x[1], x[2],0.9,x[3])
    shiyingdu0 = np.sum(np.square(Q_et[0]-Q_real[0]))
    shiyingdu1 = np.sum(np.square(Q_et[1]-Q_real[1]))
    shiyingdu2 = np.sum(np.square(Q_et[2]-Q_real[2]))
    shiyingdu = shiyingdu0 + shiyingdu1 + shiyingdu2
    return shiyingdu

# 表面1和3温度、   表面2 发射率实验
def obj_func3(x):
    Q_et = heat_flux.heat_flux_solve(x[0], 1, x[1], 0.9,x[2],0.9)
    shiyingdu0 = np.sum(np.square(Q_et[0]-Q_real[0]))
    shiyingdu1 = np.sum(np.square(Q_et[1]-Q_real[1]))
    shiyingdu2 = np.sum(np.square(Q_et[2]-Q_real[2]))
    shiyingdu = shiyingdu0 + shiyingdu1 + shiyingdu2
    return shiyingdu


ze2 = (obj_func3([0.5,0.5,0.901])-obj_func3([0.5,0.5,0.9]))/0.001
'''
# 温度发射率都估计的实验
de = DE(func=obj_func2, n_dim=4, size_pop=40, max_iter=5, lb=[0, 0 , 0, 0],
            ub=[1, 1, 1, 1])
best_x, best_y, t_best = de.run()
print(best_x)
'''

'''
# 表面温度估计实验
temperature1_lab ={}
temperature3_lab ={}
temperaturey_lab ={}
for i in range(3):
    de = DE(func=obj_func, n_dim=2, size_pop=20, max_iter=100, lb=[0, 0 ],
            ub=[1, 1])
    best_x, best_y, x_best_mat, all_history_bestY = de.run()
    x1_best_mat = []
    x3_best_mat = []
    for j in range(len(x_best_mat)):
        x1_best_mat.append(x_best_mat[j][0])
        x3_best_mat.append(x_best_mat[j][1])
    temperature1_lab["第"+str(i)+"次实验"] = x1_best_mat
    temperature1_lab["第"+str(i)+"次实验"] = x3_best_mat
    temperaturey_lab["第"+str(i)+"次实验"] = all_history_bestY
tem1_lab_data = pd.DataFrame(temperature1_lab)
tem1_lab_data.to_csv('/biyesheji/tem1_lab_data.csv')
tem3_lab_data = pd.DataFrame(temperature3_lab)
tem3_lab_data.to_csv('/biyesheji/tem3_lab_data.csv')
temy_lab_data = pd.DataFrame(temperaturey_lab)
temy_lab_data.to_csv('/biyesheji/temy_lab_data.csv')
'''
'''
t1=[]
t3=[]
e1=[]
e3=[]
lab={}
de = DE(func=obj_func2, n_dim=4, size_pop=40, max_iter=3, lb=[0, 0 , 0, 0],
            ub=[1, 1, 1, 1])
best_x, best_y,x_best_mat, all_history_bestY = de.run()
for j in range(len(x_best_mat)):
    t1.append(x_best_mat[j][0])
    t3.append(x_best_mat[j][1])
    e1.append(x_best_mat[j][2])
    e3.append(x_best_mat[j][3])
lab['t1']=t1
lab['t3']=t3
lab['e1']=e1
lab['e3']=e3

lab_data = pd.DataFrame(lab)
lab_data.to_csv("/biyesheji/4_2lab.csv")
'''

'''
zt1= (obj_func2([0.501,0.5,0.9,0.9])-obj_func2([0.5,0.5,0.9,0.9]))/0.001
zt3= (obj_func2([0.5,0.501,0.9,0.9])-obj_func2([0.5,0.5,0.9,0.9]))/0.001
ze1= (obj_func2([0.5,0.5,0.901,0.9])-obj_func2([0.5,0.5,0.9,0.9]))/0.001
ze3= (obj_func2([0.5,0.5,0.9,0.901])-obj_func2([0.5,0.5,0.9,0.9]))/0.001
'''
'''

t1=[]
t3=[]
# e1=[]
e2=[]
lab={}
de = DE(func=obj_func3, n_dim=3, size_pop=30, max_iter=5, lb=[0, 0, 0],
            ub=[1, 1, 1])
best_x, best_y,x_best_mat, all_history_bestY = de.run()
for j in range(len(x_best_mat)):
    t1.append(x_best_mat[j][0])
    t3.append(x_best_mat[j][1])
    e2.append(x_best_mat[j][2])
    # e3.append(x_best_mat[j][3])
lab['t1']=t1
lab['t3']=t3
lab['e2']=e2
# lab['e3']=e3
lab['best fitness']= all_history_bestY

lab_data = pd.DataFrame(lab)
lab_data.to_csv("/biyesheji/4_2lab.csv")
'''

def lab4_4(F):
    t1=[]
    t3=[]
    lab={}
    de = DE(func=obj_func, n_dim=2, size_pop=20, max_iter=5, lb=[0, 0],
            ub=[1, 1],F=F)
    best_x, best_y,x_best_mat, all_history_bestY = de.run()
    for j in range(len(x_best_mat)):
        t1.append(x_best_mat[j][0])
        t3.append(x_best_mat[j][1])
        lab['t1']=t1
        lab['t3']=t3
    lab['best fitness']= all_history_bestY
    lab_data = pd.DataFrame(lab)
    lab_data.to_csv("/biyesheji/4_3lab_F="+str(F)+".csv")

    return 0




def lab4_4_2(F):
    t1=[]
    t3=[]
    # e1=[]
    e2=[]
    lab={}
    de = DE_gai(func=obj_func3, n_dim=3, size_pop=30, max_iter=5, lb=[0, 0, 0],
                ub=[1, 1, 1], F=F)
    best_x, best_y,x_best_mat, all_history_bestY = de.run()
    for j in range(len(x_best_mat)):
        t1.append(x_best_mat[j][0])
        t3.append(x_best_mat[j][1])
        e2.append(x_best_mat[j][2])
        # e3.append(x_best_mat[j][3])
    lab['t1']=t1
    lab['t3']=t3
    lab['e2']=e2
    # lab['e3']=e3
    lab['best fitness']= all_history_bestY
    
    lab_data = pd.DataFrame(lab)
    lab_data.to_csv("/biyesheji/4_3lab_F="+str(F)+".csv")
    return 0

lab4_4_2(0.3)







