import pytesseract,os,openai
from pdf2image import convert_from_path
from dotenv import load_dotenv

def get_extension(string):
    return string.split(".")[-1].lower()
def handle_file(file):
    text = ""
    if get_extension(file.name) == "pdf":
        temp_path = "/Users/teo/OpenAI_API/web_app/static/temp.pdf"
        with open(temp_path, "wb+") as temp:
            for chunk in file.chunks():
                temp.write(chunk)
        images = convert_from_path(temp_path)
        for image in images:
            text += pytesseract.image_to_string(image)
    elif get_extension(file.name) == "txt":
        for chunk in file.chunks():
            text = chunk.decode('utf-8')
    with open("/Users/teo/OpenAI_API/StoredInfo.txt","w",encoding='utf-8') as destination:
            destination.write(text)
    return text
def create_summary(text,question):
    load_dotenv()
    API_KEY = os.environ.get('OPEN_API_KEY')
    client = openai.OpenAI(api_key = API_KEY)
    response = client.responses.create(
        model = "gpt-4o-mini",
        instructions = "You are my assistant.I will give you some information and expect you to answer my questions based on it.I want you to respond in plain english. No need for code or special characters.Structure the answer as beautiful as you can. Here is the info:\n" + text,
        input = question
    )
    return response.output_text
