# Text2Image_Thesis


This repository contains ONLY the code of the thesis.Some useful files may be found at the links below.

# Implementation
This implementation makes  use of  the algorithm of CLS-GAN and StackGAN found at:https://github.com/hellochick/text-to-image		


![architecture](https://user-images.githubusercontent.com/75016825/124499785-47564a80-ddc7-11eb-9e7b-c87c9ee95c5e.jpeg)


# Prepare Data
Download image files and captions from [Google Drive](https://drive.google.com/drive/folders/1aUJrBoIN3l9U5p5pNXT0NeNzlyBWF54u?usp=sharing), put into ./text-to-image directory


# Evaluation Metrics
I have also added the implemantation of IS and FID from:https://github.com/tsc2017/Frechet-Inception-Distance,
https://github.com/tsc2017/Inception-Score having made some adjustments to the code

* fid_score.py
* inception_score.py

# Slice images & store
I also have added some more code of my own for image slicing and storing in files

* slice_and_move.py

# Sample image(21  epochs)

![train5_20](https://user-images.githubusercontent.com/75016825/124499724-2aba1280-ddc7-11eb-9921-1e64116a71fc.png)
