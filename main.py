from moviepy.editor import VideoFileClip

import os
import datetime

from list_of_video_extensions import list_of_video_extensions


VIDEO_DURATION = 0


def counts_video_duration(file_folder_path, video):
	"""Считает продолжительность видео и суммирует."""

	global VIDEO_DURATION

	# Собираем абсолютный путь к видео из 2 частей.
	absolute_path = os.path.join(file_folder_path, video)
	
	# Сохраняем видео в готовом и удобном нам обьекте.
	video = VideoFileClip(absolute_path)

	# Суммируем продолжительность видео.
	VIDEO_DURATION += video.duration



# Путь к видео или к папке с видео.
path_to_video_or_video_folder = input("Введите местонахождение видео или же папку с видео: ").replace('"', "")

# Находим переданный обьект.
if os.path.exists(path_to_video_or_video_folder):

	# Проверка на то, что был передан файл, а не папка.
	if os.path.isfile(path_to_video_or_video_folder):
		# Сохраняем видео в готовом и удобном нам обьекте.
		video = VideoFileClip(path_to_video_or_video_folder)

		# Продолжительность видео.
		video_duration = video.duration

		# Дата создания видео.
		video_creation_date = datetime.datetime.fromtimestamp(
			int(os.path.getctime(path_to_video_or_video_folder))
		)

		# Дата последнего изменения.
		date_video_was_last_modified = datetime.datetime.fromtimestamp(
			int(os.path.getmtime(path_to_video_or_video_folder))
		)

		# Размер видео.
		video_file_size_in_mb = os.path.getsize(path_to_video_or_video_folder) // 1024**2

		print(f"Продолжительность видео: {video_duration}\n"\
				f"Дата создания видео: {video_creation_date}\n"\
				f"Дата последнего изменения: {date_video_was_last_modified}\n"\
				f"Размер видео файла в мб: {video_file_size_in_mb}")

	# Проверка на то, что была передана папка, а не файл.
	elif os.path.isdir(path_to_video_or_video_folder):
		print("Список: ", os.listdir(path_to_video_or_video_folder))

		# Разбираем все файлы в переданном каталоге (не рекурсивно).
		for file in os.listdir(path_to_video_or_video_folder):

			# Проверяем, является ли расширение файла расширением для видео.
			if os.path.splitext(file)[1] in list_of_video_extensions:
				counts_video_duration(path_to_video_or_video_folder, file)

else:
	print("Путь не найден")


print(VIDEO_DURATION)