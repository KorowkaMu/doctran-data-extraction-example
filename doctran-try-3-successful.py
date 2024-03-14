import json
import os
from doctran import Doctran, ExtractProperty
import openai
from dotenv import load_dotenv
import PyPDF2

load_dotenv(".env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-3.5-turbo-16k-0613"
OPENAI_TOKEN_LIMIT = 16000

#Get the list of available openai models
#print(openai.Model.list())

text = """"""
pdf_file_path="path/to/file.pdf" #path to the file on the local drive

# Open the PDF file in read-binary mode
file= open(pdf_file_path, 'rb')
# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(file)

# Iterate through each page of the PDF
for page_num in range(len(pdf_reader.pages)):
    # Get a specific page's text and append it to the 'text' variable
    page = pdf_reader.pages[page_num]
    text += page.extract_text()
    # Get a specific page's text and append it to the 'text' variable

doctran = Doctran(openai_api_key=OPENAI_API_KEY, openai_model=OPENAI_MODEL, openai_token_limit=OPENAI_TOKEN_LIMIT)
document = doctran.parse(content=text)

#following types are supported as of nov 28, 2023 type: Literal["string", "number", "boolean", "array", "object"] source https://github.com/psychic-api/doctran/blob/main/doctran/doctran.py

properties = [
        ExtractProperty(
            name="Homeowner",
            description="This is First and Last name of the homeowner",
            type="string",
            required=True
        ),
        ExtractProperty(
            name="Limitation of liability",
            description="Condition of the contract that spells out maximum liability of the parties. If present the value of the property should be set to True, otherwise - False.",
            type="boolean",
            required=True
        ),
        ExtractProperty(
            name="Homeowner signature date",
            description="Date of signature by homeowner",
            type="string",
            required=True
        ),
        ExtractProperty(
            name="HOMEE signature date",
            description="Date of signature by HOMEE, Inc.",
            type="string",
            required=True
        ),

]
transformed_document = document.extract(properties=properties).execute()
print(json.dumps(transformed_document.extracted_properties, indent=2))

