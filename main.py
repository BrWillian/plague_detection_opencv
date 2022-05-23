import argparse
import cv2
from PlagueDetection import PlagueDetection


def main():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('--sensitivity', type=int, help='Sensibilidade do detector', default=30)
    parser.add_argument('--circles', type=bool, help='Desenhar ou não circulo nas detecções', default=False)
    parser.add_argument('--image', type=str, help='Caminho da imagem', required=True)

    args = parser.parse_args()

    # Load image
    img_path = cv2.imread(args.image)

    # Create object instance
    plague_detection = PlagueDetection(img_path, circles=args.circles, sensitivity=args.sensitivity)

    # Get image from preprocess output
    img_hsv = plague_detection.preprocess_image(img_path)

    # Get mask
    msk = plague_detection.create_mask(img_hsv)

    # Get mask before morphology transformation
    msk = plague_detection.transform_image(msk)

    # Get mask with drawings
    result = plague_detection.draw_mask_color(msk, img_path)

    # Show result
    plague_detection.show_image(result)


if __name__ == "__main__":
    main()
