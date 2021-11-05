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
    x = np.linspace(mean - 4*sigma, mean + 4*sigma, 100)
    return((x,stats.norm.pdf(x, mean, sigma)))
    
def plot_normal(sample, **karg):
    distr = karg.pop('distr', None)
    plt.close('all')
    if not distr:
        plt.hist(sample, color='blue')
    else:
        plt.hist(sample, bins=np.arange(129.5,199.5,1), density=True, color='blue')
        plt.plot(distr[0], distr[1], color='black', ls='--', linewidth=4)
    
    ax = plt.gca()
    ax.set_xlabel("Height (cm)")
    if not distr:
        ax.set_ylabel("Count")
    else:
        ax.set_ylabel("P(height)")
    y_bounds = ax.get_ybound()

    ax.text(190, y_bounds[1]-(y_bounds[1]-y_bounds[0])/10, "n = %d" % sample.size, fontsize='xx-large')

def main():
    # Load config
    config = init("config.yml")
    mean = config['parameters']['mean']
    sigma = config['parameters']['sigma']
    sample_size = config['parameters']['sample_size']
    b_plot_normal = config['normal']

    sample = sample_normal(sample_size, mean=mean, sigma=sigma)
    if b_plot_normal:
        normal_distr = normal(mean=mean, sigma=sigma)
        plot_normal(sample, distr=normal_distr)
    else:
        plot_normal(sample)
    
    plt.show(block=False)

if __name__ == "__main__":
    main()