pipeline {
  agent any
  stages {
    stage ('SCM') {
      steps {
        echo "Clonando repositório..."
        sh 'git clone https://github.com/viniciusmorao-dev/app-teste.git'
      }
    }

    stage ('Build') {
      steps {
        sh 'pip install fastapi uvicorn'

        echo "Building..."
        sh 'uvicorn main:app --reload'
      }
    }
  }
}
