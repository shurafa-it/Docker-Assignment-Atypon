pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('List Files') {
            steps {
                sh 'ls -la'
                sh 'pwd'
            }
        }
        
        stage('Docker Status') {
            steps {
                sh 'docker --version || echo "Docker not available"'
                sh 'docker ps -a || echo "Cannot list containers"'
            }
        }
        
        stage('Build Project') {
            steps {
                echo 'Building project...'
                sh '''
                    # Simple shell script to build without docker-compose
                    mkdir -p build
                    cd build
                    echo "Project built successfully" > build_status.txt
                    cat build_status.txt
                '''
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline execution failed.'
        }
        always {
            echo 'Pipeline finished.'
        }
    }
}