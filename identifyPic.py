from keras.applications.xception import Xception
from keras.models import load_model
import keras
from glob import glob
import numpy as np
import cv2 as cv
import os


# pre-process test images
# img_size = 299  # match Xception input size

class identifyPic(object):
    def __init__(self, path):
        self.path = path

    def load_test_images(self, file_list):
        test_set = list()
        test_set_rgb = list()
        for file in file_list:
            print(file)
            img = cv.imread(file)
            img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            test_set.append(img)
            test_set_rgb.append(img_rgb)

        return np.asarray(test_set), np.asarray(test_set_rgb)

    def predict(self):
        keras.backend.clear_session()
        # load test images
        test_dir = self.path
        filenames = glob(os.path.join(test_dir, '*.jpg'))
        images, images_rgb = self.load_test_images(filenames)

        # calculate from the training set
        channel_mean = np.array([110.73151039, 122.90935242, 136.82249855])
        channel_std = np.array([69.39734207, 67.48444001, 66.66808662])

        # normalize images
        images = images.astype('float32')
        for j in range(3):
            images[:, :, :, j] = (images[:, :, :, j] - channel_mean[j]) / channel_std[j]

        # make predictions
        print("================================")
        print("making predictions...")
        base_model = Xception(include_top=False, weights='imagenet', pooling='avg')
        iot_model = load_model('./model/iot_model_1553242985.h5')
        features = base_model.predict(images,batch_size=20)
        prediction = iot_model.predict(features,batch_size=20)

        print("==================================")
        print("nobody prob: ", prediction)
        return prediction


# if __name__ == '__main__':
#     import emailSender as emailSender
#     identifier = identifyPic(r"./raw/test/")
#     prediction = identifier.predict()
#     if prediction < 0.5:
#         mail_username='zh4055526@gmail.com'
#         mail_password='!1q@2w#3e'
#         # from_addr = mail_username
#         to_addrs="646618065@qq.com"
         
#         # HOST & PORT
#         HOST = 'smtp.gmail.com'
#         PORT = 587
         
#         # mail_username, mail_password, to_addrs, HOST, PORT
#         email = emailSender.emailSender(mail_username, mail_password, to_addrs, HOST, PORT)
#         email.send()