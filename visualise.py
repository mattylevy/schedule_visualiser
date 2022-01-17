import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')



def gantt(df):
    ''' This function plots gantt chart from a dataframe '''
    
    """ FORMATTING """
    
    large = 22; med = 16; small = 12
    params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
    plt.rcParams.update(params)
    plt.style.use('seaborn-whitegrid')
    sns.set_style("white")
    #sns.despine()
    #%matplotlib inline
    
    
    
    
    fig, ax = plt.subplots()

    # sort dataframe by start times
    df = df.sort_values(by = ['start'])
    
    #print ("\nPrinting raw dataframe\n", df)
    
    # get unique work centre values as a list
    wc_list = df['wc'].unique()
    wc_list.sort()
    
    #print("\n Unique work centres :", wc_list)  
    
    # get unique prod order values as a list
    po_list = df['prod_order'].unique()
    po_list.sort()
    
    
    ''' BROKEN BAR CHART PLOTTING LOOP '''
    
    d = [24, 48, 72, 96, 24*5]
    m = [12, 48-12, 72-12, 96-12, (24*5)-12]
    x_labels = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    #y_labels = ["W/C 1", "W/C 2", "W/C 3", "W/C 4", "W/C 5", "W/C 6"]
    
    print (m)
    
    # set bar y-height
    bar_height = 0.7
    
    # set x padding
    padding = 0.15
     
     
    # set minor y-axis grid between WC points
    ax.set_yticks(wc_list + 0.5, minor=True)
    
    # show minor Y-axis grid
    ax.yaxis.grid(True, which='minor')

    
    # set major X-axis grid every 12 h  [FOR LABELS]
    ax.set_xticks(m, minor=False)


    
    # set axis limits
    plt.xlim(0,24*5)
    plt.ylim(-0.6,5.6)
    
    
    plt.xticks(m, x_labels)
    
    #plt.yticks(wc_list + 0.5, y_labels)
        
    # set minor X-axis grid every 24 h
    ax.set_xticks(d, minor=True)
    
    # show minor x-axis grid
    ax.xaxis.grid(True, which='minor')
    
    
    # set style
    #sns.set_style("white")
    
    # Hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())
    
    
    for index, row in df.iterrows():        # for each row in dataframe
        
        # Define PLOT variables for each task
        
        po = row['prod_order']      # DETERMINES COLOUR
        wc = row['wc']              # DETERMINES Y-POSITION MID
        start = row['start']        # DETERMINES X-POSITION START 
        time = row['duration']      # DETERMINES X-POSITION LENGTH
    
        #print(po, wc, start, time)
        
        # plot "blocks" as per data
        plt.broken_barh([(start + padding, time - padding)], (wc_list[wc] - bar_height/2, bar_height),
                    
                    # allocate colour based on prod order number
                    facecolors = plt.cm.bone(po_list[po] / len(po_list)),  # terrain
                    
                    # add edges to each block
                    #edgecolor = "black"
                    )
        '''            
        plt.annotate(po,                        # Annotation text
                 (start + (time/2),wc),         # coordinates to position the label
                 textcoords="offset points",    # how to position the text
                 xytext=(0,0),                  # distance from text to points (x,y)
                 ha='center')                   # horizontal alignment can be left, right or center
    '''
        plt.pause(0.0000001)

                            
    # display plot
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(handles, labels)
    
    
    # show legend
    plt.legend()
    
    
    plt.show()
    
    