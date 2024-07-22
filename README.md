# Password Strength Checker

This is a simple web application that checks the strength of a password based on various criteria such as length, use of digits, uppercase letters, lowercase letters, and special characters. It also estimates the time it would take for a quantum computer to decrypt the given password.

## Features

<ul>
    <li>Checks if the password is at least 8 characters long.</li>
    <li>Checks if the password contains at least one digit.</li>
    <li>Checks if the password contains at least one uppercase letter.</li>
    <li>Checks if the password contains at least one lowercase letter.</li>
    <li>Checks if the password contains at least one special character.</li>
    <li>Estimates the time for a quantum computer to decrypt the password.</li>
</ul>

## Installation

<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/yourusername/password_strength_checker.git
cd password_strength_checker
        </code></pre>
    </li>
    <li>Install the required packages:
        <pre><code>pip install flask
        </code></pre>
    </li>
    <li>Run the application:
        <pre><code>python PSC-app.py
        </code></pre>
    </li>
    <li>Open your browser and navigate to <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a>.</li>
</ol>

## Usage

<p>Enter a password in the input field and click "Check Strength". The password strength criteria will be displayed. The estimated time for a quantum computer to decrypt the password will be shown. Click the "Copy" button to copy the password to the clipboard.</p>

## Quantum Decryption Time Estimation

<h3>Calculation Method:</h3>
<ol>
    <li><strong>Quantum Speed Assumption</strong>: We assume a quantum computer can test 1 trillion passwords per second (1e12 passwords/second). This is a simplified model and real-world speeds could vary based on numerous factors.</li>
    <li><strong>Password Search Space</strong>: The search space for a password is considered to be \(2^{\text{length of the password}}\). This binary search model assumes each character can be one of two possibilities, which simplifies the calculation but does not accurately represent all character sets.</li>
    <li><strong>Attempts Calculation</strong>: The number of attempts required to crack the password is calculated as \(2^{\text{length of the password}}\).
        <pre><code>For example, for a password of length 8, this would be \(2^8 = 256\) attempts.
        </code></pre>
    </li>
    <li><strong>Time Calculation</strong>: The time it would take for a quantum computer to crack the password is then calculated by dividing the total number of attempts by the quantum speed.
        <pre><code>For a password length of 8, it would be \(256 / 1e12 = 2.56 \times 10^{-10}\) seconds.
        </code></pre>
    </li>
</ol>

<h3>Example Calculation:</h3>
<pre><code>For a password of length 8:
- Attempts: \(2^8 = 256\)
- Quantum Speed: 1 trillion attempts/second = 1e12
- Time (seconds): 256 / 1e12 = 2.56 \times 10^{-10} seconds
</code></pre>

<h3>Limitations:</h3>
<p>This calculation is highly simplified and does not account for many real-world factors such as the actual implementation of quantum algorithms, the complexity of the password (character set), and practical limitations of quantum computing. The assumption that each character has only two possibilities is not realistic. A more accurate model would consider the actual character set (e.g., alphanumeric, special characters).</p>

## Author

<p>Navjot Singh</p>
<p><a href="https://www.linkedin.com/in/njot/">LinkedIn</a></p>

## License

<p>This project is licensed under the MIT License.</p>
