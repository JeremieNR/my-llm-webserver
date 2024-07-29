from flask import request, Flask
import ollama

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def run():
    if request.method == 'POST':
        response = ollama.chat(model='gemma:2b', messages=[
            {
                'role': 'user',
                'content': str(request.data),
            },
        ])
        return response['message']['content']

if __name__ == '__main__':  
   app.run()
