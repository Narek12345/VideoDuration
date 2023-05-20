import os

from project_functions import (
	counts_duration_of_video_file,
	counts_duration_of_video_files_from_folder
)


def start():

	# Путь к видео или к папке с видео.
	path_to_video_or_video_folder = input("Введите местонахождение видео или же папку с видео: ").replace('"', "")

	# Находим переданный обьект.
	if os.path.exists(path_to_video_or_video_folder):
	
		# Проверка на то, что был передан файл, а не папка.
		if os.path.isfile(path_to_video_or_video_folder):

			# Вызваем функцию обработчик переданного файла.
			counts_duration_of_video_file.counts_duration_of_video_file(path_to_video_or_video_folder)

		# Проверка на то, что была передана папка, а не файл.
		elif os.path.isdir(path_to_video_or_video_folder):

			# Вызываем функцию обработчик переданного каталога.
			counts_duration_of_video_files_from_folder.	counts_duration_of_video_files_from_folder(path_to_video_or_video_folder)

	else:
		print("Путь не найден")


if __name__ == '__main__':
	start()