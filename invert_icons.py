from PIL import Image, ImageOps
import os

image_dir = "images"
for file in os.listdir(image_dir):
    if file.endswith(".png"):
        path = os.path.join(image_dir, file)
        image = Image.open(path).convert("RGBA")
        r, g, b, a = image.split()
        inverted = ImageOps.invert(Image.merge("RGB", (r, g, b)))
        final = Image.merge("RGBA", (*inverted.split(), a))
        final.save(os.path.join(image_dir, f"inverted_{file}"))

print("✅ All icons inverted and saved as 'inverted_*.png'")
