
pipeline {
    agent any

    environment {
        DOCKERHUB_USER = 'geethask'
        IMAGE_NAME = 'geethask/employee-management'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:v1 .'
            }
        }

        stage('Login and Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'docker-token',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    bat 'docker login -u %DOCKER_USER% -p %DOCKER_PASSWORD%'
                    bat 'docker push %IMAGE_NAME%:v1'
                    bat 'docker logout'
                }
            }
        }

        stage('Health Check') {
            steps {
                bat 'docker image inspect %IMAGE_NAME%:v1'
            }
        }
    }

    post {
        always {
            echo 'Employee Management pipeline finished.'
        }
    }
}
