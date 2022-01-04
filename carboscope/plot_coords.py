import os, sys, glob
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def read_data(src):

    data = {}
    for each in sorted(glob.glob(src+'/*')):
        key = each[-9:-2]
        data.update({key:pd.read_table(each, delim_whitespace=True, comment = '#', names = ['code', 'lat', 'lon', 'height'])})

    return(data)

def plot(data):
    plt.close('all')

    keys = data.keys()
    title = "jena_carboscope"

    print(keys)

    fig = plt.figure(figsize=(16, 8))
    fig.canvas.manager.set_window_title(title)
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())

    # make the map global rather than have it zoom in to
    # the extents of any plotted data
    ax.set_global()

    ax.coastlines()

    for key, marker, color, size in zip(keys, ['s','o','^'], ['blue','black', 'red'], [12,9,7]):
        ax.plot(data[key]['lon'], data[key]['lat'], marker, color=color, ms=size, transform=ccrs.PlateCarree(), label=key)

    plt.legend()
    plt.savefig(title+".png")

def main():

    src = "coordinates"

    data = read_data(src)


    plot(data)
    
    plt.show(block=False)


if __name__ == '__main__':
    main()
