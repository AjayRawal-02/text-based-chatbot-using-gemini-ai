import google.generativeai as genai
API_KEY="AIzaSyDg2146fgeoq0jO8AIMFbROAzzjqdTA22Q"
genai.configure(api_key=API_KEY)

model= genai.GenerativeModel("gemini-2.0-flash")
chat=model.start_chat()
print("chat with gemini:type exit to quit")
while True:
    user_input=input("you:")
    if user_input.lower()=="exit":
        break
    response=chat.send_message(user_input)
    print("gemini:",response.text)
