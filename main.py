import moviepy.editor
from pathlib import Path

filename = 'wh40k.mp4'

# получить путь к видеофайлу
video_file = Path(filename)

# получаем данные видео с помощью библиотеки
video = moviepy.editor.VideoFileClip(f'{video_file}')
# получаем данные аудио из объекта
audio = video.audio
# записываем аудио в файл
audio.write_audiofile(f'{video_file.stem}.mp3')