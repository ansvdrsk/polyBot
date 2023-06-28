pipeline {
    agent any

    environment {
        IMAGE_TAG = "${env.BUILD_NUMBER}-${env.BUILD_ID}"
    }

    stages {
        stage('Build') {
            steps {
                // Use the official Python base image for building the Docker image
                sh "docker build -t your-docker-image:${env.IMAGE_TAG} ."
            }
        }

        stage('Test') {
            steps {
                // Run your tests here
                // For example: unit tests, integration tests, etc.
                // Replace this with your actual test commands

                // Example command:
                sh "python -m unittest tests/*.py"
            }
        }

        stage('Deploy') {
            steps {
                // Push Docker image to the registry
                sh "docker push your-registry/your-docker-image:${env.IMAGE_TAG}"

                // Deploy your application
                // Add deployment steps specific to your environment
            }
        }
    }

    post {
        always {
            // Clean up the built Docker images from the disk
            sh "docker rmi your-docker-image:${env.IMAGE_TAG}"
        }
    }
}
