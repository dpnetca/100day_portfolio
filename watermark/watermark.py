import os

from PIL import Image, ImageDraw, UnidentifiedImageError


class WaterMark:
    """Add watermark to one or more images"""

    def __init__(self, mark, mark_color, out_prefix):
        self.mark = mark
        self.mark_color = mark_color
        self.out_prefix = out_prefix
        self.out_folder = None

    def mark_image(self, image):
        """Open image and add watermark to bottom left and save as new file

        Args:
            image (string): image filename
        """
        with Image.open(image) as im:
            draw = ImageDraw.Draw(im)
            mark_x = 5
            mark_y = im.size[1] - 10

            draw.text((mark_x, mark_y), self.mark, fill=self.mark_color)
            if self.out_folder:
                out_file = os.path.join(
                    self.out_folder, f"{self.out_prefix}-{image}"
                )
            else:
                out_file = f"{self.out_prefix}-{image}"
            im.save(out_file)

    def mark_images(self, image_folder):
        """Get a list of all files in folder and pass them to mark image method

        Args:
            image_folder (str): folder name
        """
        image_list = [
            f
            for f in os.listdir(image_folder)
            if os.path.isfile(os.path.join(image_folder, f))
        ]
        self.out_folder = image_folder
        for image in image_list:
            # don't watermark images that are already watermarked
            if image.startswith(self.out_prefix):
                print(f"skipping {image}: already marked")
                continue
            # mark images, and handle errors if folder contains non-image files
            try:
                self.mark_image(image)
            except UnidentifiedImageError as e:
                print(f"skipping {image}: {e}")
