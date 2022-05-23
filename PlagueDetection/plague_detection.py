import cv2
import numpy as np
import random

'''
@@Author Willian Antunes
https://github.com/brwillian/plague_detection_opencv
'''


class PlagueDetection:
    def __init__(self, img, **kwargs):
        self._sensitivity = kwargs.get("sensitivity") if kwargs.get("sensitivity") else 30
        self._with_circles = kwargs.get("circles") if kwargs.get("circles") else False
        self._save_result = kwargs.get("save") if kwargs.get("save") else False

    def preprocess_image(self, img):
        '''
            Blurs image and converts to HSV color scale for better detection of the weeds
        '''
        # gamma correction
        img = np.array(255 * (img / 255) ** 3, dtype='uint8')
        kernel_size = 17
        # blur image
        img_blur = cv2.medianBlur(img, kernel_size, 0)

        # convert to HSV color scale
        img_hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)

        return img_hsv

    def create_mask(self, img_hsv):
        '''
            Create a mask containing only green colored pixels
        '''
        lower_bound = np.array([60 - self._sensitivity, 80, 50])
        upper_bound = np.array([60 + self._sensitivity, 255, 255])

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

        res_msk = cv2.medianBlur(res_msk, 7)

        return res_msk

    def draw_mask_color(self, mask, img):
        '''
            Create a mask filters on circles or not
        '''
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Get plagues
        analysis = cv2.connectedComponentsWithStats(mask,
                                                    4,
                                                    cv2.CV_32S)

        # Separe componets
        (totalLabels, label_ids, values, centroid) = analysis

        if self._with_circles:
            # Draw index and circles on plagues
            label_hue = np.zeros(gray.shape, np.uint8)

            for index, cord in enumerate(centroid):
                x, y = cord
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                cv2.circle(label_hue, (int(x), int(y)), 26, color, -1)
                cv2.putText(gray, str(index + 1), (int(x) - 7, int(y) + 7), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2,
                            cv2.LINE_AA)
        else:
            # Draw masks randon colors
            label_hue = np.uint8(179 * label_ids / np.max(label_ids))
            for index, cord in enumerate(centroid):
                x, y = cord
                cv2.putText(gray, str(index + 1), (int(x) + 10, int(y) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 1,
                            cv2.LINE_AA)
                cv2.drawMarker(gray, (int(x), int(y)), (255, 255, 255), cv2.MARKER_CROSS, 35, 2)

        # create hsv mask
        blank_ch = 255 * np.ones_like(label_hue)
        labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

        labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
        labeled_img[label_hue == 0] = 0

        gray_portion = np.stack((gray,) * 3, axis=-1)

        # add opacity on circles
        masked_cirles = cv2.addWeighted(gray_portion, 1, labeled_img, 0.25, 0)

        return masked_cirles

    @staticmethod
    def show_image(img):
        cv2.imshow('nome', img)
        cv2.waitKey(0)