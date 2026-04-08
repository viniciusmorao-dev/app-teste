pipeline {
  agent any

  environment {
    IMAGE_NAME = 'api-teste'
  }
  
  stages {
    stage ('SCM') {
      steps {
        sh 'rm -rf app-teste'
        
        echo "Clonando repositório..."
        sh 'git clone https://github.com/viniciusmorao-dev/app-teste.git'
      }
    }

    stage ('Build Image') {
      steps {
        sh 'docker build -t $IMAGE_NAME .'
      }
    }

    stage ('Deploy Container') {
      steps {
        sh '''
        docker run -d -p 8080:8080 --name api-teste-container $IMAGE_NAME
        '''
      }
    }
    
  }
}
