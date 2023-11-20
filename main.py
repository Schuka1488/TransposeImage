from PIL import Image
import os

def mirror_images_in_directory(directory):
    for filename in os.listdir(directory):  # Перебираем файлы в указанной директории
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(directory, filename)  # Получаем путь к изображению
            original_image = Image.open(image_path)  # Открываем изображение
            mirrored_image = original_image.transpose(Image.FLIP_LEFT_RIGHT)  # Отзеркаливаем изображение
            new_filename = f"копия_{filename}"  # Создаем новое имя файла
            new_image_path = os.path.join(directory, new_filename)
            mirrored_image.save(new_image_path)  # Сохраняем отраженную копию в указанной директории

if __name__ == "__main__":
    directory_path = "D:/PythonProject/PythonImage"
    mirror_images_in_directory(directory_path)

