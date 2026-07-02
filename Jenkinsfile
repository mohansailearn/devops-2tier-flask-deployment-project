pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/mohansailearn/devops-2tier-flask-deployment-project.git'
            }
        }

        stage('Build Flask Image') {
            steps {
                sh '''
                docker build -t flask-app -f docker/Dockerfile .
                '''
            }
        }

        stage('Create Docker Network') {
            steps {
                sh '''
                docker network create flask-network || true
                '''
            }
        }

        stage('Clean Old Containers') {
            steps {
                sh '''
                docker rm -f flask-container || true
                docker rm -f nginx-container || true
                '''
            }
        }

        stage('Deploy Flask Container') {
            steps {
                sh '''
                docker run -d \
                --name flask-container \
                --network flask-network \
                -p 5000:5000 \
                flask-app
                '''
            }
        }

        stage('Deploy Nginx Container') {
            steps {
                sh '''
                docker run -d \
                --name nginx-container \
                --network flask-network \
                -p 80:80 \
                -v $(pwd)/nginx/nginx.conf:/etc/nginx/conf.d/default.conf \
                nginx
                '''
            }
        }

        stage('Check Containers') {
            steps {
                sh '''
                echo "Checking containers..."
                docker ps -a
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                echo "Checking Nginx logs..."
                docker logs nginx-container

                echo "Testing application through Nginx..."
                curl -f localhost:80
                '''
            }
        }
    }

    post {

        success {
            echo 'Flask + Nginx deployment successful!'
        }

        failure {
            echo '''
             Deployment failed.
            Checking container logs...
            '''
            sh '''
            docker logs flask-container || true
            docker logs nginx-container || true
            '''
        }
    }
}
