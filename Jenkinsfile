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
                    appImage = docker.build("vsrekul/my-app:${params.VERSION}")
                }
            }
        }

        stage('Tag') {
            steps {
                script {
                   sh "echo tagging"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'dockerhub-credentials', url: 'https://index.docker.io/v1/') {
                        appImage.push()
                    }
                }
            }
        }
    }
}
