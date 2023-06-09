from moviepy.editor import VideoFileClip
from colorama import (
	init,
	Fore,
	Back
)

import os
import datetime

from list_of_video_extensions import list_of_video_extensions


# Инициализируем colorama.
init(autoreset=True)


def counts_duration_of_video_file(file):
	"""Обрабатывает видео файл и выводит информацию о нем."""

	# Проверка на то, что был передан видео файл.
	if os.path.splitext(file)[1] not in list_of_video_extensions:
		
		print(Fore.RED + f'\nПростите, но мы не можем обработать файл "{file}" с таким расширением.')

	else:

		# Продолжительность видео.
		video_duration = VideoFileClip(file).duration
	
		# Дата создания видео.
		video_creation_date = datetime.datetime.fromtimestamp(
			int(os.path.getctime(file))
		)

		# Дата последнего изменения.
		date_video_was_last_modified = datetime.datetime.fromtimestamp(
			int(os.path.getmtime(file))
		)

		# Размер видео.
		video_file_size_in_mb = os.path.getsize(file) // 1024**2
	
		# Выводим все данные красиво в консоль.
		print(Fore.BLACK + Back.WHITE + f"\nПродолжительность видео: {video_duration}"\
			f"\nДата создаиня видео: {video_creation_date}"
			f"\nДата последнего изменения видео: {date_video_was_last_modified}"\
			f"\nРазмер видео файла в МБ: {video_file_size_in_mb}")