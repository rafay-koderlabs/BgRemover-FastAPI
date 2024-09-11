from transformers import pipeline
from PIL import Image

# Load the image
image_path = "person.jpg"

# Create the pipeline
pipe = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)

# Get the mask
pillow_mask = pipe(image_path, return_mask=True)
pillow_mask.save("output_mask.png")

# Get the image with background removed
pillow_image = pipe(image_path)
pillow_image.save("output_image.png")

print("Processing complete. Check 'output_mask.png' for the mask and 'output_image.png' for the image with background removed.")