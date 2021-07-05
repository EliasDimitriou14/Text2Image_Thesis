import image_slicer
import path
import shutil
import os

# set the number of images you want sliced
n_images = 21
for counter in range(n_images):
    # slice the images with the given format
    image_slicer.slice('train_samples/train_{:02d}.png'.format(counter), 64)

# define source directory of sliced images
src = "train_samples"
# define destination directory for the slices
dst = "train_samples_sliced"
# create the destination directory to save slices of the image
if not os.path.exists(dst):
 os.mkdir(dst)
else:
    print('Directory for sliced samples already exists.Using the one created already...')


for counter in range(n_images):
    # take all the files from source directory with the given prefix and save them to files list variable
    files = [i for i in os.listdir(src) if i.startswith("train_{:02d}_".format(counter)) and os.path.isfile(os.path.join(src, i))]
    for f in files:
        # move all the right files to destination directory
        shutil.move(os.path.join(src, f), dst)
