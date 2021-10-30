import os, sys
import numpy as np
import yaml
import matplotlib.pyplot as plt

def signal(m, x):
    return(m*x)

def noise(a, x):
    return(a*np.random.normal(0,1,x.size))

def init(config_file):
    plt.close('all')
    # Read configuration
    with open(r'%s' % config_file) as file:
        config_list = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    return(config_list)

def plot(y, x, **karg):
    title = karg.pop('title', None)
    fig = plt.figure(1, figsize=(12,6))
    if title:
        fig.canvas.set_window_title(title)
    plt.plot(x,y)
    plt.axhline(0, ls=':')
    ax = plt.gca()
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    plt.show(block=False)
    plt.savefig(title)

def main():
    # Load config
    config = init("config.yml")
    
    start = config['data']['start']
    stop = config['data']['stop']
    step = config['data']['step']

    m = config['parameters']['inclination']
    a = config['parameters']['noise_amplitude']

    x = np.arange(start, stop, step)
    y = signal(m, x)
    y_eps = y + noise(a,x)

    plot(y_eps, x, title=config['experiment'])



if __name__ == "__main__":
    main()