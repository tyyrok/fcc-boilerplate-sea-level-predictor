import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('./epa-sea-level.csv',
                     sep=',')
    # Create scatter plot 
    # Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Create first line of best fit
    reg = linregress(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])
    yearPredict = np.arange(1880, 2051)

    plt.plot(yearPredict, reg.intercept + reg.slope * yearPredict)

    # Create second line of best fit
    df_new = df.loc[df['Year'] >= 2000, ['Year', 'CSIRO Adjusted Sea Level'] ]
    reg2 = linregress(x=df_new['Year'], y=df_new['CSIRO Adjusted Sea Level'])
    yearPredict2 = np.arange(2000, 2051)
    plt.plot(yearPredict2, reg2.intercept + reg2.slope * yearPredict2)
    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()