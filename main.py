from PIL import Image
import os
import concurrent.futures

def mirror_image(image_path):
    try:
        original_image = Image.open(image_path)
        mirrored_image = original_image.transpose(Image.FLIP_LEFT_RIGHT)
        new_filename = f"копия_{os.path.basename(image_path)}"
        new_image_path = os.path.join(os.path.dirname(image_path), new_filename)
        mirrored_image.save(new_image_path)
    except IOError:
        print(f"Ошибка. Не удается открыть изображение: {image_path}")

def mirror_images_in_directory(directory):
    image_paths = [os.path.join(directory, filename) for filename in os.listdir(directory)
                   if filename.endswith(".jpg") or filename.endswith(".png") or
                   filename.endswith(".jpeg") or filename.endswith(".gif") or
                   filename.endswith(".bmp")]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(mirror_image, image_paths)

if __name__ == "__main__":
    directory_path = "D:/PythonProject/PythonImage"
    mirror_images_in_directory(directory_path)
