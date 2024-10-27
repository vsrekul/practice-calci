pipeline {
    agent any

    parameters {
        string(name: 'VERSION', defaultValue: '0.0.1', description: 'provide the app version')
    }

    environment {
        appImage = ''
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/vsrekul/practice-calci.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    appImage = docker.build('my-app:latest')
                }
            }
        }

        stage('Tag') {
            steps {
                script {
                    appImage.tag("vsrekul/my-app:${params.VERSION}")
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'dockerhub-credentials', url: 'https://github.com/vsrekul/practice-calci.git') {
                        appImage.push()
                    }
                }
            }
        }
    }
}
