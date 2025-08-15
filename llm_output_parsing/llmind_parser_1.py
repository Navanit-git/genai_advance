import json
with open("../keys.json") as f:
    api_key = json.load(f)


groq_key_1 =api_key["grok_api_key_1"]
groq_key_2 =api_key["grok_api_key_2"]
groq_key_3 =api_key["grok_api_key_3"]


from llama_index.llms.groq import Groq
llm = Groq(model="moonshotai/kimi-k2-instruct", api_key=groq_key_1)


from llama_index.core.callbacks import LlamaDebugHandler, CallbackManager
from llama_index.core import Settings

# Initialize the debug handler
debug_handler = LlamaDebugHandler(print_trace_on_end=True)

# Set the callback manager
Settings.callback_manager = CallbackManager([debug_handler])

import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

from datetime import datetime
from pydantic import BaseModel, Field

class LineItem(BaseModel):
    """A line item in an invoice."""

    Description: str = Field(description="The description of this item")
    price: float = Field(description="Total amount payable with IGST for this item")

class Invoice(BaseModel):
    """A representation of information from an invoice."""

    invoice_id: str = Field(description="A unique identifier for this invoice, majorly the invoice number")
    date: str = Field(description="The date this invoice was created")
    line_items: list[LineItem] = Field(description="A list of all the items in this invoice")

from llama_index.readers.file import PDFReader
from pathlib import Path
pdf_reader = PDFReader()
documents = pdf_reader.load_data(file=Path("uber_reciept.pdf"))
text = documents[0].text

sllm = llm.as_structured_llm(Invoice)
response = sllm.complete(text)
print(response)

json_response = json.loads(response.text)
print(json.dumps(json_response, indent=2))

# {"invoice_id":"HCJFJIJI25156289","date":"12 Aug 2025","line_items":[{"Description":"Transportation service fare","price":165.0}]}
# {
#   "invoice_id": "HCJFJIJI25156289",
#   "date": "12 Aug 2025",
#   "line_items": [
#     {
#       "Description": "Transportation service fare",
#       "price": 165.0
#     }
#   ]
# }
# Request options: {'method': 'post', 'url': '/chat/completions', 'files': None, 'idempotency_key': 'stainless-python-retry-7962f7ba-898b-434c-a94c-5a8dcc9cc77c', 'json_data': {'messages': [{'role': 'user', 'content': 'Tax Invoice\nNAVANIT DUBEY\nPick up address: 3A, Sector 33, Gurugram,\nHaryana 122101, India\nIndia\n \nInvoice issued by Uber India Systems Private\nLimited on behalf of:\nP K TRAVELS\nRailway Line Apartment Park, FLAT NO. 801,\nRailway Line Staff CGHS, DWARKA, Sector\n19B Dwarka, 110075, New Delhi, Delhi, IN-DL\nIndia\nGSTIN: 07AHEPK5797K2ZP\nInvoice number:  \nHCJFJIJI25156289\nInvoice date:  \n12 Aug 2025\nPlace of supply (Name of state):  \nHaryana\nHSN Code:  \n996412\nCategory of services:  \nPassenger Transport Services\nTax is payable on reverse charge basis:  \nNo\n \n \nTax Point Date \nDescription \nQty \nTax \nTax\nAmount \nNet\namount \n12 Aug 2025 \nTransportation service fare \n1 \nIGST 5%\n₹\n7.86\n₹\n157.14 \n \nTotal net amount \n₹\n157.14 \n \nTotal IGST 5%\n₹\n7.86 \n \nTotal amount payable \n₹\n165.00 \nDetails of ECO under GST:\nUber India Systems Private Limited / \nPrivate Office No: 205 and 207 (A,B,C) DBS Business Center, New Delhi, 1st\nFloor, World Trade Tower, Barakhamba Lane, Connaught Place, New Delhi - 110001 / \nGST: 07AABCU6223H1ZG'}], 'model': 'moonshotai/kimi-k2-instruct', 'stream': False, 'temperature': 0.1, 'tool_choice': 'required', 'tools': [{'type': 'function', 'function': {'name': 'Invoice', 'description': 'A representation of information from an invoice.', 'parameters': {'$defs': {'LineItem': {'description': 'A line item in an invoice.', 'properties': {'Description': {'description': 'The description of this item', 'title': 'Description', 'type': 'string'}, 'price': {'description': 'The total amount payable for this item', 'title': 'Price', 'type': 'number'}}, 'required': ['Description', 'price'], 'title': 'LineItem', 'type': 'object'}}, 'properties': {'invoice_id': {'description': 'A unique identifier for this invoice, majorly the invoice number', 'title': 'Invoice Id', 'type': 'string'}, 'date': {'description': 'The date this invoice was created', 'title': 'Date', 'type': 'string'}, 'line_items': {'description': 'A list of all the items in this invoice', 'items': {'$ref': '#/$defs/LineItem'}, 'title': 'Line Items', 'type': 'array'}}, 'required': ['invoice_id', 'date', 'line_items'], 'type': 'object', 'additionalProperties': False}, 'strict': False}}]}}