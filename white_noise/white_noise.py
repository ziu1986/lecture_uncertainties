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
    
def plot_fit(fit, **karg):
    start = karg.pop('start', 0)
    stop = karg.pop('stop', 20)

    ax = plt.gca()
    fit_x = (start, stop)
    fit_y = [ fit(each) for each in fit_x]

    ax.plot(fit_x, fit_y, color='blue')

    ax.text(ax.get_xbound()[0]+2, ax.get_ybound()[1]-2, "$f(x) = m*x + b$", color='blue', size='xx-large')
    plt.show(block=False)


def fitting(y, x, **karg):
    window = karg.pop('window', None)

    fit = np.polyfit(x, y, 1)
    print("Fitting: f(x) = m * x + b")
    print("Result: m = %2.2f; b = %2.2f" % (fit[0], fit[1]))
    return(fit)

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

    if config['fit']:
        fit = np.poly1d(fitting(y, x))
        plot_fit(fit)
        
    plt.savefig(config['experiment']) 

if __name__ == "__main__":
    main()