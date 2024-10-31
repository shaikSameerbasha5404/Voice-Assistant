from flask import Flask, render_template, jsonify
import main  # Make sure 'main.py' is in the same directory as this script
import threading

app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/start_voice_assistant', methods=['GET'])
def start_voice_assistant():
    # Start the voice assistant in a separate thread
    threading.Thread(target=main.start_voice_assistant).start()
    return jsonify({"message": "Voice Assistant started!"}), 200

if __name__ == '__main__':
    app.run(debug=True)
