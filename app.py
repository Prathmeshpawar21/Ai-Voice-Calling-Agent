import assemblyai as asi
# `pip install assemblyai` (Windows)

import assemblyai as aai

aai.settings.api_key = "04798c6e7a304a249b3ebb9f66461bcc"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://assembly.ai/news.mp4")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")





print(transcript.text) 


# Prathmeshpawar21
# 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