import numpy as np
from mne.viz import circular_layout, plot_connectivity_circle
import matplotlib.pyplot as plt


# Load data
corr_chans = np.loadtxt('/Volumes/LBCN8T/Stanford/data/Results/Memoria/connectivity/Memoria_corr_chans_math.csv', delimiter=',')

corr_chans = np.loadtxt('/Volumes/LBCN8T/Stanford/data/Results/Memoria/connectivity/Memoria_dist_chans_iES.csv', delimiter=',')
corr_chans = np.loadtxt('/Volumes/LBCN8T/Stanford/data/Results/Memoria/connectivity/Memoria_corr_chans_iES.csv', delimiter=',')

corr_chans = np.loadtxt('/Volumes/LBCN8T/Stanford/data/Results/Memoria/connectivity/Memoria_corr_chans_norm_dist_iES.csv', delimiter=',')




boundaries = np.loadtxt('/Users/pinheirochagas/Desktop/boundaries.csv', delimiter=',')

import csv
with open('/Users/pinheirochagas/Desktop/labels.csv', 'r') as f:
  reader = csv.reader(f, delimiter=',')
  labels = list(reader)
labels = labels[1:]

l1 = ['a' for i in range(len(labels))]
for i in range(len(labels)):
    l1[i] = labels[i][0]
labels = l1


label_colors = [labels for label in labels]

labels[1][0]

node_angles = circular_layout(labels, labels, group_boundaries = boundaries)

fig = plt.figure(figsize=(20,20))


plot_connectivity_circle(corr_chans, labels,
                         node_angles=node_angles,
                         node_colors=[(.5,.5,.5, 1)],
                         facecolor = [0.1,0.1,0.1],
                         node_edgecolor=[0.1,0.1,0.1],
                         textcolor=[1,1,1],
                         fontsize_names = 10,
                         colormap='viridis',
                         vmin=np.min(corr_chans),
                         vmax = np.max(corr_chans),
                         linewidth = 1.5, fig=fig)
, fig=fig
vmax = np.max(corr_chans[corr_chans < 1]),

plot_connectivity_circle(corr_chans, labels,
                         node_angles=node_angles,
                         node_colors = [(.5, .5, .5, 1)],
                         facecolor = [0.1, 0.1, 0.1],
                         node_edgecolor = [0.1, 0.1, 0.1],
                         linewidth = 1.5)

plt.savefig('/Users/pinheirochagas/Desktop/chan_corr.png')
plt.savefig('/Users/pinheirochagas/Desktop/chan_corr_norm_dist.png')

plt.savefig('/Users/pinheirochagas/Desktop/chan_dist.png')


plt.savefig('/Users/pinheirochagas/Desktop/connectivity_plot_memoria_ies.png')











from nilearn import datasets
print('Datasets shipped with nilearn are stored in: %r' % datasets.get_data_dirs())



motor_images = datasets.fetch_neurovault_motor_task()
stat_img = motor_images.images[0]


from nilearn import plotting




