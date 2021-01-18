import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", float_precision='legacy')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = np.array([i for i in df['Year']] + [i for i in range(2014, 2050)])
    plt.plot(x, res.intercept + res.slope*x, 'r', label='fitted line')
    # Create second line of best fit
    yr2000 = df[df['Year'] >= 2000]
    res2000 = linregress(yr2000['Year'], yr2000['CSIRO Adjusted Sea Level'])
    x = np.array([i for i in range(2000, 2050)])
    plt.plot(x, res2000.intercept + res2000.slope*x, 'r', label='fitted line 2000')
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
