import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import warnings

register_matplotlib_converters()
warnings.filterwarnings('ignore')

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df.loc[df.value.between(df.value.quantile(0.025), df.value.quantile(0.975))]


def draw_line_plot():

    # Draw line plot
    fig, ax = plt.subplots(figsize=(32, 10))
    
    ax.plot(df.index, df.value, linewidth=3, color='#E3242B')
    
    #Set label and title
    plt.xlabel('Date', fontsize=20, labelpad=9)
    plt.ylabel('Page Views', fontsize=20, labelpad=9)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=24, pad=12)
    plt.tick_params(axis='both', which='both', labelsize=20, pad=10, width=1.5)
    
    # Customize the linewidth of all spines
    for spine in ax.spines.values():
        spine.set_linewidth(1.5)

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
    

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy().reset_index()
    
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    df_bar['year'] = [i.year for i in df_bar.date]
    df_bar['month'] = [i.strftime('%B') for i in df_bar.date]
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=month_order, ordered=True)
    df_bar = df_bar.groupby(['year', 'month'], observed=False).mean().reset_index()

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(15.14, 13.3))

    sns.barplot(ax=ax, x=df_bar.year, y=df_bar.value, hue=df_bar.month, palette='tab10', width=0.5)
    
    #Set label and title    
    plt.xlabel('Years', fontsize=20, labelpad=9)
    plt.ylabel('Average Page Views', fontsize=20, labelpad=9)
    plt.legend(title='Months', title_fontsize=20, fontsize=20)
    plt.tick_params(axis='both', which='both', labelsize=20, pad=10, width=1.5)
    plt.xticks(rotation=90)

    # Customize the linewidth of all spines
    for spine in ax.spines.values():
        spine.set_linewidth(1.5)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():

    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    # Set up subplots
    fig, ax = plt.subplots(1, 2, figsize=(28.8, 10.8))
    
    boxplot_settings = {'flierprops': dict(markerfacecolor='black', marker='d', markersize=4)}
    
    # Subplot 1 (Year)
    sns.boxplot(ax=ax[0], x=df_box.year, y=df_box.value, palette='tab10', **boxplot_settings)
    
    ax[0].set_xlabel('Year', fontsize=15)
    ax[0].set_ylabel('Page Views', fontsize=15)
    ax[0].set_title('Year-wise Box Plot (Trend)', fontsize=19)
    ax[0].set_yticks(range(0, 200001, 20000))
    ax[0].tick_params(axis='both', which='both', labelsize=15)
    ax[0].set_ylim(bottom=0, top=200000)
    
    # Subplot 2 (Month)
    sns.boxplot(ax=ax[1], x=df_box.month, y=df_box.value, order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], palette='husl', **boxplot_settings)
    
    ax[1].set_xlabel('Month', fontsize=15)
    ax[1].set_ylabel('Page Views', fontsize=15)
    ax[1].set_title('Month-wise Box Plot (Seasonality)', fontsize=19)
    ax[1].set_yticks(range(0, 200001, 20000))
    ax[1].tick_params(axis='both', which='both', labelsize=15)
    ax[1].set_ylim(bottom=0, top=200000)
    
    plt.tight_layout(rect=(0.015, 0.045, 0.985, 0.955), w_pad=5)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
