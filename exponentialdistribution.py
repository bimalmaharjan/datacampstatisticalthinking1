import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import empiricalcumulativedistribution as ecdf

def successive_poisson(tau1, tau2, size=1):
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(tau1, size)

    # Draw samples out of second exponential distribution: t2
    t2 = np.random.exponential(tau2, size)

    return t1 + t2


 # Draw samples of waiting times: waiting_times
waiting_times = successive_poisson(764,715, 100000)


# Make the histogram

_ = plt.hist(waiting_times,bins=100,normed=True, histtype='step') 



# Label axes
_ = plt.xlabel('waiting_times')
_ = plt.ylabel('probability ')

# plot ecdf

x,y = ecdf.ecdf(waiting_times)
_ = plt.plot(x,y, marker='.',linestyle='none')
_ = plt.xlabel('waitng times')
_ = plt.ylabel('probability of waiting times')



# Show the plot

plt.show()