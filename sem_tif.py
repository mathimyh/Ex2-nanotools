from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import tifffile as tf
from scipy import ndimage
import os
import matplotlib.gridspec as gridspec
from scipy.ndimage import rotate


def micro_platina():
    
    bilder = []

    temp = tf.imread("sem\\01_1um_p0t_closeup_cross_ETD_SE.tif")
    bilde0 = temp[300:1800, 0:3000]
    bilder.append(bilde0)
    temp = tf.imread("sem\\01_1um_p0t_closeup_edge_ETD_SE.tif")
    bilde1 = temp[500:2000, 0:3000]
    bilder.append(bilde1)
    temp = tf.imread("sem\\01_1um_p0t_overview_ETD_BSE.tif")
    temp = rotate(temp,182)
    bilde2 = temp[250:2150, 450:2650]
    bilder.append(bilde2)

    skala0 = 1.34896e-09
    skala1 = 6.74479e-10
    skala2 = 1.92708e-08
    extent0 = [0, skala0 * bilde0.shape[1] * 10**6, 0, skala0 * bilde0.shape[0] * 10**6]
    extent1 = [0, skala1 * bilde1.shape[1] * 10**6, 0, skala1 * bilde1.shape[0] * 10**6]
    extent2 = [0, skala2 * bilde2.shape[1] * 10**6, 0, skala2 * bilde2.shape[0] * 10**6]
    
    
    plt.rcParams["figure.figsize"] = [7.5, 3.5]
    fig = plt.figure(constrained_layout=True)
    gs = fig.add_gridspec(2,2)
    ax0 = fig.add_subplot(gs[0,1])
    ax1 = fig.add_subplot(gs[1,1])
    ax2 = fig.add_subplot(gs[:,0])
    
    ax0.imshow(bilder[0], extent=extent0)
    ax1.imshow(bilder[1], extent=extent1)
    ax2.imshow(bilder[2], extent=extent2)
            
    ax0.set_xticks([])
    ax0.set_yticks([])
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax2.set_xticks([])
    ax2.set_yticks([])
    
    gs.update(wspace = 0.01, hspace = 0.01)
    fig.tight_layout()
    
    from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
    import matplotlib.font_manager as fm
    import matplotlib.patheffects as patheffects
    fontprops = fm.FontProperties(size=18)
    
    scalebar_kwargs = {'size': 0.5, 'label': '500 nm', 'loc': 3, 'frameon': False, 'color': 'white', 'size_vertical': 0.01, 'label_top': False, 'fontproperties': fontprops}
    scalebar0 = AnchoredSizeBar(transform=ax0.transData, **scalebar_kwargs)
    # Denne legger til et svart omriss rundt scalebar teksten, for å gjøre den lettere å lese
    scalebar0.txt_label._text.set_path_effects([patheffects.withStroke(linewidth=2, foreground='black', capstyle="round")])
    ax0.add_artist(scalebar0)
    
    scalebar1 = AnchoredSizeBar(transform=ax1.transData, **scalebar_kwargs)
    # Denne legger til et svart omriss rundt scalebar teksten, for å gjøre den lettere å lese
    scalebar1.txt_label._text.set_path_effects([patheffects.withStroke(linewidth=2, foreground='black', capstyle="round")])
    ax1.add_artist(scalebar1)
    
    
    scalebar_kwargs = {'size': 5, 'label': '5 um', 'loc': 3, 'frameon': False, 'color': 'white', 'size_vertical': 0.2, 'label_top': False, 'fontproperties': fontprops}
    scalebar2 = AnchoredSizeBar(transform=ax2.transData, **scalebar_kwargs)
    # Denne legger til et svart omriss rundt scalebar teksten, for å gjøre den lettere å lese
    scalebar2.txt_label._text.set_path_effects([patheffects.withStroke(linewidth=2, foreground='black', capstyle="round")])
    ax2.add_artist(scalebar2)
    
    
    # # Lagrer figuren
    fig.savefig("1_um_pt_SEM_data", dpi=500)
    
    
    #plt.show()

micro_platina()