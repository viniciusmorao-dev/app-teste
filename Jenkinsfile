pipeline {
  agent any
  stages {
    stage ('SCM') {
      steps {
        echo "Clonando repositório..."
        git 'https://github.com/viniciusmorao-dev/app-teste.git'
      }
    }

    stage ('Build') {
      steps {
        echo "Building..."
        sh 'uvicorn main:app --reload'
      }
    }
  }
}
