pipeline {
    agent any

    environment {
        IMAGE_NAME = "python-cicd-app"
        CONTAINER_NAME = "python-app-container"
    }

    stages {

        stage('Install Dependencies') {
            steps {
                // Windows command
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker rm -f %CONTAINER_NAME% || exit 0'
            }
        }

        stage('Run New Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name %CONTAINER_NAME% %IMAGE_NAME%'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'curl http://localhost:5000'
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline executed successfully!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}