import csv
import numpy as np
from matplotlib import pyplot as plt

############################################
###########  visualize Data ################
############################################
def plot2D(p_X, p_Y,labels):

    plt.plot(p_X, p_Y)
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])
    plt.title(labels[2])

    plt.ylim(np.amin(p_Y), np.amax(p_Y))

    plt.show()

############################################
############## Cost Compute ################
############################################
def computeCost(c_X,c_Y,c_w):
    
    c_J = 0

    c_J = np.sum(np.square(np.dot(c_X,c_w) - c_Y.reshape((c_Y.shape[0],1))))
    c_J = 1 / (2 * m) * c_J

    return c_J


############################################
########### Gradient Descent ###############
############################################
def gradientDescent(g_X, g_Y, g_w, g_eta, g_iters):
    m = len(g_Y)
    J_history = np.zeros((g_iters,1),dtype=float)

    for i in range(g_iters):
        A = np.dot(g_X,g_w) - g_Y.reshape((g_Y.shape[0],1))
        #gradient calculation and stored in delta
        delta = (1/m) * (np.dot(A.T,g_X)).T
        # compute changed values of w 
        g_w = g_w - (eta * delta)

        J_history[i] = computeCost(g_X, g_Y, g_w)
    
    plot2D(list(range(g_iters)),J_history,['Number of Iterations','Cost Function J(w)','Number of Iterations VS Cost Function (J(w))'])    
    return g_w, J_history

############################################
####### Extract values for processing ######
############################################
df = np.genfromtxt('test_O3_final.csv', delimiter=',')
df_pm = np.genfromtxt('test_PM25_final.csv', delimiter=',')
df_so = np.genfromtxt('test_SO2_final.csv', delimiter=',')

df = np.delete(df,0,0)
df_pm = np.delete(df_pm,0,0)
df_so = np.delete(df_so,0,0)

#m is the number of samples 
#D is the number of features, (-1 since the df contains the last column as Y values)
m = df.shape[0]
m_pm = df_pm.shape[0]
m_so = df_so.shape[0]

D = df.shape[1]-1
D_pm = df_pm.shape[1]-1
D_so = df_so.shape[1]-1

#create a separate matix for X and Y data, where 
#X is the features samples (adding a column of ones for bias)
#Y is the output column vector for training
Y = df[:,-1]
Y_pm = df_pm[:,-1]
Y_so = df_so[:,-1]

X = np.ones((m,D+1),dtype=float)
X_pm = np.ones((m_pm,D_pm+1),dtype=float)
X_so = np.ones((m_so,D_so+1),dtype=float)

X[:,1:] = df[:,:9]
X_pm[:,1:] = df_pm[:,:9]
X_so[:,1:] = df_so[:,:9]

###########################################
#########    Gradient Descent   ###########
###########################################
#the w vector that would contained the trained parameters
w = np.zeros((X.shape[1],1),dtype=float)
w_pm = np.zeros((X_pm.shape[1],1),dtype=float)
w_so = np.zeros((X_so.shape[1],1),dtype=float)

#some hyper-paramters
iters = 1000
eta = 0.01

#Gradient descent function
w, J = gradientDescent(X, Y, w, eta, iters)
w_pm, J_pm = gradientDescent(X_pm, Y_pm, w_pm, eta, iters)
w_so, J_so = gradientDescent(X_so, Y_so, w_so, eta, iters)

#Predicting values 
#predict [1.0, hour,altimeter,air_temp, relative_humidity, wind_speed, wind_direction, visibility, dew_point_temp, pressure]
#predicting O3
inp1 = np.array([1.0,0.043,0.41,0.46,0.54,0,0,1,0.92,0.42])
predict1 = np.dot(inp1,w)
inp2 = np.array([1.0,0.52,0.52,0.23,0.82,0,0,1,-1.05,0.52])
predict2 = np.dot(inp2,w)

print("**********************************************")
print("**********************************************")
print("For the inputs inp1: ",inp1)
print("For the inputs inp2: ",inp2)
print("**********************************************")
print("**********************************************")

print("The (1) predicted value of O3 is ",predict1)
print("The (2) predicted value of O3 is ",predict2)

#predicting PM25
inp1 = np.array([1.0,0.043,0.41,0.46,0.54,0,0,1,0.92,0.42])
predict1 = np.dot(inp1,w_pm)
inp2 = np.array([1.0,0.52,0.52,0.23,0.82,0,0,1,-1.05,0.52])
predict2 = np.dot(inp2,w_pm)

print("The (1) predicted value of PM2.5 is ",predict1)
print("The (2) predicted value of PM2.5 is ",predict2)

#predicting SO2
inp1 = np.array([1.0,0.043,0.41,0.46,0.54,0,0,1,0.92,0.42])
predict1 = np.dot(inp1,w_so)
inp2 = np.array([1.0,0.52,0.52,0.23,0.82,0,0,1,-1.05,0.52])
predict2 = np.dot(inp2,w_so)

print("The (1) predicted value of SO2 is ",predict1)
print("The (2) predicted value of SO2 is ",predict2)

