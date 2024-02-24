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
                sh 'ssh deploy@192.168.0.105 -o StrictHostKeyChecking=no "bash /var/www/CRUD-django-Docker/script/deploy.sh"'
            }
        }
    }
}
