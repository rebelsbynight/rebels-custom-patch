# Rebels Custom Patch Creation

Welcome to the Rebels Custom Patch Creation repository! This README provides step-by-step instructions to get you up and running with the tools and dependencies necessary to use the project. No prior technical knowledge is required. We've broken down the setup process for macOS, Linux, and Windows users.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [MacOS](#macos)
  - [Linux](#linux)
  - [Windows (WIP)](#windows-wip)
- [Rendering the Full Collection](#rendering-the-full-collection)
  - [MacOS](#macos-rendering)
  - [Linux](#linux-rendering)
- [Support](#support)

---

## Prerequisites

1. **git** - A tool for version control.
2. **Python3** - The programming language we'll use.
3. **Blender 3.1.2** - The 3D modeling tool for our patches.
4. **coreutils** - Provides access to the "timeout" command.

---

## Setup

### MacOS

1. Install **brew** (Homebrew) - A package manager for macOS.
    ```
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. Install **Python3** via brew:
    ```
    brew install python3
    ```

3. Install **Blender 3.1.2** from their [official website](https://www.blender.org/download/).

4. Install **coreutils**:
    ```
    brew install coreutils
    ```

5. Clone the project:
    ```
    git clone https://github.com/rebelsbynight/rebels-custom-patch
    cd rebels-custom-patch
    ```

6. Download the Rebels Patches 3D files:
   Navigate to the given URL (`<FIXME>`) in your browser and download the `Rebels-Patches.zip`.

7. Unzip the archive in the current directory:
    ```
    unzip Rebels-Patches.zip
    ```

### Linux

1. Install **Python3**:
    ```
    sudo apt update
    sudo apt install python3 python3-pip
    ```

2. Install **Blender 3.1.2**:
    ```
    sudo add-apt-repository ppa:thomas-schiex/blender
    sudo apt-get update
    sudo apt-get install blender
    ```

3. Clone the project:
    ```
    git clone https://github.com/rebelsbynight/rebels-custom-patch
    cd rebels-custom-patch
    ```

4. Download and unzip the Rebels Patches 3D files:
    ```
    wget <FIXME>
    unzip Rebels-Patches.zip
    ```

### Windows (WIP)

> **Note:** Windows setup is still in progress. We recommend using a macOS or Linux machine for now.

---

## Rendering the Full Collection

### MacOS Rendering

Run the command:

```
python3 generate-patches.py --output_patches_filepath ./rendered-patches --output_image_filepath ./rendered-patches --blender_application /Applications/Blender.app/Contents/MacOS/Blender --patch_nft_blender_file ./Rebels-Patches/Rebels_All_Patches-custom-nft.blend --blender_python_nft_generation_script ./blender-script/gen-custom-patches.py --full_patches_hats_csv_filepath ./csv/patches-hats.csv --full_patches_clothes_csv_filepath ./csv/patches-clothes.csv --full_patches_csv_filepath ./csv/patches.csv --image_filepath <image_to_use_for_patches>
```

### Linux Rendering

Run the command:

```
python3 generate-patches.py --output_patches_filepath ./rendered-patches --output_image_filepath ./rendered-patches --blender_application $(which blender) --patch_nft_blender_file ./Rebels-Patches/Rebels_All_Patches-custom-nft.blend --blender_python_nft_generation_script ./blender-script/gen-custom-patches.py --full_patches_hats_csv_filepath ./csv/patches-hats.csv --full_patches_clothes_csv_filepath ./csv/patches-clothes.csv --full_patches_csv_filepath ./csv/patches.csv --image_filepath <image_to_use_for_patches>
```

## Understanding the Rendering Command

The provided rendering command is tailored to generate custom patches using our proprietary Blender script. Let's break it down:

- `generate-patches.py`: This is the main script that orchestrates the whole rendering process.
- `--output_patches_filepath ./rendered-patches`: Specifies where the rendered 3D model files of the patches will be saved.
- `--output_image_filepath ./rendered-patches`: Dictates where the rendered image previews of these patches will be saved.
- `--blender_application`: Points to the Blender application's executable file. Depending on your OS, the location of this file will vary.
- `--patch_nft_blender_file ./Rebels-Patches/Rebels_All_Patches-custom-nft.blend`: Specifies the Blender file that contains the 3D models of the patches.
- `--blender_python_nft_generation_script ./blender-script/gen-custom-patches.py`: Indicates the Python script that Blender will use to generate the custom patches. This script automates the process inside Blender.
- `--full_patches_hats_csv_filepath ./csv/patches-hats.csv`: Points to a CSV file that contains information about various hat designs for the patches.
- `--full_patches_clothes_csv_filepath ./csv/patches-clothes.csv`: Indicates a CSV file with data about different clothes designs for the patches.
- `--full_patches_csv_filepath ./csv/patches.csv`: This is a CSV file containing data about the patches themselves.
- `--image_filepath <image_to_use_for_patches>`: You need to replace `<image_to_use_for_patches>` with the path to the image you want to use as a texture or design for the patches.

When you run this command, the script interfaces with Blender, leverages the provided Python script to automate the rendering process, and eventually produces both 3D models and image previews of the custom patches, saving them to the specified directories.


## License
The code and 3D files can used in any way you'd like so long as it's applied for the Rebels project and Rebels NFTs, any other use is prohibited.

---

Thank you for being a part of the Rebels community! Enjoy creating your custom patches! 🚀

