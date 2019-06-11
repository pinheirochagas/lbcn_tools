


from nilearn import plotting
import pandas as pd
import scipy.io as sio
import numpy as np


# Load subjVar as pandas dataframe
fname = '/Users/pinheirochagas/Desktop/elinfo.csv'
mni = np.loadtxt(fname, delimiter=',')
fname = '/Users/pinheirochagas/Desktop/colors.csv'
colors = np.loadtxt(fname, delimiter=',')

view = plotting.view_markers(mni, colors, marker_size=5)
view.open_in_browser()
view.save_as_html("/Users/pinheirochagas/Desktop/elinfo.html")


img = datasets.fetch_localizer_button_task()
view = plotting.view_img_on_surf(img, threshold='90%', surf_mesh='fsaverage')



fname = '/Users/pinheirochagas/Downloads/arithmetic_association-test_z_FDR_0.01.nii'

plotting.plot_glass_brain(fname, display_mode='lyrz', threshold=3)
plt.savefig('/Users/pinheirochagas/Desktop/arith_neurosynth.png')




plotting.plot_glass_brain(stat_img, threshold=3)




from nilearn import plotting, datasets, surface
dmn_coords = [(0, -52, 18), (-46, -68, 32), (46, -68, 32), (1, 50, -5)]




img = datasets.fetch_localizer_button_task()['tmap']
view = plotting.view_img_on_surf(fname, threshold='90%', surf_mesh='fsaverage')






from nilearn import plotting
dmn_coords = [(0, -52, 18), (-46, -68, 32), (46, -68, 32), (1, 50, -5)]
view = plotting.view_markers(
dmn_coords, ['red', 'cyan', 'magenta', 'orange'], marker_size=10)
view.open_in_browser()