pipeline {
   agent any

   stages {
      stage('Run Code Stage') {
         steps {
            echo 'This step will run your code'
	    sh 'python3 code.py'
         }
      }
      stage('Test Code Stage') {                                                                                                steps {
        	echo 'This step will test your code'
		sh 'python3 test_code.py'
 	}
      }
   }

}
