<<<<<<< HEAD
# Simple Python App
print("Hello from CI/CD Pipeline 🚀")
=======
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD Pipeline Working!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
>>>>>>> b1d884b93d585a3504d12a7be5e2271faee90562
