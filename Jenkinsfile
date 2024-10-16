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
                    python3 -m .venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                    source venv/bin/activate
                    pytest --junitxml=results.xml
                '''
            }
            post {
                always {
                    junit 'results.xml'
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                echo 'Publishing test results to Jenkins...'
            }
        }
    }

    post {
        success {
            emailext(
                subject: "Jenkins Pipeline Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "The Jenkins pipeline for ${env.JOB_NAME} has completed successfully.",
                to: 'InsertYour@Mail.Here'
            )
        }
        failure {
            emailext(
                subject: "Jenkins Pipeline Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "The Jenkins pipeline for ${env.JOB_NAME} has failed. Please check the Jenkins logs for more details.",
                to: 'InsertYour@Mail.Here'
            )
        }
    }
}
