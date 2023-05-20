from moviepy.editor import VideoFileClip
from colorama import(
	init,
	Fore,
	Back
)

import os

from list_of_video_extensions import list_of_video_extensions


# Инициализируем colorama.
init(autoreset=True)


def counts_duration_of_video_files_from_folder(folder):
	"""Обрабатывает переданную папку, и если тама есть видео, то выводит сумму их продолжительности."""

	# Общая сумма продолжительности всех видео.
	DURATION_ALL_VIDEOS = 0
	# Количесто видео, которые были обработаны.
	NUMBER_VIDEOS = 0

	# Разбираем все файлы в переданном каталоге.
	for file in os.listdir(folder):

		# Проверяем, является ли расширение файла расширением для видео.
		if os.path.splitext(file)[1] not in list_of_video_extensions:

			continue

		else:
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
			print(Fore.BLACK + Back.WHITE + f"\nПродолжительность всех видео в сумме: {round(DURATION_ALL_VIDEOS)}"\
				f"\nКоличество видео: {NUMBER_VIDEOS}")
		else:
			print(Fore.RED + "\nПростите, но в этом каталоге не находится ни одного файла, который мы могли бы обработать.")