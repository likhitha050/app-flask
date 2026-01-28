pipeline{
  agent any
  environment{
    DOCKERHUB_CRED = credentials('dockerID')
    IMAGE_NAME = "cslikhitha/app-flask"
  }
  triggers{
    cron('* * * * *')
  }
  stages{
    stage('checkout'){
      steps{
        git(
          url:"https://github.com/likhitha050/app-flask.git",
          branch: 'main'
        )
      }
    }
      stage('Build docker Image'){
        steps{
          script{
            dockerImage = docker.build("${IMAGE_NAME}:latest")
          }
      }
    }
    stage('Push docker image'){
      steps{
        script{
          docker.withRegistry("https://index.docker.io/v1/",'dockerID'){
            dockerImage.push()
          }
        }
      }
    }
  }
  post{
    success{
      echo "Build Success..."
    }
    failure{
      echo "Build Failure....."
    }
    always{
      echo "Cleanning...."
      deleteDir()
    }
  }
}
