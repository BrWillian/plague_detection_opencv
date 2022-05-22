import argparse
import cv2
from PlagueDetection import PlagueDetection


def main():
    img = cv2.imread('data/usa.jpg')
    wd = PlagueDetection(img)
    img_hsv = wd.preprocess_image(img)
    msk = wd.create_mask(img_hsv)
    msk = wd.transform_image(msk)
    res_msk = cv2.bitwise_and(img, img, mask=msk)
    cv2.imshow('Mask', res_msk)
    cv2.waitKey()
    cv2.imshow('Frame', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
