from flask import Flask, render_template, request
import json
import spacy

app = Flask(__name__)

# Load intents from JSON file
with open('intents.json') as file:
    intents = json.load(file)

# Load NLP model
nlp = spacy.load('en_core_web_sm')

# Define route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Define route for processing user input
@app.route('/process', methods=['POST'])
def process():
    message = request.form['message']
    response = chatbot_response(message)
    return render_template('index.html', message=message, response=response)

# Define function for generating chatbot response
def chatbot_response(message):
    # Process user input with NLP model
    doc = nlp(message)
    # Determine intent and entities from user input
    intent = None
    entities = {}
    for token in doc:
        if token.text in intents['intents']:
            intent = intents['intents'][token.text]['intent']
            for ent in intents['intents'][token.text]['entities']:
                entities[ent] = None
        elif token.ent_type_ in intents['entities']:
            entities[intents['entities'][token.ent_type_]] = token.text
    # Generate chatbot response based on intent and entities
    if intent:
        if intent in intents['responses']:
            response = intents['responses'][intent]
        else:
            response = "I'm sorry, I don't understand what you're asking."
    else:
        response = "I'm sorry, I don't understand what you're asking."
    return response

if __name__ == '__main__':
    app.run(debug=True)
