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
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    playwright install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                    . venv/bin/activate
                    pytest --junitxml=pytest-report.xml
                '''
            }
        }
    }

    post {
        always {
            junit 'pytest-report.xml'
        }
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
