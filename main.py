from pytubefix import YouTube

def download_video(url, save_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
        if stream:
            stream.download(output_path=save_path)
            print("✅ Video downloaded successfully")
        else:
            print("❌ No progressive mp4 stream found")
    except Exception as e:
        print("⚠️ Error:", e)


url = url = "https://youtu.be/knGCfzm4jWs?si=nP5brr-GKyyG1Ww4"

save_path = r"C:\Users\User\Desktop\New folder"

download_video(url, save_path)
