import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

def run(text_input):
    genai.configure(api_key="AIzaSyBhs9H_3HSIGmS0bmayLIFe4pd-fNS_m10")

    # Create the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-002",
    generation_config=generation_config,
    )

    chat_session = model.start_chat(
    history=[
    ]
    )

    response = chat_session.send_message(text_input)


    return str(response.text)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')




@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message')
    print(f"Received input: {user_input}")  # Debugging line
    try:
        response_text = run(user_input)
        print(f"Generated response: {response_text}")  # Debugging line
        return jsonify({"response": response_text})
    except Exception as e:
        print(f"Error occurred: {e}")  # Debugging line
        return jsonify({"response": f"Error: {str(e)}"}), 500



if __name__ == "__main__":
    app.run(debug=True)