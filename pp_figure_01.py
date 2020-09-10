"""
Module file containing functions that allow to reproduce FIG. 1 of the article

    Interaction of "Solitons" in a Collisionless Plasma and the Recurrence of Initial States,
    N. J. Zabusky and M. D. Kruskal,
    Phys. Rev. Lett. 15, 240 (1965)

This module was prepared as a part of the scientific short course

  A brief guide to publication-ready scientific figures using Python's matplotlib

held during the 2020 seminar week of the Ultrafast Laser Laboratory
at Institute of Quantum Optics at Leibniz University Hannover.

Author: O. Melchert
Date: 2020-09-08
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

__author__ = 'Oliver Melchert'
__date__ = '2020-09-09'

def fetch_data(path):
    """fetch data

    Reads in data from file in numpy npz-format

    Args:
      path (str): path to npz-file

    Returns: (x, t, uxt)
      x (1D array): x samples
      t (1D array): t samples
      uxt (2D array): wave profile u(x,t)
    """
    dat = np.load(path)
    return dat['x'], dat['t'], dat['uxt']


def set_style():
    """set figure style

    Function that customizes the default style to be conform with the Physical
    Review style and notation guide [1]. For instructions on how to set the
    default style using style sheets see [2].

    Notes:
    - main font size is chosen as 8pt, matching the fontsize of figure captions
    - fontsize of legends and auxiliary text labels are set to 6pt, exceeding
      the minimally required pointsize of 4.25 pt. (1.5 mm)
    - default rc (rc = "run commands", i.e. startup information) settings are
      changed dynamically
    - the custom font-scheme 'type2' depends on your latex installation and
      is not guaranteed to run on your specific system

    Refs:
      [1] https://journals.aps.org/prl/authors
      [2] https://matplotlib.org/3.3.1/tutorials/introductory/customizing.html
    """

    fig_width_1col = 3.4        # figure width in inch
    fig_width_2col = 7.0        # figure width in inch
    fig_aspect_ratio = 0.66     # width to height aspect ratio
    font_size = 8               # font size in pt
    font_size_small = 6         # font size in pt
    font_scheme = 'type2'       # options: 
                                #   None    - default matplotlib fonts
                                #   'type1' - text: Helvetica, math: Computer modern
                                #   'type2' - text: Helvetica, math: Helvetica 

    mpl.rcParams['figure.figsize'] = fig_width_1col, fig_aspect_ratio*fig_width_1col
    mpl.rcParams['axes.labelsize'] = font_size
    mpl.rcParams['font.size'] = font_size
    mpl.rcParams['legend.fontsize'] = font_size_small
    mpl.rcParams['xtick.labelsize'] = font_size
    mpl.rcParams['ytick.labelsize'] = font_size
    mpl.rcParams['xtick.direction'] = 'out'
    mpl.rcParams['ytick.direction'] = 'out'
    mpl.rcParams['lines.linewidth'] = 1.0
    mpl.rcParams['axes.linewidth'] =  0.5

    if font_scheme == 'type1':
        mpl.rcParams['text.usetex'] = True
        mpl.rcParams['font.family'] = 'sans-serif'
        mpl.rcParams['font.sans-serif'] = 'Helvetica'
        mpl.rcParams['mathtext.fontset'] = 'cm'

    if font_scheme == 'type2':
        mpl.rcParams['text.usetex'] = True
        mpl.rcParams['text.latex.preamble'] = [
           r'\usepackage{siunitx}',
           r'\sisetup{detect-all}',
           r'\usepackage{helvet}',
           r'\usepackage{sansmath}',
           r'\sansmath'
        ]


def set_circle(ax, x0, y0, label):
    """set circle

    Function that generates a circle with text-label at its center.
    For more options on scatter plots, see [1], for more options on
    setting text, see [2]

    Refs:
      [1] https://matplotlib.org/3.3.1/api/_as_gen/matplotlib.pyplot.scatter.html
      [2] https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.text.html

    Args:
      ax (object): figure part for which the labeled circle is intended
      x0 (float): x-position for center of circle
      y0 (float): y-position for center of circle
      label (str): text that should be displayed within circle
    """
    # -- scatter plot consisting of a single object
    ax.scatter(x0, y0, s=50, linewidth=0.75, facecolors='none', edgecolor='black', zorder=10)
    # -- place text at the center of the scatter plot object
    ax.text(x0, y0, label, backgroundcolor='none', ha='center', va='center', color='black', zorder=10, fontsize=6)


def set_key(ax, lines):
    """set key

    Function generating a custom key, see [1] for more options

    Refs:
      [1] https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.legend.html

    Args:
      ax (object): figure part for which the key is intended
      lines (list): list of  Line2D objects
    """
    # -- extract labels from lines
    labels = [x.get_label() for x in lines]
    # -- customize key
    ax.legend(lines,                # list of Line2D objects
              labels,               # labels 
              title = '',           # title shown on top of key 
              loc = 0,              # location of the key 
              ncol = 1,             # number of columns
              labelspacing = 0.3,   # vertical space between handles in font-size units
              borderpad = 0.3,      # distance to legend border in font-size units
              handletextpad = 0.6,  # distance between handle and label in font-size units
              handlelength = 2.0,   # length of handle in font-size units
              frameon = False       # remove background patch
              )


def set_grid(ax):
    """set grid

    Function generating a custom grid, see [1] for more options

    Refs:
      [1] https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.grid.html

    Args:
      ax (object): figure part for which the key is intended
    """
    #ax.set_facecolor('lightgray')
    ax.grid(which = 'major',        # grid lines at major ticks only
            linestyle = '-',        # solid line
            linewidth = 0.5,        # width of gridlines
            color = 'lightgray',    # color of gridlines
            zorder = 0
            )


def generate_figure(x, t, uxt, fig_format=None, fig_name='fig01'):
    """generate figure

    Function generating a figure reproducing FIG. 1 of [1].

    Refs:
      [1] Interaction of "Solitons" in a Collisionless Plasma and the Recurrence of Initial States,
          N. J. Zabusky and M. D. Kruskal,
          Phys. Rev. Lett. 15, 240 (1965)

    Args:
      x (1D array): x-samples
      ax (object): figure part for which the labeled circle is intended
      x0 (float): x-position for center of circle
      y0 (float): y-position for center of circle
      label (str): text that should be displayed within circle

      x (1D array): x samples
      t (1D array): t samples
      uxt (2D array): wave profile u(x,t)
      fig_format (str): format for output figure
                        (choices: png, pdf, svg; default: interactive figure)
    """

    # (1) SET A STYLE THAT FITS THE TARGET JOURNAL
    set_style()

    # (2) SET FIGURE LAYOUR
    fig = plt.figure()
    plt.subplots_adjust(left=0.12, bottom=0.16, right=0.97, top= 0.98)
    gs00 = GridSpec(1,1)
    ax01 = plt.subplot(gs00[:,:])

    # (3) SET FIGURE CONTENTS
    # -- custom constants and local functions
    tB = 1./np.pi                                   # breakdown time
    _ux = lambda t0: uxt[np.argmin(np.abs(t-t0))]   # wave form for array index closest to t0 

    # -- plot real-vaued field at selected times 
    l1 = ax01.plot(x, _ux(0.0),    color='blue',  dashes=[1,1], zorder=100, label=r'$t=0$')
    l2 = ax01.plot(x, _ux(1.0*tB), color='green', dashes=[3,1], zorder=101, label=r'$t=t_{\mathrm{B}}$')
    l3 = ax01.plot(x, _ux(3.6*tB), color='black', zorder=102, label=r'$t=3.6\,t_{\mathrm{B}}$')

    # -- add legend 
    set_key(ax01, l1 + l2 + l3)

    # -- set data curve labels
    ax01.text(1.27, -0.9, r'A', backgroundcolor='none', ha='left', va='bottom', color='blue',  zorder=10)
    ax01.text(0.60, -0.9, r'B', backgroundcolor='none', ha='left', va='bottom', color='green', zorder=10)
    ax01.text(1.75, -0.9, r'C', backgroundcolor='none', ha='left', va='bottom', color='black', zorder=10)

    # -- set auxiliary dash-dotted lines
    _f = lambda x: -1.5+1.5*np.where(x>0.8, x, x+2.)
    ax01.plot(x[x<0.75], _f(x[x<0.75]), color='black', dashes = [15,1,2,1,2,1], linewidth=0.75)
    ax01.plot(x[x>0.80], _f(x[x>0.80]), color='black', dashes = [15,1,2,1,2,1], linewidth=0.75)

    # -- set circles with labels
    for  idx, x0 in enumerate([0.643, 0.362, 0.098, 0.920, 1.14, 1.37, 1.6, 1.845]):
        set_circle(ax01, x0, _f(x0) + 0.2, '$%d$'%(idx+1))

    # (4) SET AXIS DETAILS
    # -- customize x-axis
    x_lim = (0, 2)
    x_ticks = (0., 0.5, 1.0, 1.5, 2.0)
    # -- major ticks
    ax01.tick_params(axis='x', direction='out', length=3.5, pad=2, top=False)
    ax01.set_xlim(x_lim)
    ax01.set_xticks(x_ticks)
    # -- minor ticks
    ax01.tick_params(axis='x', which='minor', length=2.)
    ax01.set_xticks(np.linspace(x_lim[0],x_lim[1], int((x_lim[1]-x_lim[0])/0.1), endpoint=False), minor=True)
    # -- label
    ax01.set_xlabel(r'Normalized distance $x$')

    # -- customize y-axis
    y_lim = (-1., 3.)
    y_ticks = (-1., 0., 1., 2., 3.)
    # -- major ticks
    ax01.tick_params(axis='y', direction='out', length=3.5, pad=2, right=False)
    ax01.set_ylim(y_lim)
    ax01.set_yticks(y_ticks)
    # -- minor ticks
    ax01.tick_params(axis='y', which='minor', length=2.)
    ax01.set_yticks(np.linspace(y_lim[0], y_lim[1], int((y_lim[1]-y_lim[0])/0.2), endpoint=False), minor=True)
    # -- label 
    ax01.set_ylabel(r'Real-valued field $u(x,t)$')

    # (5) SET BACKGROUND GRID
    set_grid(ax01)

    # (6) SAVE FIGURE
    if fig_format == 'png':
        plt.savefig(fig_name+'.png', format='png', dpi=600)
    elif fig_format == 'pdf':
        plt.savefig(fig_name+'.pdf', format='pdf')
    elif fig_format == 'svg':
        plt.savefig(fig_name+'.svg', format='svg')
    else:
        plt.show()


def main():
    x, t, uxt = fetch_data('KdV_raw_data.npz')
    generate_figure(x, t, uxt, fig_format='png', fig_name='fig01')


if __name__ == '__main__':
    main()
