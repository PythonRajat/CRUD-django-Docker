pipeline {
    agent any

    
    stages {
        stage ('Build') {
            steps{
                sh 'echo building'
                sh 'cp .env.example .env'
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage ('test') {
            steps{
                sh 'echo testing'
                sh 'python3 manage.py test'
            }
        }
        stage ('Deploy') {
            steps{
                sh 'echo deploying'
            }
        }
    }
}