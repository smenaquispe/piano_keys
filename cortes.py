from pydub import AudioSegment
from pydub.silence import split_on_silence
import os

# Ruta del archivo de audio
audio_path = "audio2.mp3"

# Cargar el audio
audio = AudioSegment.from_file(audio_path, format="mp3")

# Configuración para el corte en los vacíos de sonido
min_silence_len = 700  # Duración mínima del silencio para considerar un corte (en milisegundos)
silence_thresh = audio.dBFS - 14  # Umbral de silencio (basado en el nivel promedio de dBFS del audio)
keep_silence = 500  # Tiempo de silencio a mantener en cada lado del segmento

# Cortar el audio en segmentos basados en los vacíos
audio_chunks = split_on_silence(
    audio,
    min_silence_len=min_silence_len,
    silence_thresh=silence_thresh,
    keep_silence=keep_silence
)

# Crear una carpeta para guardar los segmentos
output_folder = "output_audio_segments"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Guardar cada segmento en la carpeta
for i, chunk in enumerate(audio_chunks):
    segment_path = os.path.join(output_folder, f"segment_{i+1}.mp3")
    chunk.export(segment_path, format="mp3")
    print(f"Guardado: {segment_path}")

print("Corte de audio completado y segmentos guardados.")
