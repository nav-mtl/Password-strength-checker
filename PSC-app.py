from flask import Flask, request, render_template
import re

app = Flask(__name__)

# Function to check the strength of the password
def check_password_strength(password):
    # Initialize strength criteria
    strength = {"length": False, "digit": False, "upper": False, "lower": False, "special": False}
    
    # Check if password meets criteria
    if len(password) >= 8:
        strength["length"] = True
    if re.search(r"\d", password):
        strength["digit"] = True
    if re.search(r"[A-Z]", password):
        strength["upper"] = True
    if re.search(r"[a-z]", password):
        strength["lower"] = True
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength["special"] = True
    
    return strength

# Function to estimate the time for a quantum computer to decrypt the password
def estimate_quantum_decryption_time(password):
    # This is a very rough estimate and highly depends on various factors.
    # For simplicity, we assume a quantum computer can test 1 trillion passwords per second.
    attempts = 2 ** len(password)  # Assuming each character can be one of two possibilities (binary search)
    quantum_speed = 1e12  # 1 trillion attempts per second
    
    # Calculate the time in seconds
    time_seconds = attempts / quantum_speed
    
    # Convert the time to a human-readable format
    if time_seconds < 60:
        return f"{time_seconds:.2f} seconds"
    elif time_seconds < 3600:
        return f"{time_seconds / 60:.2f} minutes"
    elif time_seconds < 86400:
        return f"{time_seconds / 3600:.2f} hours"
    else:
        return f"{time_seconds / 86400:.2f} days"

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = {}
    password = ''
    password_length = 0
    quantum_time = ''
    if request.method == 'POST':
        password = request.form['password']
        password_length = len(password)
        strength = check_password_strength(password)
        quantum_time = estimate_quantum_decryption_time(password)
    return render_template('index.html', strength=strength, password=password, password_length=password_length, quantum_time=quantum_time)

if __name__ == '__main__':
    app.run(debug=True)
