from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# 1
@app.route('/')
def home():
   return render_template('index.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)