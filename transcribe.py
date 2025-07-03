import speech_recognition as sr
from datetime import datetime

r = sr.Recognizer()

# Create or open the transcript file
with open("transcript.txt", "a", encoding="utf-8") as file:
    with sr.Microphone() as source:
        print("🎤 Say something (Ctrl+C to stop)...")
        while True:
            try:
                audio = r.listen(source)
                text = r.recognize_google(audio)
                timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
                line = f"{timestamp} {text}"
                print("📝 Transcribed:", line)

                # Save to file
                file.write(line + "\n")
                file.flush()  # Save immediately without waiting

            except sr.UnknownValueError:
                print("⚠️ Could not understand audio")
            except KeyboardInterrupt:
                print("\n🔚 Exiting and saving transcript...")
                break

