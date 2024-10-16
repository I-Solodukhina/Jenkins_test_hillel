pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Cloning the repository...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Setting up Python environment and installing dependencies...'
                bat '''
                    C:\\Users\\solod\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m venv venv
                    venv\\Scripts\\activate
                    venv\\Scripts\\pip install -r requirements.txt
                    venv\\Scripts\\playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                bat '''
                    venv\\Scripts\\activate
                    venv\\Scripts\\pytest --junitxml=results.xml -v
                    dir
                '''
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }
    }

    post {
        success {
            emailext(
                subject: "Jenkins Pipeline Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "The Jenkins pipeline for ${env.JOB_NAME} has completed successfully.",
                to: 'solodushka@gmail.com'
            )
        }
        failure {
            emailext(
                subject: "Jenkins Pipeline Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "The Jenkins pipeline for ${env.JOB_NAME} has failed. Please check the Jenkins logs for more details.",
                to: 'solodushka@gmail.com'
            )
        }
    }
}
