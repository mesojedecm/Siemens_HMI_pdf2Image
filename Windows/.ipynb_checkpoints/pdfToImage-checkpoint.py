import glob, os
from PIL import Image
from pdf2image import convert_from_path

new_size = (370, 260)

######################### pdf2image ###########################
# Adjust the path to your Poppler installation on Fedora
#poppler_path = r"C:\Users\matej.mesojedec\Desktop\pdf2image\poppler-23.08.0\Library\bin"  # The default installation path on Fedora

# Use the correct folder path to your PDF files
pdf_directory = r'C:\Users\matej.mesojedec\Desktop\pdf2image\Linux\pdf'


pdf_filenames = glob.glob(pdf_directory + '*.pdf')

for pdf_filename in pdf_filenames:
    images = convert_from_path(pdf_filename, poppler_path=poppler_path)
    for i, image in enumerate(images):
        image.save(f"{pdf_filename[:-4]}_{i}.jpg", 'JPEG')

######################### crop ###########################

# Define the directory where your JPEG images are located
image_directory = pdf_directory

# Use glob to get a list of JPEG files in the directory
jpeg_files = glob.glob(image_directory + '*.jpg')

# Define a function to crop an image into halves
def crop_image(image_path):
    try:
        # Open the image using PIL (Python Imaging Library)
        img = Image.open(image_path)

        # Get the width and height of the image
        width, height = img.size

        # Calculate the coordinates for cropping
        left = 42
        top = 35
        right = width - 37
        bottom = 970 # Crop the image into halves

        # Crop the top half
        top_half = img.crop((left, top, right, bottom))
        top_half = top_half.resize(new_size)
        top_half.save(image_path[:-4] + '_screen.jpg', 'JPEG')

        os.remove(image_path)
        print(f"Cropped {image_path} into halves.")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")

# Loop through each JPEG file and crop it into halves
for jpeg_file in jpeg_files:
    crop_image(jpeg_file)
    