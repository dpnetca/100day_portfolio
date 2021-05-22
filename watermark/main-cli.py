#!/usr/bin/env python
import argparse
from watermark import WaterMark


def main(args):

    mark = args.mark
    mark_color = args.color

    watermark = WaterMark(mark, mark_color, args.out)
    if args.folder:
        watermark.mark_images(args.folder)
    else:
        watermark.mark_image(args.file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add image watermark")
    in_group = parser.add_mutually_exclusive_group(required=True)
    in_group.add_argument("-f", "--file", help="Single File to Mark")
    in_group.add_argument("-F", "--folder", help="Mark all images in folder")
    parser.add_argument("-m", "--mark", help="Text to mark", required=True)
    parser.add_argument(
        "-o", "--out", help="File output prefix", default="out"
    )
    parser.add_argument(
        "-c", "--color", help="watermark color", default="green"
    )
    args = parser.parse_args()
    main(args)
