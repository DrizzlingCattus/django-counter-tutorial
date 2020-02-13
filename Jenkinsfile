pipeline {
  agent any
  stages {
    stage('stage1') {
      steps {
	echo 'starting jenkins!!!'
	sh 'cat Dockerfile'
	sh 'ls -al'
      }
    }
    stage('clean-up') {
      steps {
	echo 'clean up previous docker container'
	script {
	  try {
	    sh 'docker container stop counter'
	  } catch(err) {
	    unstable(err)
	  }
	}
      }
    }
    stage('build dockerfile') {
      steps {
	echo 'starting building dockerfile'
	sh 'echo $(whoami)'
	sh 'echo $(groups)'
	sh 'ls -al'
	sh 'docker build -t test1 .'
      }
    }
    stage('start project') {
      steps {
	echo 'starting project'
	sh 'docker run --name "counter" --rm -it -d -p 9000:8000 test1'
      }
    }
  }
}
