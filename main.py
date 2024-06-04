import google.generativeai as genai
import PIL, os, sys

from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key: sys.exit()

genai.configure(api_key=api_key)

geminiModel=genai.GenerativeModel("gemini-1.5-flash-latest") 

image = PIL.Image.open("resumes/resume5.png")
prompt = "extract only experiences from this resume, collect only organization, start date, end date and Job title in json"

response = geminiModel.generate_content([prompt.strip(), image])

print(response.text.replace("```json", "").replace("```", ""))