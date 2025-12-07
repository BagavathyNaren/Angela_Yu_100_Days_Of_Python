# Day 91 Professional Portfolio Project: PDF to Audiobook



## Overview

- Topics: Python, Flask

### The challenge

- Build a python script that takes a PDF file, identifies the text and converts the text to speech, like a free audiobook.
 
### Links


## Reflection
**Approach, Challenges, Future Improvements:** 

Some aspects I would improve would be to enhance the user experience (UX) by adding a spinner while the PDF is converting to audio to let the user know it's processing. Additionally, I would improve the file handling experience by allowing users to name the file instead of having a hardcoded filename.

**Biggest learning:**

My biggest learning today was about using state in Flask and gaining a deeper understanding of the os module, including functions such as:

```
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
```
It was also a bit of a challenge to get the audio in the HTML to work, so needed to use a bit of ChatGPT to get over the parts where I got stuck. Also, had to look up PyPDF2 and gTTS to work with the pdf and audio conversion.
If I were to tackle this project again, I would primarily focus on improving the UX/UI to make it more straightforward and user-friendly.


## References

https://stackoverflow.com/questions/43961999/play-html5-sound-files-with-flask

PyPDF2

pip install PyPDF2

gTTS

pip install gTTS
