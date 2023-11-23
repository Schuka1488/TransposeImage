import os
import concurrent.futures
from PIL import Image
import time

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
    image_paths = []
    for dirpath, dirnames, filenames in os.walk(directory):
        image_paths.extend([os.path.join(dirpath, filename) for filename in filenames
                       if filename.endswith(".jpg") or filename.endswith(".png") or
                       filename.endswith(".jpeg") or filename.endswith(".gif") or
                       filename.endswith(".bmp")])

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_path = {executor.submit(mirror_image, image_path): image_path for image_path in image_paths}
        total_images = len(image_paths)
        processed_images = 0
        start_time = time.time()
        for future in concurrent.futures.as_completed(future_to_path):
            processed_images += 1
            try:
                data = future.result()
            except Exception as exc:
                print(f"Ошибка обработки изображения {future_to_path[future]}: {exc}")
            else:
                print(f"Изображение обработано: {future_to_path[future]}")
            finally:
                progress_bar(processed_images, total_images, start_time)

def progress_bar(processed_images, total_images, start_time):
    progress = (processed_images / total_images) * 100
    elapsed_time = time.time() - start_time
    time_left = elapsed_time * (total_images / processed_images - 1)
    print(f"Прогресс: {progress:.2f}% | Обработано: {processed_images}/{total_images} | Осталось: {time_left:.2f} сек.")

if __name__ == "__main__":
    directory_path = "D:/PythonProject/PythonImage"
    mirror_images_in_directory(directory_path)
