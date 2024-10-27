pipeline{
    agent any
    parameters{
        text(name: 'VERSION', defaultValue: '0.0.1', description: 'provide the app version')
    }
    environment{
        appImage = ''
    }
    stages{
        stage('checkout scm'){
            git branch: 'main', url: 'https://github.com/vsrekul/practice-calci.git'
        }
    }
    stages{
        stage('build'){
            appImage = docker.build('my-app:latest')
        }
    }
    stages{
        stage('tag'){
            appImage.tag("vsrekul/my-app:${params.VERSION}")
        }
    }
    stages{
        stage('tag'){
            withDockerRegistry(credentialsId: 'dockerhub-credentials', url: 'https://index.docker.io/v1/') {
                appImage.push("vsrekul/my-app:${params.VERSION}")
            }            
        }
    }
}