import numpy as np
import matplotlib.pyplot as plt
'''
def which_data_set():
    ip = input('What is your student No.? ')
    tmp = 0
    for c in ip:
        tmp += int(c)
    return tmp%5 + 1
'''
''' code for determining the dataset that a student should use in lab task 2.'''

def readfile(filename): # used to read the file and return the data in the file as an array
    with open(filename) as f:
        lines=f.readlines()
    length=len(lines)
    arr=np.zeros(length) # create an array whose length equals to the number of data in the file to store the data
    num=0
    for line in lines:
        arr[num]= line.rstrip() # wipe off the '\n' in the end of each line
        '''print(line)'''
        num+=1 # move to the next position of the array
    return arr

def cost(a2,a3,data):
    return sum(np.power(data[3:]-(a2*data[1:length-2]+a3*data[:length-3]),2)) #Based on the derived formula, calculate the cost
'''
dataset=which_data_set()
print("The dataset used should be dataset {}.".format(dataset))
'''#code to print the dataset to be used
a=readfile('eie2108-lab-2021-datafile-04.txt') # use an array called a to store the data in the file
length=len(a)
'''
print(a)
print(length)
'''
a2=1 # set the initial value of the parameter a2
a3=-1 # set the initial value of the parameter a3
alpha=0.0001 # set the learning rate
threshold=0.001 # set the threshold for early termination
max_no_of_iter=1000 # set the maximum number of iterations
iterations=1000 # used to store how many interations are actually done
rec_J=np.zeros(max_no_of_iter) # create an array to store cost J of each iteration
rec_a2_a3=np.zeros([max_no_of_iter,2]) # create an array to store the values of a2 and a3 of each iteration
J=cost(a2,a3,a) # calculate the initial cost
rec_J[0]=J # give the cost J to the first item in rec_J
rec_a2_a3[0,:]=[a2,a3] # give the initial values of a2,a3 to the column 0 and column 1 of the row 0  
for i in range(1,max_no_of_iter):
    temp=a[3:]-a3*a[:length-3]-a2*a[1:length-2] # By deriving the formula, we find that the update formula of both a2 and a3 have this same term
    a2-=alpha*sum(-2*a[1:length-2]*temp) # update a2
    a3-=alpha*sum(-2*a[:length-3]*temp) # update a3
    J=cost(a2,a3,a) # calculate the cost J of this iteration
    rec_J[i]=J # store the cost
    rec_a2_a3[i,:]=[a2,a3] # store the updated a2 and a3
    print('After iter '+str(i+1)+' cost J is '+str(J)+' for [a2,a3]=' +str([a2,a3])) # print the updating information
    if(rec_J[i-1]-rec_J[i]<threshold): #if the difference of the updated cost and the cost of the last iteration is less than the threshold
        iterations=i+1 # update the actual iteration times
        break # stop the iteration
        
# fig1 is used to show how J converges to the minimum using the gradient descent method
fig1, ax1=plt.subplots() 
ax1.plot(range(iterations),rec_J[:iterations],color='red',linewidth=2,label='cost J') # We should use the actual iteration times rather than the maximum of the iteration times
ax1.set_xlabel('iter i')
ax1.set_ylabel('J')
ax1.set_title('Cost J @ iter i')
ax1.grid()
fig1
# fig2 is used to show how a2 and a3 converge
fig2,ax2=plt.subplots()
ax2.plot(range(iterations),rec_a2_a3[:iterations,0],color='red',linewidth=2,label='a2')
ax2.plot(range(iterations),rec_a2_a3[:iterations,1],color='green',linewidth=2,label='a3')
ax2.set_xlabel('iter i')
ax2.set_title('a2 and a3 @ iter i')
ax2.grid()
ax2.legend()
fig2




