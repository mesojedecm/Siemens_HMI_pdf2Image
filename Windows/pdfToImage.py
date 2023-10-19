import glob, os
from PIL import Image
from pdf2image import convert_from_path


# Adjust the path to your Poppler installation on Linux
poppler_path = poppler_path = r"C:\Users\matej.mesojedec\Desktop\pdf2image\poppler-23.08.0\Library\bin"  

# Use the correct folder path to your PDF files
pdf_directory = r'C:\Users\matej.mesojedec\Desktop\pdf2image\Linux\pdf'

# Set image size after resizing
small_size = (400, 290)

######################### pdf2image ###########################

pdf_filenames = glob.glob(pdf_directory + '*.pdf')
crop_filenames = glob.glob(pdf_directory + '*.jpg')

for pdf_filename in pdf_filenames:
    images = convert_from_path(pdf_filename, poppler_path=poppler_path)
    for i, image in enumerate(images):
        image.save(f"{pdf_filename[:-4]}_{i}.jpg", 'JPEG')

######################### crop ###########################

# Define the directory where your JPEG images are located
image_directory = pdf_directory

# Use glob to get a list of JPEG files in the directory
jpeg_files = glob.glob(image_directory + '*.jpg')

# Define a function to crop an image
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

        # Crop the image
        crop = img.crop((left, top, right, bottom))
        
        # Save original image
        crop.save(image_path[:-4] + '_screen_big.jpg', 'JPEG')
        
        # Resize original image
        resize = crop.resize(small_size)
        
        # Save resized image
        resize.save(image_path[:-4] + '_screen_small.jpg', 'JPEG')

        # Remove original pdf
        os.remove(image_path)

        print(f"Cropped {image_path}.")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")

# Loop through each JPEG file and crop
for jpeg_file in jpeg_files:
    crop_image(jpeg_file)

    