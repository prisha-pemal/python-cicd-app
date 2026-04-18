pipeline {
    agent any

    environment {
        IMAGE_NAME = "python-cicd-app"
        CONTAINER_NAME = "python-app-container"
    }

    stages {

        stage('1. Clone Code') {
            steps {
                // Pull code from Git
                git branch: 'main', url: '<your-repo-url>'
            }
        }

        stage('2. Install Dependencies') {
            steps {
                // Install Python dependencies
                sh 'pip install -r requirements.txt'
            }
        }

        stage('3. Run Tests') {
            steps {
                // Run pytest
                sh 'pytest'
            }
        }

        stage('4. Build Docker Image') {
            steps {
                // Build Docker image
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('5. Stop Old Container') {
            steps {
                // Stop and remove old container if exists
                sh '''
                docker rm -f $CONTAINER_NAME || true
                '''
            }
        }

        stage('6. Run New Container') {
            steps {
                // Run container
                sh '''
                docker run -d -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME
                '''
            }
        }

        stage('7. Verify Deployment') {
            steps {
                // Check if app is running
                sh 'curl http://localhost:5000'
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