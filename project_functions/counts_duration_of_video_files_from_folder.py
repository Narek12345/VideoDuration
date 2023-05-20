from moviepy.editor import VideoFileClip

import os

from list_of_video_extensions import list_of_video_extensions


def counts_duration_of_video_files_from_folder(folder):
	"""Обрабатывает переданную папку, и если тама есть видео, то выводит сумму их продолжительности."""
	
	# Общая сумма продолжительности всех видео.
	DURATION_ALL_VIDEOS = 0
	# Количесто видео, которые были обработаны.
	NUMBER_VIDEOS = 0

	# Разбираем все файлы в переданном каталоге.
	for file in os.listdir(folder):

		# Проверяем, является ли расширение файла расширением для видео.
		if os.path.splitext(file)[1] in list_of_video_extensions:

			# Собираем абсолютный путь к видео из 2 частей.
			absolute_path = os.path.join(folder, file)

			# Суммируем продолжительность видео.
			DURATION_ALL_VIDEOS += VideoFileClip(absolute_path).duration

			# Добавляем еще одно единицу в кол. обрабатываемых видео.
			NUMBER_VIDEOS += 1
	else:
		# Проверяем чтобы был обработан хотя бы 1 файл.
		if NUMBER_VIDEOS > 0:
			# Вывдоим красиво результат.
			print(DURATION_ALL_VIDEOS, NUMBER_VIDEOS)
		else:
			print("\nПростите, но в этом каталоге не находится ни одного файла, который мы могли бы обработать.")