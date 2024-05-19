# Background-Image-Remover
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/shabir-mp/Image-Background-Remover/blob/main/LICENSE)

A simple Python script to remove the background from an image using the rembg library. This script is useful for quickly and easily removing the background from an image, which can be useful for a variety of purposes such as creating transparent images or replacing the background with a different image.

## Usage
1. Save this script as a Python file (e.g. background_remover.py or main.py).
2. Run the script from the command line: `python background_remover.py` or your file name.
3. Enter the path to the input image when prompted. This can be an absolute or relative path to the image file.
4. Enter the desired output path for the background-removed image. This can also be an absolute or relative path.
5. Optionally, enter Y to open the output image after processing. This will open the image using the default image viewer for your system.

## Requirements
1. rembg library (install with `pip install rembg`)
2. PIL library (install with `pip install pillow`)

## How it Works
The script uses the rembg library to remove the background from the input image. The rembg library uses a deep learning model to automatically remove the background from an image, leaving only the foreground objects. The resulting image is then saved to the specified output path. If desired, the script can also open the output image using the PIL library.

## Example
```
$ python background_remover.py
Image Path: /path/to/input/image.jpg
Output Path: /path/to/output/image.png
Open image after when finished? (Y/n): Y
Background Removed Successfully !
```

## Note
This script assumes that the input image is in a format that can be read by PIL. If you encounter issues with certain image formats, you may need to modify the script accordingly.

Additionally, the rembg library may not be able to perfectly remove the background from all images. In some cases, the foreground objects may be partially removed or the edges may be jagged. If you need more precise background removal, you may need to use a more advanced image editing tool or library.

Finally, this script is intended for use with images that have a clear distinction between the foreground and background. If the input image has a complex background or overlapping objects, the results may not be as expected.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

-----------------------------------------------------------------------------------------
![Github Footer](https://github.com/shabir-mp/Kereta-Api-Indonesia-Booking-System/assets/133546000/c1833fe4-f470-494f-99e7-d583421625be)

