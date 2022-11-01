import hyperspy.api as hs
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import tifffile as tf
from scipy import ndimage
import os
import matplotlib.gridspec as gridspec

def pt_1_eds():
    # Henter de første filene å se på
    filename_rpl = "eds\\1\\New folder\\Pt_um_star 1.rpl"
    filename_emsa = "eds\\1\\Pt_um_star 1Map Sum Spectrum.emsa"
    filename_txt = "eds\\1\\Pt_um_star 1New Text Document.txt"
    
    
    # Fikser dataene 
    s = hs.load(filename_rpl).T
    s.set_signal_type('EDS_SEM')
    s_c = hs.load(filename_emsa, signal_type='EDS_SEM')
    s.get_calibration_from(s_c)
    import numpy as np
    width = float(np.loadtxt(filename_txt, skiprows=4, max_rows=1, dtype=object, usecols=2)[()][:-2])
    scale = width / s.axes_manager.navigation_shape[0]
    s.axes_manager.navigation_axes[0].scale = scale
    s.axes_manager.navigation_axes[1].scale = scale
    s.axes_manager.navigation_axes[0].units = "um"
    s.axes_manager.navigation_axes[1].units = "um"
    
    # Gjør funksjonsgreiene som er nice 
    st = s.T
    st_rebin = st.rebin(scale=(4,8,8))
    s_sum = s.sum()
    s_rebin = s.rebin(scale=(8,8,1))
    elements = ["C", "Fe", "Ga", "N", "Ni", "O", "Pt", "Si"]
    s_rebin.set_elements(elements)
    s_sum2 = s_rebin.sum()
    
    # Denne her viser godt alle elementene du har 
    #s_sum2.plot(integration_windows='auto')
    
    s_rebin.add_lines()
    # Denne sjekker lista di, så du vet hvilke som tilhører hverandre
    #print(s_rebin.metadata.Sample)
    
    linjer = s_rebin.get_lines_intensity(plot_result=False)
    s_sum2 = s_rebin.sum()
    
    fig, axes = plt.subplots(4, 2)
    imshow_axes = [0,0,0,0,0,0,0,0]
    colors = ["Greys", "Oranges", "Reds", "Purples", "Greens", "Blues", "RdPu", "YlOrBr"]
    indeks = 0
    
    for stuff in axes:
        for element in stuff:
            imshow_axes[indeks] = element.imshow(linjer[indeks].T, extent=linjer[indeks].T.axes_manager.signal_extent, cmap=colors[indeks])
            element.set_title(elements[indeks])
            mini, maxi = (imshow_axes[indeks].get_clim())
            imshow_axes[indeks].set_clim(0, maxi-3)
            indeks += 1
    
    plt.show()


    
def pt_2_eds():
    # Henter de første filene å se på
    filename_emsa = "eds\\2\\Pt_um_star 2Map Sum Spectrum.emsa"
    filename_rpl = "eds\\2\\New folder\Pt_um_star 2.rpl"
    filename_txt = "eds\\2\\Pt_um_star 2New Text Document.txt"
    
    
    # Fikser dataene 
    s = hs.load(filename_rpl).T
    s.set_signal_type('EDS_SEM')
    s_c = hs.load(filename_emsa, signal_type='EDS_SEM')
    s.get_calibration_from(s_c)
    import numpy as np
    width = float(np.loadtxt(filename_txt, skiprows=4, max_rows=1, dtype=object, usecols=2)[()][:-2])
    scale = width / s.axes_manager.navigation_shape[0]
    s.axes_manager.navigation_axes[0].scale = scale
    s.axes_manager.navigation_axes[1].scale = scale
    s.axes_manager.navigation_axes[0].units = "um"
    s.axes_manager.navigation_axes[1].units = "um"
    
    # Gjør funksjonsgreiene som er nice 
    st = s.T
    st_rebin = st.rebin(scale=(4,8,8))
    s_sum = s.sum()
    
    # Sjekker hvilke grunnstoffer man har ved hjelp av denne :)
    #s_sum.plot()
    
    s_rebin = s.rebin(scale=(8,8,1))
    elements = ["C", "Fe", "Ga", "N", "Ni", "O", "Pt", "Si"]
    s_rebin.set_elements(elements)
    s_sum2 = s_rebin.sum()
    
    # Denne her viser godt alle elementene du har 
    #s_sum2.plot(integration_windows='auto')
    
    s_rebin.add_lines()
    # Denne sjekker lista di, så du vet hvilke som tilhører hverandre
    #print(s_rebin.metadata.Sample)
    
    linjer = s_rebin.get_lines_intensity(plot_result=False)
    s_sum2 = s_rebin.sum()
    
    fig, axes = plt.subplots(4, 2)
    imshow_axes = [0,0,0,0,0,0,0,0]
    colors = ["Greys", "Oranges", "Reds", "Purples", "Greens", "Blues", "RdPu", "YlOrBr"]
    indeks = 0
    
    for stuff in axes:
        for element in stuff:
            imshow_axes[indeks] = element.imshow(linjer[indeks].T, extent=linjer[indeks].T.axes_manager.signal_extent, cmap=colors[indeks])
            element.set_title(elements[indeks])
            indeks += 1
    
    plt.show()
 
def pt_3_eds():
    # Henter de første filene å se på
    filename_emsa = "eds\\3\\Pt_um_star 3Map Sum Spectrum.emsa"
    filename_rpl = "eds\\3\\New folder\Pt_um_star 3.rpl"
    filename_txt = "eds\\3\\Pt_um_star 3New Text Document.txt"
    
    
    # Fikser dataene 
    s = hs.load(filename_rpl).T
    s.set_signal_type('EDS_SEM')
    s_c = hs.load(filename_emsa, signal_type='EDS_SEM')
    s.get_calibration_from(s_c)
    import numpy as np
    width = float(np.loadtxt(filename_txt, skiprows=4, max_rows=1, dtype=object, usecols=2)[()][:-2])
    scale = width / s.axes_manager.navigation_shape[0]
    s.axes_manager.navigation_axes[0].scale = scale
    s.axes_manager.navigation_axes[1].scale = scale
    s.axes_manager.navigation_axes[0].units = "um"
    s.axes_manager.navigation_axes[1].units = "um"
    
    # Gjør funksjonsgreiene som er nice 
    st = s.T
    st_rebin = st.rebin(scale=(4,8,8))
    s_sum = s.sum()
    
    # Sjekker hvilke grunnstoffer man har ved hjelp av denne :)
    s_sum.plot()
    
    s_rebin = s.rebin(scale=(8,8,1))
    elements = ["C", "Fe", "Ga", "N", "Ni", "O", "Pt", "Si"]
    s_rebin.set_elements(elements)
    s_sum2 = s_rebin.sum()
    
    # Denne her viser godt alle elementene du har 
    #s_sum2.plot(integration_windows='auto')
    
    s_rebin.add_lines()
    # Denne sjekker lista di, så du vet hvilke som tilhører hverandre
    #print(s_rebin.metadata.Sample)
    
    linjer = s_rebin.get_lines_intensity(plot_result=False)
    s_sum2 = s_rebin.sum()
    
    fig, axes = plt.subplots(4, 2)
    imshow_axes = [0,0,0,0,0,0,0,0]
    colors = ["Greys", "Oranges", "Reds", "Purples", "Greens", "Blues", "RdPu", "YlOrBr"]
    indeks = 0
    
    for stuff in axes:
        for element in stuff:
            imshow_axes[indeks] = element.imshow(linjer[indeks].T, extent=linjer[indeks].T.axes_manager.signal_extent, cmap=colors[indeks])
            element.set_title(elements[indeks])
            indeks += 1
    
    plt.show() 
    
pt_3_eds()