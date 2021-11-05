import sys, os
import numpy as np
import scipy.stats as stats
import yaml
import matplotlib.pyplot as plt


def init(config_file):
    plt.close('all')
    # Read configuration
    with open(r'%s' % config_file) as file:
        config_list = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    return(config_list)

def sample_normal(n_samples, **karg):
    seed = karg.pop('seed', 21)
    mean = karg.pop('mean', 0)
    sigma = karg.pop('sigma', 1)
    np.random.seed(seed)
    return(np.random.normal(mean, sigma, n_samples))

def normal(**karg):
    mean = karg.pop('mean', 0)
    sigma = karg.pop('sigma', 1)
    x = np.linspace(mean - 3*sigma, mean + 3*sigma, 100)
    return((x,stats.norm.pdf(x, mean, sigma)))
    
def plot_normal(sample, **karg):
    distr = karg.pop('distr', None)
    plt.close('all')
    if not distr:
        plt.hist(sample, color='blue')
    else:
        plt.hist(sample, density=True, color='blue')
        plt.plot(distr[0], distr[1], color='black', ls='--')
    
    ax = plt.gca()
    ax.set_xlabel("Height (cm)")

    if not distr:
        ax.set_ylabel("Count")
    else:
        ax.set_ylabel("P(height)")

def main():
    mean = 165
    sigma = 7.5
    sample_size = 1000
    sample = sample_normal(sample_size, mean=mean, sigma=sigma)
    normal_distr = normal(mean=mean, sigma=sigma)
    plot_normal(sample, distr=normal_distr)
    
    plt.show(block=False)

if __name__ == "__main__":
    main()