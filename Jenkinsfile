pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'github-credentials', passwordVariable: 'Sheva1997@', usernameVariable: 'ansvdrsk')]) {

                    // Build Docker image
                    sh 'docker build -t bot-app .'


                }
            }
        }



        stage('Deploy') {
            steps {
                // Push Docker image to the registry
                sh 'docker push your-registry/your-docker-image:latest'

                // Deploy your application
                // Add deployment steps specific to your environment
            }
        }
    }
}
