# 🚀 Simple Flask Web App with Docker and GitHub Actions

This is a simple Flask web application that demonstrates the basics of building, containerizing, and automating the deployment of a Python web app using Docker and GitHub Actions.

## 🧩 Features

- A basic Flask route that returns "Hello DevOps!"
- Containerized using Docker
- Version-controlled with Git and hosted on GitHub
- Automated CI/CD pipeline using GitHub Actions (builds and pushes Docker image to Docker Hub)

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/omiete01/webapp.git
cd webapp
```

### 2. Run the Application Locally

If you want to run the app without Docker:

```bash
pip install -r requirements.txt
python webapp.py
```

Visit `http://127.0.0.1:5000` in your browser.

### 3. Run with Docker

Build and run the Docker container:

```bash
docker build -t webapp:1.0 .
docker run -p 5000:5000 webapp:1.0
```

Visit `http://127.0.0.1:5000` in your browser.

## 📦 Technologies Used

- **Python** – Programming language
- **Flask** – Web framework
- **Docker** – Containerization
- **GitHub** – Version control
- **GitHub Actions** – CI/CD automation

## 🧪 What’s Included

| Task | Description |
|------|-------------|
| ✅ Create a Simple Flask App | A basic Flask route that returns "Hello DevOps!!!" |
| ✅ Containerize the App | Dockerfile and .dockerignore for packaging the app |
| ✅ Set Up Version Control | GitHub repo, .gitignore, and code pushed to GitHub |
| ✅ CI/CD with GitHub Actions | Workflow to build and push Docker image to Docker Hub |

## 📦 How It Works

1. The Flask app runs on port 5000.
2. The Dockerfile defines how to build the app into a container.
3. The `.dockerignore` file ensures unnecessary files are not included in the Docker image.
4. The GitHub Actions workflow automatically builds the Docker image and pushes it to Docker Hub when changes are pushed to the `master` branch.

## 📦 To Use with Docker Hub

To use this project with Docker Hub:

1. Ensure you have a dockerhub account and generate a token.
2. Go to the Settings tab on your Github repository and update the token in the Actions under Secrets and Variables
3. Make sure to name the username as `secrets.DOCKERHUB_NAME` and password as `secrets.DOCKERHUB_TOKEN`

## 📝 Author

Esther Fyneface 
https://github.com/omiete01
estheromiete01@gmail.com

## 📄 License

MIT License