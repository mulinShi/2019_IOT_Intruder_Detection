# 2019_IOT_assignment1
# Classifier to judge if there are prople in the room
In order to practice the idea of transfer learning, I decided to work on this scene image classification project as an AI application for my IOT assignment one. 

# Dataset
I first built a small dataset consisting of 160 images. 

All the images are downloaded from Google and preprocessed.  There are 160 images in the training set (80 per class); 20 images (10 per class) in the validation set; 10 images  in the test set. The test set is left untouched during the training and tuning, and it is only used in the final step to assess the generalization of the model.

# Design
In this project, I used the pretrained CNN model Xception as the body, and build a custom head to decode the feature in the end. Xception is an improvement from Inception-V3. It has 79% Top-1 and 94.5% Top-5 accuracy on ImageNet. The pretrained model takes 299x299x3 image input and outputs a 2048x1 feature vector after global average pooling. Then I added a fully connected layer of 10 units and an output layer with 1 unit for binary classification. L2 regularization is used in both layers to prevent overfitting. Retraining is done using Keras with Tensorflow as backend.

# Preprocessing and augmentation
All the images are cropped to square and resized to 299x299 with OpenCV-Python as described in preprocessing.py. For convenience, the images are saved as numpy arrays in room_dataset.py. Images are then standardized to N(0, 1) on per channel basis. Since the dataset is very small, the training set is augmented, i.e. train images are randomly rotated, shifted, sheared, zoomed or flipped to some degree.

One trick I found particularly useful (for small dataset) is to do the augmentation beforehand and save the whole augmented data (e.g. for 20 epochs) with its corresponding labels. We can also use the pretrained model to extract feature vectors from these augmented data (aug_and_feature_extract.py).

In this way, we only need to compute for the two-layer head later on. In other words, we no longer need to do real time augmentation and calculate the whole model again and again (forward pass still time-consuming even though the Xception is non-trainable). This is useful when we are not sure about the hyper parameters and need to tune the model many times in the beginning. However, we might end up with limited variability because once we augment the data, we settle on it. For this specific project, it seems no issues with this approach so far.


