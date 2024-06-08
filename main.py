import google.generativeai as genai
import PIL, os, sys, json

from dotenv import load_dotenv
load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key: sys.exit()

genai.configure(api_key=api_key)

geminiModel=genai.GenerativeModel("gemini-1.5-flash-latest") 

image = PIL.Image.open("resumes/resume3.png")
prompt = "extract only experiences from this resume, collect only organization, start date, end date and Job title in json"

response = geminiModel.generate_content([prompt.strip(), image])

rstring = response.text.replace("```json", "").replace("```", "")

jsondata = json.loads(rstring)

final = [tuple(x.values()) for x in jsondata]

print(final)