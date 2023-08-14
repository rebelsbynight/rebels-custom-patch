import os
import argparse
import subprocess
from PIL import Image, ImageDraw, ImageOps

def round_corners_and_darken(image_path, output_path):
    # Load image
    img = Image.open(image_path)

    # Convert image to RGB (removes alpha if any)
    img = img.convert("RGB")

    # Darken the image
    img = ImageOps.autocontrast(img, cutoff=10)

    # Make corners round
    radius = min(img.size) // 5
    circle_img = Image.new('L', (radius * 2, radius * 2), 0)
    draw = ImageDraw.Draw(circle_img)
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)
    alpha = Image.new('L', img.size, "white")
    w, h = img.size
    alpha.paste(circle_img.crop((0, 0, radius, radius)), (0, 0))
    alpha.paste(circle_img.crop((0, radius, radius, radius * 2)), (0, h - radius))
    alpha.paste(circle_img.crop((radius, 0, radius * 2, radius)), (w - radius, 0))
    alpha.paste(circle_img.crop((radius, radius, radius * 2, radius * 2)), (w - radius, h - radius))

    # Merge the alpha with the RGB image
    img.putalpha(alpha)

    # Save the image
    img.save(output_path)

    return output_path


def create_directory(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def run_blender(blender_app, blender_file, blender_py_script, patches_hats, patches_clothes, patches, updated_image, output_patches_filepath):
    subprocess.call([blender_app, "-b", blender_file, "--engine", "BLENDER_EEVEE", "-P", blender_py_script, "--",
                     patches_hats, patches_clothes, patches, updated_image, output_patches_filepath])

def main(args):
    create_directory(args.output_patches_filepath)

    # Round corners and darken
    output_image_path = round_corners_and_darken(args.image_filepath, args.output_image_filepath)

    # Run Blender script
    run_blender(args.blender_application, args.patch_nft_blender_file, args.blender_python_nft_generation_script,
                args.full_patches_hats_csv_filepath, args.full_patches_clothes_csv_filepath,
                args.full_patches_csv_filepath, output_image_path, args.output_patches_filepath)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Image paths
    parser.add_argument("--image_filepath", type=str, required=True)
    parser.add_argument("--output_patches_filepath", type=str, required=True)
    parser.add_argument("--output_image_filepath", type=str, required=True)

    # Blender application and scripts
    parser.add_argument("--blender_application", type=str, required=True)
    parser.add_argument("--patch_nft_blender_file", type=str, required=True)
    parser.add_argument("--blender_python_nft_generation_script", type=str, required=True)

    # Full CSV filepaths
    parser.add_argument("--full_patches_hats_csv_filepath", type=str, required=True)
    parser.add_argument("--full_patches_clothes_csv_filepath", type=str, required=True)
    parser.add_argument("--full_patches_csv_filepath", type=str, required=True)

    args = parser.parse_args()
    main(args)

