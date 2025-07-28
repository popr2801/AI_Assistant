import openai, os,pytesseract
from openai import OpenAI
from pdf2image import convert_from_path
from dotenv import load_dotenv

load_dotenv()

file_path = 'lab4.pdf'

images = convert_from_path(file_path)
text = ""
for image in images:
    text += pytesseract.image_to_string(image)

API_KEY = os.environ.get('OPENAI_API_KEY')

client = OpenAI(api_key = API_KEY)

response = client.responses.create(
    model = "gpt-4o-mini",
    instructions="Please read the following text carefully and prepare to answer quiestions based on that info. Here is the text:\n" + text,
    input =  "Can you tell me what the file is about?",
)


print(response.output_text)