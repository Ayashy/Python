import matplotlib.pyplot as plt

# ---------------------------------------------------------------- #
#                        Figures and axes
# ---------------------------------------------------------------- #

fig = plt.figure(figsize=(5, 2))                  # initialize figure
fig.savefig('out.png')                            # save png image
fig, axes = plt.subplots(5, 2, figsize=(5, 5))    # fig and 5 x 2 nparray of axes
ax = fig.add_subplot(3, 2, 2)                     # add second subplot in a 3 x 2 grid
ax = plt.subplot2grid((2, 2), (0, 0), colspan=2)  # multi column/row axis
ax = fig.add_axes([left, bottom, width, height])  # add custom axis
 
 
# ---------------------------------------------------------------- #
#                        Properties
# ---------------------------------------------------------------- #

fig.suptitle('title')            # big figure title
fig.subplots_adjust(bottom=0.1, right=0.8, top=0.9, wspace=0.2,
hspace=0.5)                      # adjust subplot positions
fig.tight_layout(pad=0.1, h_pad=0.5, w_pad=0.5,
                 rect=None)      # adjust subplots to fit into fig
ax.set_xlabel('xbla')            # set xlabel
ax.set_ylabel('ybla')            # set ylabel
ax.set_xlim(1, 2)                # sets x limits
ax.set_ylim(3, 4)                # sets y limits
ax.set_title('blabla')           # sets the axis title
ax.set(xlabel='bla')             # set multiple parameters at once
ax.legend(loc='upper center')    # activate legend
ax.grid(True, which='both')      # activate grid
bbox = ax.get_position()         # returns the axes bounding box
bbox.x0 + bbox.width             # bounding box parameters
 

# ---------------------------------------------------------------- #
#                        Plotting routines
# ---------------------------------------------------------------- #

ax.plot(x,y, '-o', c='red', lw=2, label='bla')  # plots a line
ax.scatter(x,y, s=20, c=color)                  # scatter plot
ax.pcolormesh(xx, yy, zz, shading='gouraud')    # fast colormesh
ax.colormesh(xx, yy, zz, norm=norm)             # slower colormesh
ax.contour(xx, yy, zz, cmap='jet')              # contour lines
ax.contourf(xx, yy, zz, vmin=2, vmax=4)         # filled contours
n, bins, patch = ax.hist(x, 50)                 # histogram
ax.imshow(matrix, origin='lower',
          extent=(x1, x2, y1, y2))              # show image
ax.specgram(y, FS=0.1, noverlap=128,
            scale='linear')                     # plot a spectrogram
ax.text(x, y, string, fontsize=12, color='m')   # write text