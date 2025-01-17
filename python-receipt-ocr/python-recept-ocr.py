import requests

print("=== Python Receipt OCR Demo - Need help? Email support@asprise.com ===")

receiptOcrEndpoint = 'https://ocr.asprise.com/api/v1/receipt' # Receipt OCR API endpoint
imageFile = "receipt.jpg" # // Modify this to use your own file if necessary
r = requests.post(receiptOcrEndpoint, data = { \
  'client_id': 'TEST',        # Use 'TEST' for testing purpose \
  'recognizer': 'auto',       # can be 'US', 'CA', 'JP', 'SG' or 'auto' \
  'ref_no': 'ocr_python_123', # optional caller provided ref code \
  }, \
  files = {"file": open(imageFile, "rb")})

print(r.text) # result in JSON

response_data = r.json()
items = response_data["receipts"][0]["items"]
for i in range(len(items)):
    print(items[i]["description"])