"""
Module file containing functions that allow to reproduce FIG. 2 of the article

    Interaction of "Solitons" in a Collisionless Plasma and the Recurrence of Initial States,
    N. J. Zabusky and M. D. Kruskal,
    Phys. Rev. Lett. 15, 240 (1965)

This module was prepared as a part of the scientific short course

  A brief guide to publication-ready scientific figures using Python's matplotlib

held during the 2020 seminar week of the Ultrafast Laser Laboratory
at Institute of Quantum Optics at Leibniz University Hannover.

Author: O. Melchert
Date: 2020-09-09
"""
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as col
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
    fig_aspect_ratio = 1.45     # width to height aspect ratio
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
    ax.scatter(x0, y0, s=60, linewidth=0.75, facecolors='white', edgecolor='black', zorder=10)
    # -- place text at the center of the scatter plot object
    ax.text(x0, y0, label, backgroundcolor='none', ha='center', va='center', color='black', zorder=11, fontsize=6)


def set_colorbar(fig, img, ax):
    """colorbar helper"""
    # -- extract position information for colorbar placement
    refPos = ax.get_position()
    x0, y0, w, h = refPos.x0, refPos.y0, refPos.width, refPos.height
    colorbar_axis = fig.add_axes([x0, y0+1.015*h, w, 0.0175*h])
    colorbar = fig.colorbar(img, cax=colorbar_axis, orientation='horizontal',extend='both')
    colorbar.ax.tick_params(color='k',
                        labelcolor='k',
                        bottom=False,
                        direction='out',
                        labelbottom=False,
                        labeltop=True,
                        top=True,
                        size=3,
                        labelsize=8.,
                        pad=0.
                        )

    colorbar.set_ticks((-1, 0, 1))
    colorbar.ax.set_title(r"Real-valued field $u(x,t)$", fontsize=8., y=2.5)

def generate_figure(x, t, uxt, fig_format=None, fig_name='fig02'):
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
    plt.subplots_adjust(left=0.17, bottom=0.065, right=0.96, top= 0.91, wspace=0.3, hspace=0.05)
    gs00 = GridSpec(1,6)
    ax01 = plt.subplot(gs00[0,0:5])
    ax02 = plt.subplot(gs00[0,5])

    # (3.1) SUBPLOT 1 - SET FIGURE CONTENTS
    tR = 30.4/np.pi
    t = t/tR
    img = ax01.pcolorfast(x, t, uxt[:-1,:-1],
                          norm = col.Normalize(vmin = -1., vmax = 1.),
                          cmap = mpl.cm.get_cmap('coolwarm')
                          )
    set_colorbar(fig, img, ax01)

    # -- add auxiliary horizontal lines
    for t0 in [0.5,1./3,1./4,1./5,1./6]:
        ax01.axhline(t0, color='black', dashes=[2,2], linewidth=1)

    for idx, x0 in enumerate([0.59, 0.33, 0.1, 1.86, 1.64, 1.43, 1.23, 1.02, 0.82]):
      set_circle(ax01, x0, 0.11, r"$%d$"%(idx+1))

    ax01.scatter(0.45, 0.5,  facecolors='None', s=1400, linewidth=1, edgecolors='black',linestyle='--', zorder=100)
    ax01.scatter(1.90, 0.4,  facecolors='None', s=600,  linewidth=1, edgecolors='black',linestyle='--', zorder=100)
    ax01.scatter(1.67, 1./3, facecolors='None', s=600,  linewidth=1, edgecolors='black',linestyle='--', zorder=100)
    ax01.scatter(1.23, 1./4, facecolors='None', s=400,  linewidth=1, edgecolors='black',linestyle='--', zorder=100)
    ax01.scatter(0.98, 1./5, facecolors='None', s=400,  linewidth=1, edgecolors='black',linestyle='--', zorder=100)
    ax01.scatter(0.83, 1./6, facecolors='None', s=200,  linewidth=1, edgecolors='black',linestyle='--', zorder=100)

    # (4.1) SUBPLOT 1 - SET AXIS DETAILS
    # -- customize x-axis
    x_lim = (0,2)
    x_ticks = (0,0.6,1.2,1.8)
    ax01.tick_params(axis='x', length=3., pad=2, right=False)
    ax01.set_xlim(x_lim)
    ax01.set_xticks(x_ticks)
    ax01.set_xlabel(r"Normalized distance $x$")

    # -- customize y-axis
    y_lim = (0.1,0.6)
    y_ticks = (0.1,1./6, 1./5,1./4,0.3,1./3,0.4,0.5)
    y_ticklabels = (r'$0.1\,T_{\mathrm{R}}$', r'$T_{\mathrm{R}}/6$',
                    r'$T_{\mathrm{R}}/5$', r'$T_{\mathrm{R}}/4$',
                    r'$0.3\,T_{\mathrm{R}}$', r'$T_{\mathrm{R}}/3$',
                    r'$0.4\,T_{\mathrm{R}}$', r'$0.5\,T_{\mathrm{R}}$')
    ax01.tick_params(axis='y', length=3., pad=2, top=False)
    ax01.set_ylim(y_lim)
    ax01.set_yticks(y_ticks)
    ax01.set_yticklabels(y_ticklabels)
    ax01.set_ylabel(r"Normalized time $t$")


    # (3.2) SUBPLOT 2 - SET FIGURE CONTENTS

    # -- trace path of 1st soliton in subfigure 1
    x_idx = np.zeros(len(t), dtype=int)
    a = np.zeros(len(t)); a[0]=1
    mask = np.zeros(len(x)); mask[x<0.2]=1; mask[x>1.8]=1
    for i in range(1,len(t)):
       x_idx[i] = np.argmax(uxt[i]*mask)
       a[i] = np.real(uxt[i,x_idx[i]])
       s = np.min( [ np.abs(x_idx[i]-x_idx[i-1]), np.abs(x_idx[i]-x_idx[-1]+len(x))    ]  )
       mask = np.roll(mask, s )

    ax02.plot(a, t, color='black')

    # -- highlight traced path of 1st soliton in subfigure 1
    ax01.plot(x[x_idx][::20],t[::20],color='white', linewidth=0, marker='.', markersize=2)

    # -- add auxiliary horizontal lines
    for t0 in [0.5,1./3,1./4,1./5,1./6]:
        ax02.axhline(y=t0, xmin=0., xmax=a[np.argmin(np.abs(t-t0))]/4.,  color='black', dashes=[2,2], linewidth=1)


    # (4.2) SUBPLOT 2 - SET AXIS DETAILS
    x_lim = (0,4)
    x_ticks = (0,2,4)
    ax02.tick_params(axis='x',length=3.,pad=1,top=False)
    ax02.set_xlim(x_lim)
    ax02.set_xticks(x_ticks)
    ax02.set_xlabel(r'$A_{\mathrm{S1}}$')

    ax02.tick_params(axis='y',length=3.,pad=1,labelleft=False,right=False)
    ax02.set_ylim(y_lim)
    ax02.set_yticks(y_ticks)

    ax02.spines['right'].set_visible(False)
    ax02.spines['top'].set_visible(False)

    ax02.text(1., 0.01, r'Amplitude of soliton no. 1',
            horizontalalignment='center', verticalalignment='bottom',
            rotation='vertical', transform=ax02.transAxes)


    # -- add figure labels
    ax01.text(-0.02, 1.01, r'(a)', fontsize=8,
            horizontalalignment='right', verticalalignment='bottom',
            transform=ax01.transAxes)

    ax02.text(0.0, 1.01, r'(b)', fontsize=8,
            horizontalalignment='left', verticalalignment='bottom',
            transform=ax02.transAxes)

    # (6) SAVE FIGURE
    if fig_format == 'png':
        plt.savefig(fig_name+'.png', format='png', dpi=600)
    elif fig_format == 'pdf':
        plt.savefig(fig_name+'.pdf', format='pdf', dpi=600)
    elif fig_format == 'svg':
        plt.savefig(fig_name+'.svg', format='svg')
    else:
        plt.show()


def main():
    x, t, uxt = fetch_data('KdV_raw_data.npz')
    generate_figure(x, t, uxt, fig_format='png', fig_name='fig02')


if __name__ == '__main__':
    main()
