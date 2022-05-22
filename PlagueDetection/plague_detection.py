import cv2
import numpy as np

'''
@@Author Willian Antunes
https://github.com/brwillian/plague_detection
'''


class PlagueDetection:
    def __init__(self, img):
        self.h = img.shape[0]
        self.w = img.shape[1]

    def preprocess_image(self, img):
        '''
            Blurs image and converts to HSV color scale for better detection of the weeds
        '''
        # gamma correction
        img = np.array(255 * (img / 255) ** 3, dtype='uint8')
        kernel_size = 15
        # blur image
        img_blur = cv2.medianBlur(img, kernel_size, 0)

        # convert to HSV color scale
        img_hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)

        return img_hsv

    @staticmethod
    def create_mask(img_hsv):
        '''
            Create a mask containing only green colored pixels
        '''
        sensitivity = 25
        lower_bound = np.array([60 - sensitivity, 80, 50])
        upper_bound = np.array([60 + sensitivity, 255, 255])

        # create mask
        msk = cv2.inRange(img_hsv, lower_bound, upper_bound)

        return msk

    @staticmethod
    def transform_image(msk):
        '''
            Perform morphology transformation in the binary image
        '''
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

        # erosion and dilation
        res_msk = cv2.morphologyEx(msk, cv2.MORPH_OPEN, kernel)
        res_msk = cv2.morphologyEx(res_msk, cv2.MORPH_CLOSE, kernel)

        return res_msk

    @staticmethod
    def draw_mask_color(img, msk):
        '''
            Create a mask containing original backgroud image
        '''
        colored_portion = cv2.bitwise_or(img, img, mask=msk)

        # create and invert mask to black color
        msk_inv = cv2.bitwise_not(msk)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # create 3 channels in gray image
        gray_portion = cv2.bitwise_or(gray, gray, mask=msk_inv)
        gray_portion = np.stack((gray_portion,) * 3, axis=-1)

        mask_with_color = colored_portion + gray_portion

        return mask_with_color

    @staticmethod
    def draw_anchors(mask):
        pass


    @staticmethod
    def show_image(img):
        cv2.imshow('nome', img)
        cv2.waitKey(0)


if __name__ == "__main__":
    # Debug Project

    img = cv2.imread('../data/usa.jpg')
    wd = PlagueDetection(img)
    img_hsv = wd.preprocess_image(img)
    msk = wd.create_mask(img_hsv)
    msk = wd.transform_image(msk)

    output = wd.draw_mask_color(img, msk)

    cv2.imshow('Mask', output)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
