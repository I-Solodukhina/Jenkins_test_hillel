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
                // Створення віртуального середовища та встановлення залежностей
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                // Запуск тестів
                sh '''
                    source venv/bin/activate
                    pytest --junitxml=results.xml
                '''
            }
            post {
                always {
                    // Архівування результатів тестів у форматі JUnit
                    junit 'results.xml'
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                echo 'Publishing test results to Jenkins...'
                // Відображення результатів у веб-інтерфейсі Jenkins
            }
        }
    }

    post {
        success {
            // Надсилання повідомлення при успішному виконанні пайплайну
            emailext(
                subject: "Jenkins Pipeline Success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "The Jenkins pipeline for ${env.JOB_NAME} has completed successfully.",
                to: 'InsertYour@Mail.Here'
            )
        }
        failure {
            // Надсилання повідомлення при невдалому виконанні пайплайну
            emailext(
                subject: "Jenkins Pipeline Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: "The Jenkins pipeline for ${env.JOB_NAME} has failed. Please check the Jenkins logs for more details.",
                to: 'InsertYour@Mail.Here'
            )
        }
    }
}
