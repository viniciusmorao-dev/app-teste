pipeline {
  agent any
  stages {
    stage ('SCM') {
      steps {
        echo "Clonando repositório..."
        git clone "https://github.com/viniciusmorao-dev/app-teste.git"
      }
    }

    stage ('Build') {
      steps {
        echo "Building..."
        uvicorn main:app --reload
      }
    }
  }
}
