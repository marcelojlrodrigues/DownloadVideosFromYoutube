import pandas as pd

from pytube import YouTube

SpreadsheatWay = "LinksYoutube.xlsx"
sheetName = "ApiRest"

planilha = pd.read_excel(SpreadsheatWay, sheet_name=sheetName)

print(planilha['links'])

links_youtube = planilha['links']

for link in links_youtube:
    try:
        yt = YouTube(link)
        video = yt.streams.get_highest_resolution()  # Altere a qualidade se necessário
        print(f"Baixando: {yt.title}")
        video.download(output_path='DownloadedVideos/Curso Ifood Tech (Ada Tech)/07. API REST')
        print(f"{yt.title} baixado com sucesso.")
    except Exception as e:
        print(f"Erro ao baixar {link}: {str(e)}")

