node {
    checkout scm

    try {
        stage 'Run unit/integration tests'
        sh 'make -f Makfile.v2 test'
        
        stage 'Build application artefacts'
        sh 'make -f Makfile.v2 build'

        stage 'Create release environment and run acceptance tests'
        sh 'make -f Makfile.v2 release'

        stage 'Tag and publish release image'
        sh "make -f Makfile.v2 tag latest \$(git rev-parse --short HEAD) \$(git tag --points-at HEAD)"
        sh "make -f Makfile.v2 buildtag master \$(git tag --points-at HEAD)"

        withEnv(["DOCKER_USER=${DOCKER_USER}",
                 "DOCKER_PASSWORD=${DOCKER_PASSWORD}",
                 "DOCKER_EMAIL=${DOCKER_EMAIL}"]) {    
            sh "make -f Makfile.v2 login"
        }

        sh "make -f Makfile.v2 publish"
    }
    finally {
        stage 'Collect test reports'
        step([$class: 'JUnitResultArchiver', testResults: '**/reports/*.xml'])

        stage 'Clean up'
        sh 'make -f Makfile.v2 clean'
        sh 'make -f Makfile.v2 logout'
    }
}
