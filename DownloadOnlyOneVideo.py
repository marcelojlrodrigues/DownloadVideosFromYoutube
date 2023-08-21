from pytube import YouTube

link="https://www.youtube.com/watch?v=Je4Ggx4jRp8"

yt = YouTube(link)
try:
    video = yt.streams.get_highest_resolution()  # Altere a qualidade se necessário
    print(f"Baixando: {yt.title}")
    video.download(output_path='DownloadedVideos')
    print(f"{yt.title} baixado com sucesso.")
except Exception as e:
    print(f"Erro ao baixar {link}: {str(e)}")