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
                body: """
                    The Jenkins pipeline for ${env.JOB_NAME} completed successfully.

                    Test Summary:
                    Total Tests: ${currentBuild.getTestResultAction().getTotalCount()}
                    Passed: ${currentBuild.getTestResultAction().getTotalCount() - currentBuild.getTestResultAction().getFailCount()}
                    Failed: ${currentBuild.getTestResultAction().getFailCount()}
                    Skipped: ${currentBuild.getTestResultAction().getSkipCount()}

                    See the full test report here: ${env.BUILD_URL}testReport
                """,
                to: 'InsertYour@Mail.Here',
                attachLog: true,
                attachmentsPattern: "pytest-report.xml"
            )
        }
        failure {
            emailext(
                subject: "Jenkins Pipeline Failed: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                body: """
                    The Jenkins pipeline for ${env.JOB_NAME} has failed.

                    Test Summary:
                    Total Tests: ${currentBuild.getTestResultAction().getTotalCount()}
                    Passed: ${currentBuild.getTestResultAction().getTotalCount() - currentBuild.getTestResultAction().getFailCount()}
                    Failed: ${currentBuild.getTestResultAction().getFailCount()}
                    Skipped: ${currentBuild.getTestResultAction().getSkipCount()}

                    See the full test report here: ${env.BUILD_URL}testReport
                """,
                to: 'InsertYour@Mail.Here',
                attachLog: true,
                attachmentsPattern: "pytest-report.xml"
            )
        }
    }
}
