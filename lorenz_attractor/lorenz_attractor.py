import sys, os
import numpy as np
import yaml
import matplotlib.pyplot as plt


def init(config_file):
    plt.close('all')
    # Read configuration
    with open(r'%s' % config_file) as file:
        config_list = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    return(config_list)

def lorenz_attractor(**karg):
    initial_position = karg.pop('init', np.array((1,1,1)))
    time_step = karg.pop('step', 0.01)
    sigma = karg.pop('sigma', 11)
    rho = karg.pop('rho', 28)
    beta = karg.pop('beta', 5/3.)

    X = initial_position[0]
    Y = initial_position[1]
    Z = initial_position[2]
    # Equations
    dX = sigma * (Y - X)
    dY = X * (rho - Z) - Y
    dZ = X*Y - beta*Z

    dr = np.array((dX, dY, dZ))
    return(initial_position+dr*time_step)
    
def plot_lorenz_attractor(pos, **karg):
    title = karg.pop('title', None)

    plt.close('all')
    fig = plt.figure(1, figsize=(12,8))
    fig.canvas.set_window_title("%s" % title)

    ax = plt.gca()
    

def main():
    # Load config
    config = init("config.yml")
    sigma = config['parameters']['sigma']
    rho = config['parameters']['rho']
    beta = config['parameters']['beta']
    
    initial_position = config['initial_condition']['position']
    time_step = config['time_control']['step']
    time_stop = config['time_control']['stop']

    pos = initial_position
    print(0, pos)

    for time in np.arange(1,time_stop):
        pos = lorenz_attractor(init=pos,time_step=time_step,sigma=sigma,rho=rho,beta=beta)
        print(time, pos)
    
    #plt.show(block=False)
    #plt.savefig(config['experiment'])

if __name__ == "__main__":
    main()