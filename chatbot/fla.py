from flask import Flask, render_template, request
import nltk
from nltk.chat.util import Chat, reflections

app1 = Flask(__name__)

pairs = [
    ['hi|hello|hey|sup|whats up?', ['Hello!', 'Hi there!', 'Hey!']],
    ['what is your name?|who are you?|introduce', ['My name is Mr. BrainMan.']],
    ['how are you ?', ['I am doing well, thank you.', 'I am fine, thanks for asking.']],
    ['what can you do?', ['I can answer questions and have simple conversations.']],
    ['bye|goodbye', ['Goodbye!', 'Have a nice day!', 'See you later.']],
    ['what is the weather like?', ['I am sorry, I am not able to provide weather information.']],
    ['what time is it?', ['I am sorry, I do not have access to the current time.']],
    ['what is the meaning of life?', ['That is a philosophical question that has been debated for centuries.']],
    ['tell me a joke', ['Why did the tomato turn red? Because it saw the salad dressing!']],
    ['what is your favorite color?', ['I do not have a favorite color, as I am an artificial intelligence and do not have personal preferences.']],
    ['can you help me?', ['Of course! What do you need help with?']],
    ['how do I reset my password?', ['You can reset your password by clicking on the "Forgot Password" link on the login page.']],
    ['what is the capital of France?', ['The capital of France is Paris.']],
    ['how do I contact customer support?', ['You can contact customer support by phone, email, or through the contact form on our website.']],
    ['what is your favorite book?', ['As an AI chatbot, I do not have the ability to read books or have personal preferences.']],
    ['can you recommend a restaurant?', ['Sure! What type of cuisine are you in the mood for?']],
    ['what is your favorite food?', ['I do not have a favorite food, as I am an artificial intelligence and do not have personal preferences.']],
    ['how do I place an order?', ['You can place an order by selecting the item you want to purchase and following the checkout process.']],
    ['what is your favorite movie?', ['As an AI chatbot, I do not have the ability to watch movies or have personal preferences.']],
]

chatbot = Chat(pairs, reflections)

@app1.route('/')
def home():
    return render_template('chatsup.html')

@app1.route('/get')
def get_bot_response():
    user_input = request.args.get('msg')
    
    response = chatbot.respond(user_input)
    print(user_input)
    return str(response)

if __name__ == '__main__':
    app1.run(port=5001,debug=True)
