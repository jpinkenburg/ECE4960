# RUN ME
# This file gives the initial condition to the scipy.integrat.odeint function 
# and plots the resulting state outputs at each time step in an animation and
# on a plot that compares the actual output with the reference input

import numpy as np
import sys
sys.path.append('..')  # add parent directory
import matplotlib.pyplot as plt
import control
import pendulumParam as P
from kalmanFilter import kalmanFilter
from pendulumNonlinearDynamics import Pendulum
from pendulumAnimation import pendulumAn
from plotDataZ_Kirstin import plotData      
from signalGenerator import signalGen
import scipy

#Compute controller - change to LQR
dpoles = np.array([-1.1,-1.2,-1.3,-1.4])
Kr = control.place(P.A,P.B,dpoles) # c h a n g e  t o  L Q R

Q = np.matrix([
	[10,0.0,0.0,0.0],
	[0.0,1,0.0,0.0],
	[0.0,0.0,10,0.0],
	[0.0,0.0,0.0,100]
])
R = np.matrix([1])
S = scipy.linalg.solve_continuous_are(P.A,P.B,Q,R)
Kr = np.linalg.inv(R).dot(P.B.transpose().dot(S))

#Initialize and rename for convenience
ref = signalGen(amplitude=0.5, frequency=0.05, y_offset=0) 
pendulum = Pendulum(param=P)

states = [np.array([[P.z0], [P.zdot0], [P.theta0], [P.thetadot0]])]
states_est = [np.array([states[0][0],states[0][1],states[0][2],states[0][3]])]

states_uncertainty = [[0,0,0,0]]
mu = np.array([[P.z0+0.18], [P.zdot0+0.18], [P.theta0+0.075], [P.thetadot0+0.075]])
sigma = np.eye(4)*0.00001
u=0

#performs very simple first order integration 
length = int((P.t_end-P.t_start)/P.Ts)              #The number of time steps over the time interval
t_array = np.linspace(P.t_start, P.t_end, length)   #The time vector for integration.
dt=t_array[1] - t_array[0]

maxForce = (P.m2+P.m1)*3.8 #F=ma
minForce = 0.1
maxVel = 2.7
minVel = 0.1

print(maxForce)

for t in t_array[:-1]:
    des_state = np.array([[ref.sawtooth(t)[0]], [0.0], [0.0], [0.0]])
    old_state=states[-1]

    #Update controller and sensors every <T_update> seconds
    if (t % P.T_update) < dt:
        u=-Kr.dot(mu-des_state) #change to LQR

        if abs(u) > maxForce:
            u = np.sign(u)*maxForce
        elif abs(u) < minForce:
            u = 0

        y_kf = P.C.dot(old_state) + np.random.normal(0,0.01)
        mu,sigma = kalmanFilter(mu,sigma,u,y_kf)
    
    new_state=old_state + np.array(pendulum.cartpendfunc(old_state,u)) * dt

    #Arrays for debugging
    states_est.append(mu)
    states.append(new_state)
    states_uncertainty.append([sigma[0,0],sigma[1,1],sigma[2,2],sigma[3,3]])
states_uncertainty = np.array(states_uncertainty)
#print(states_uncertainty[1000])
#print(np.array(states_uncertainty).shape)

#Plot state uncertainty values
'''
sdPlot = plotData()
sdPlot.plot_uncertainty(t_array,states_uncertainty)
input()
'''
#animation
plt.close('all')
animation = pendulumAn()

#Recast arrays for plotting
states = np.array(states)
states_est = np.array(states_est)
print(states_est.shape)

i = 0
reference = np.zeros((length,1))
while i < len(t_array):  
    #calculate the reference value
    t_curr = t_array[i]                 #Current time step
    z_ref = ref.sawtooth(t_curr)          #Get cart z location
    reference[i:(i+100)] = z_ref        #Which reference value is used

    #update animation and data plots
    animation.drawPendulum(states[i,:]) #Animate
    plt.pause(0.001)                    #Pause while plot updates
    i = i + 100                         #speeds up the simulation by not plotting all the points
 

# Plot how closely the actual performance of the pendulum on a cart matched the desired performance
dataPlot = plotData()                       #initializes plot
dataPlot.Plot(t_array, reference, states_est, 1) #plot the estimate
dataPlot.Plot(t_array, reference, states, 1) #plot the estimate
#dataPlot2 = plotData('Estimated State Values') #initializes plot
#dataPlot2.Plot(t_array, reference, states, 1,'r','g')     #plots the data
plt.show()
input()
