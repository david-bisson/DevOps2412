#!groovy
import org.jenkinsci.plugins.workflow.steps.FlowInterruptedException
import com.nice.pipeline. *
import groovy.transform.Field
import hudson.tasks.test.AbstractTestResultAction


@Field


final
PIPELINE_TEMPLATE_NAME = 'generic-playwright-sm'


@Field


final
PIPELINE_STASH_NAME


@Field


String
nodeLabe


@Field def parameters
    @Field

    Environment[]
    environment


@Field def dockerImage
    @Field def mountCommand

        @Field def AWS_REGION

        @Field def envArray =

    []


@Field def secretParams =


[:]

@Field def htmlReportFiles =


[]


@Field def dockerVersion
    @Field def playwrightVersion

        @Field def containerName

        @Field def smStatus

        @Field def smEnvRun

        @Field

    String
    jenkins_account


@Field


String
junitFileMask


@Field


String
runTimeOut = '60'


@Field


String
runMemory = '1g'


@Field


Boolean
toggle = false


@Field


String
parallelTest


@Field


String
BUILD_CMD


def runJenkinsFile(pipelineConfigPath, envConfigPath, def nodeLabelLocal = 'aws') {


timestamps
{
    ansiColor('xterm')
{
// below
line is to
force
protractor
run
to
AWS
slave,
if provided label is 'cluster'
nodeLabelLocal = (nodeLabelLocal == 'cluster') ? 'aws': nodeLabelLocal

jenkins_account = env.JENKINS_AWS_ACCOUNT

                  // Below if block is
for default properties, Only enabled for staging and QM for now


def smProperties =


[]
smProperties.add(disableConcurrentBuilds())
smProperties.add(durabilityHint('PERFORMANCE_OPTIMIZED'))
println('[INFO] Setting default jenkins job properties')
properties(smProperties)

node(nodeLabelLocal)
{
try {
env.PIPELINE_TYPE = PIPELINE_TEMPLATE_NAME
env.DEPLOYED_ON_STAGING = true
currentBuild.result = 'SUCCESS'
parameters = preparationStage(pipelineConfigPath, envConfigPath) // Prepare pipeline parameters
junitFileMask = parameters.JUNIT_FILE_MASK ?: 'target/junit/*.xml'
if (currentBuild.result == 'FAILURE')
{ // Do
not run
SM if there is an
infra
failure
return
}

def batchMap =


[:]
for (String param: parameters) {
    String batchMatch = param
if (batchMatch.startsWith("BATCH_SUITE")) {
if (batchMatch.contains("=")) {
String[] initialBatch = batchMatch.split("=", 2)
batchMap.put(initialBatch[0], initialBatch[1])
}
}
}

if (batchMap.isEmpty() == false) {
parallelTest = 'true'
envArray.add("parallelTest=${parallelTest}")
pipelineHelperUtils.displayMessage(" Batches to be executed in Sequence, Comma seperated values would be executed in parallel")
for (batch in batchMap) {
pipelineHelperUtils.displayMessage(batch.key + "=" + batch.value)
}

parallel_run =[:]

for (batch in batchMap) {
    paralleltests =[]
paralleltests = batch.value.split(",")
pipelineHelperUtils.displayMessage("paralleltests " + paralleltests)

for (test in paralleltests) {
parallel_run.put("${test}", syntheticMonitor(envArray, "${test}", nodeLabelLocal))

}
stage(batch.key) {
try {
parallel parallel_run
} // Execute Synthetic Monitor
catch(err)
{
    echo
err.getMessage()
}
}
parallel_run = [:]
}
} else {
    parallel_run = [:]
parallelTest = 'false'
parallel_run.put("SyntheticMonitorTests", syntheticMonitor(envArray, "SyntheticMonitorTests", nodeLabelLocal))
parallel
parallel_run // Execute
Synthetic
Monitor

}

//}

} catch(FlowInterruptedException
interruptEx) {
    currentBuild.result = 'ABORTED'
println
"[${PIPELINE_TEMPLATE_NAME}] The pipeline was aborted. ${interruptEx}"
} catch(exception)
{
    currentBuild.result = 'FAILURE'
println
"[${PIPELINE_TEMPLATE_NAME}] An exception occurred: ${exception}"
envArray.add('errorStack=exception')
} finally {
    stage(StageName.getPost())
{
    postBuild(parameters, envArray)
}
}
}
}
}
}

def preparationStage(pipelineConfigPath, envConfigPath) {
    stage(StageName.getPreparation())


{
    pipelineHelperUtils.displayMessage("[${NODE_NAME}][${PIPELINE_TEMPLATE_NAME}][${StageName.getPreparation()}]")
pipelineHelperUtils.setSplunkData('')
pipelineHelperUtils.sendSplunkEvent('Pipeline Start', "${JOB_NAME}", "${BUILD_ID}")
pipelineHelperUtils.setSplunkData(StageName.getPreparation())
pipelineHelperUtils.sendSplunkEvent('Start', "${JOB_NAME}", "${BUILD_ID}")
pipelineHelperUtils.simpleCheckout()
parameterFileValidator(pipelineConfigPath)
PIPELINE_STASH_NAME = PIPELINE_TEMPLATE_NAME + env.BUILD_ID

                      // getting
this
parameter
from job configuration


def e2e_is_on_remote
    if (params.containsKey("E2E_REMOTE_IP")) {
    e2e_is_on_remote = params['E2E_REMOTE_IP']
    }
    params = readProperties
    file: "${pipelineConfigPath}" // read
    generic
    properties
    for the SM
        params += readProperties
        file: "${envConfigPath}" // read
        env
        specific
        properties
        for the SM
            smEnvRun = params.TARGET_ENVIRONMENT
    AWS_REGION = pipelineHelperUtils.getAWSRegion(params.TARGET_ENVIRONMENT)
    AWS_PARTITION = AWS_REGION.contains("us-gov") ? "aws-us-gov": "aws"
    params['AWS_REGION'] = AWS_REGION

    if (params.TARGET_ENVIRONMENT == "staging") {
    envArray.add("JIRA_AUTH_TOKEN=${xray.getXrayAuth()}")
    envArray.add("XRAY_URL=${xray.get_xray_app_url()}")
    }
    withCredentials([usernamePassword(
        credentialsId: 'report-portal-url-token', passwordVariable: 'jenkins_token', usernameVariable: 'report_portal_url')]) {
        envArray.add("REPORT_PORTAL_URL=${report_portal_url}")
    envArray.add("JENKINS_TOKEN=${jenkins_token}")
    }
    if (params.containsKey("USE_TM_LOGIN") & & params['USE_TM_LOGIN'].trim().equalsIgnoreCase("true")) {
    params['TM_LOGIN'] = awsSecretManagerHelper.getSecretArn("${params.TARGET_ENVIRONMENT}-tm-t0", params.TARGET_ENVIRONMENT, AWS_REGION)
    toggle = true
    }

    if (params.containsKey("USE_EC2_WINDOWS_HOST_PLAYWRIGHT") & & params["USE_EC2_WINDOWS_HOST_PLAYWRIGHT"] == 'true') {
    if (e2e_is_on_remote) {
    params["WINDOWS_HOST"] = e2e_is_on_remote
    } else {
    params["WINDOWS_HOST"] = getWinEc2IpByTag("${JOB_BASE_NAME}")
    }
    }

    // get
    secrets

    def secrets =

    awsSecretManagerHelper.parseSecrets(params)
    {secretArn ->
    return getSecretManagerValue.returnSecretManagerValues(secretArn, params.TARGET_ENVIRONMENT, params.AWS_REGION)
    }

    secrets.each
    {entity ->
    params[entity.key] = entity.value
    if (toggle) {// if TM LOGIN creds then get key value pair for user and password
    entity.value.each {
    params['TM_LOGIN_EMAIL_ADDRESS'] = entity.value.user
    params['TM_LOGIN_PASSWORD'] = entity.value.password
    }
    }

}

// set
run
timeout
if (params['RUN_TIMEOUT'])
{
runTimeOut = params['RUN_TIMEOUT']
pipelineHelperUtils.displayMessage(
    "[${PIPELINE_TEMPLATE_NAME}][${StageName.getPreparation()}] Overwriting default SM timeout with custom value: ${runTimeOut}")
}

if (params['RUN_MEMORY']) {
runMemory = params['RUN_MEMORY']
pipelineHelperUtils.displayMessage(
    "[${PIPELINE_TEMPLATE_NAME}][${StageName.getPreparation()}] Overwriting default SM memory with custom value: ${runTimeOut}")
}


if (params['SSH_EC2'] != 'true') {
params['SSH_EC2'] = 'false'
}

// get
Playwright
version
String
nodejsver = params['NODEJS_VERSION'] ?: "14"
playwrightVersion = playwrightVersions("NO-SSP", params.TARGET_ENVIRONMENT, nodejsver)
                    // check if we
have
an
image or using
default
dockerVersion = playwrightVersion ?: DockerBuilderType.getPlaywrightVer()

initDockerParameters()

containerName = "synthetic." + (params.SSP_COMPONENT ?: (params.APP_CONTEXT ?: "default")) +
                                                                                           "." + params.MONITOR_NAME +
                                                                                           "." + params.TARGET_ENVIRONMENT +
                                                                                           "." + AWS_REGION

pipelineHelperUtils.sendSplunkEvent('End', "${JOB_NAME}", "${BUILD_ID}")
pipelineHelperUtils.displayMessage(
    "[${PIPELINE_TEMPLATE_NAME}][${StageName.getPreparation()}] Done with preparation stage.")

params.each
{param ->
envArray.add("${param.key}=${param.value}") // add
generic + env
specific
properties
to
the
envArray
}
pipelineHelperUtils.doStash(PIPELINE_STASH_NAME)
return params
}
}

def initDockerParameters() {
    dockerImage = DockerBuilderType.getPlaywright14()


mountCommand = DockerAttributes.getDockerMount()

if (params.containsKey('NODEJS_VERSION') & & params['NODEJS_VERSION'] == "16")
{
    dockerImage = DockerBuilderType.getPlaywright16()
}

if (params.containsKey('NODEJS_VERSION') & & params['NODEJS_VERSION'] == "18") {
dockerImage = DockerBuilderType.getPlaywright18()
}
}


def syntheticMonitor(localenv, testname, nodeLabelLocal) {


return {
    stage(testname)
{
// commenting
below
line
due
to
https: // nice - ce - cxone - prod.atlassian.net / browse / CXDEVOPS - 15584
          // node(nodeLabelLocal)
{
    pipelineHelperUtils.displayMessage(
        "[${NODE_NAME}][${PIPELINE_TEMPLATE_NAME}]['Synthetic Monitor Execution'] Running Synthetic Monitors...")
    // localenv.add("testname=${testname}")

pipelineHelperUtils.displayDebugMessage("Starting Unstash for testing step..")
pipelineHelperUtils.doUnstash(PIPELINE_STASH_NAME)

pipelineHelperUtils.setSplunkData('Synthetic Monitor Execution')
pipelineHelperUtils.sendSplunkEvent('Start', "${JOB_NAME}", "${BUILD_ID}")
dockerGid = pipelineHelperUtils.getDockerGid()

dockerArgs = "  ${mountCommand} --memory=${runMemory} --group-add ${dockerGid}"

jenkins_account_id = env.JNK_ACCOUNT_ID
jenkins_region = env.JNK_REGION

sh
"aws ecr get-login-password --region ${jenkins_region} | docker login --username AWS --password-stdin ${jenkins_account_id}.dkr.ecr.${jenkins_region}.amazonaws.com"

wrapperDockerNoCred(dockerArgs, dockerImage, dockerVersion, smEnvRun)
{

    println("${PIPELINE_TEMPLATE_NAME} Checking packge in CodeArtifact")
pipelineHelperUtils.codeArtifactAuthToken('NICE_DEV' as Environment, 'cxone-npm', 'npm')
withEnv(localenv)
{
    timeout(time: "${runTimeOut}", unit: 'MINUTES') {
    pipelineHelperUtils.displayMessage(
        "[${PIPELINE_TEMPLATE_NAME}][${StageName.getBuild()}] Synthetic Monitor Execution")
sh
""" 
			            npm config set fetch-retry-maxtimeout 180000
			            npm install  
			            """

if (params.containsKey('CREATE_SSH_TUNNEL') & & params['CREATE_SSH_TUNNEL'])
{
    pipelineHelperUtils.displayMessage(
        "[${PIPELINE_TEMPLATE_NAME}][${StageName.getBuild()}] Creating SSH Tunnel to ${smEnvRun} environment")
pipelineHelperUtils.credCheckOut()
pipelineHelperUtils.createSSHTunnel(smEnvRun, params)
}

try {
smStatus = 0
if (toggle) {
withCredentials([[$


class: 'AmazonWebServicesCredentialsBinding', credentialsId: "jenkins_user_${TARGET_ENVIRONMENT}"

]]) {
if (parallelTest == 'true')
{
    sh
"""
                                        #!/bin/bash
                                        eval "npm run ${testname}"
                                         """
} else {
    sh
"""
                                        #!/bin/bash
                                        echo eval "${params.BUILD_CMD}"
                                        eval "${params.BUILD_CMD}"
                                        """

}
}
} else {
    withCredentials([[$

class: 'AmazonWebServicesCredentialsBinding', credentialsId: "jenkins_user_${TARGET_ENVIRONMENT}"

],
string(credentialsId: 'TM_PROD_CREDS', variable: 'prodna1_PASS'),
string(credentialsId: 'TM_PROD_EU_Password_SM', variable: 'prodeu_PASS'),
string(credentialsId: 'TM_PROD_Fedramp_Password_SM', variable: 'prodfedramp_PASS'),
string(credentialsId: 'TM_PROD_UK_CREDS_SM', variable: 'produk_PASS'),
string(credentialsId: 'TM_PROD_CA_CREDS_SM', variable: 'prodca_PASS'),
string(credentialsId: 'TM_PROD_AU_CREDS_SM', variable: 'prodau_PASS'),
string(credentialsId: 'TM_PROD_JP_CREDS_SM', variable: 'prodjp_PASS'),
string(credentialsId: 'TM_PROD_FH_CREDS_SM', variable: 'prodfh_PASS'),
string(credentialsId: 'TM_STAGING_CREDS', variable: 'staging_PASS'),
string(credentialsId: 'TM_DEVTEST_CREDS', variable: 'test_PASS')]) {

    sh
"""
                                #!/bin/bash
                                set +x


                                case "${STACK_NAME}" in

                                production)  echo "Using TM Credentials for Production"
                                export TM_LOGIN_PASSWORD="${prodna1_PASS}"
                                ;;

                                production-au)  echo "Using TM Credentials for Production-au"
                                export TM_LOGIN_PASSWORD="${prodau_PASS}"
                                ;; 

                                production-de)  echo "Using TM Credentials for Production-de"
                                export TM_LOGIN_PASSWORD="${prodeu_PASS}"
                                ;;

                                production-fedramp)  echo "Using TM Credentials for Production-fedramp"
                                export TM_LOGIN_PASSWORD="${prodfedramp_PASS}"
                                ;;

                                production-uk)  echo "Using TM Credentials for Production-uk"
                                export TM_LOGIN_PASSWORD="${produk_PASS}"
                                ;;

                                production-ca)  echo "Using TM Credentials for Production-ca"
                                export TM_LOGIN_PASSWORD="${prodca_PASS}"
                                ;;

                                production-jp)  echo "Using TM Credentials for Production-jp"
                                export TM_LOGIN_PASSWORD="${prodjp_PASS}"
                                ;;

                                production-fh)  echo "Using TM Credentials for Production-fh"
                                export TM_LOGIN_PASSWORD="${prodfh_PASS}"
                                ;;

                                staging)  echo "Using TM Credentials for Staging"
                                export TM_LOGIN_PASSWORD="${staging_PASS}"
                                ;;

                                test)  echo "Using TM Credentials for test"
                                export TM_LOGIN_PASSWORD="${test_PASS}"
                                ;;

                                *)  echo "unknown Stack-Name. Make sure this stack is supported with the pipeline template. Exiting"
                                ;;

                                esac
                                echo value of variable parallelTest is ${parallelTest}
                                if [[ "${parallelTest}" == true ]]  
                                then
                                    echo "npm run ${testname}"
                                    eval "npm run ${testname}";

                                else 
                                echo eval "${params.BUILD_CMD}"
                                eval "${params.BUILD_CMD}"
                                fi


                            """
}
}
} catch(Error | Exception
exc) {
    pipelineHelperUtils.displayMessage('failed to run')
currentBuild.result = 'FAILURE'
parameters['ERROR_STACK'] = exc
println("The flow has failed... ${exc}")
smStatus = 1
println("\n return code is: ${smStatus}")
archiveVideoToS3("${STACK_NAME}", "${MONITOR_NAME}")
} finally {
if (env.USE_CUCUMBER_FOR_IT != null & & (
    env.USE_CUCUMBER_FOR_IT).toLowerCase() == "true" & & env.CUCUMBER_REPORT_FOLDER != null)
{
    println("[Info] Generating Cucmber Integration Test report")
pipelineHelperUtils.publishHtmlReport(env.CUCUMBER_REPORT_FOLDER, "cucumber_report.html",
                                      "${STACK_NAME} cucumber IT Report")
}
println("[Info] Generating jUnit Integration Test report")
junit
testResults: junitFileMask, allowEmptyResults: true
}
}
}
}
//}
}
}
}

def getWinEc2IpByTag(String tag

) {
    String
EC2_INSTANCE = ""
location = "--region ${env.JNK_REGION}"
EC2_INSTANCE = sh(
    script: "aws ec2 describe-instances ${location} --filter Name=tag:Name,Values=${tag} | jq -r '.Reservations[0].Instances[0].PrivateIpAddress'", returnStdout: true).trim()
println("${PIPELINE_TEMPLATE_NAME} Checking EC2_INSTANCE ${EC2_INSTANCE}")
if (EC2_INSTANCE == "null")
{ // sometimes
ipv4
network
card is the
2
nd
one
EC2_INSTANCE = sh(
    script: "aws ec2 describe-instances ${location} --filter Name=tag:Name,Values=${tag} | jq -r '.Reservations[1].Instances[0].PrivateIpAddress'", returnStdout: true).trim()
}
if (EC2_INSTANCE == "null") {// sometimes ipv4 network card is the 3rd one
EC2_INSTANCE = sh(script: "aws ec2 describe-instances ${location} --filter Name=tag:Name,Values=${tag} | jq -r '.Reservations[2].Instances[0].PrivateIpAddress'", returnStdout: true).trim()
}
println("Special case of windows tests, changing WINDOWS_HOST value to ${EC2_INSTANCE}")
return EC2_INSTANCE
}

def archiveVideoToS3(String stack_name, String


monitor_name) {
    withAWSJenkinsCreds('test')
{
    println('[Info][archiveVideoToS3] Archiving video file')
String
localDate = new
Date().format('yyyy-MM-dd-HHmm')
String
destFolder = "cxone-sm-video/${stack_name}/${monitor_name}/build-${BUILD_NUMBER}-${localDate}"
sh(script: "aws s3 cp ${WORKSPACE}/test-results/ s3://${destFolder}/ --recursive --exclude \"*\" --include \"*.zip\" --include \"*.webm\"", returnStdout: true)
pipelineHelperUtils.displayMessage('Video file is archived here\n' +
                                   "https://s3.console.aws.amazon.com/s3/buckets/${destFolder}/")
}
}

def postBuild(localParams, envArray) {
if (currentBuild.result == 'ABORTED' | | currentBuild.result == 'FAILURE')


{
    notification
{
    notifyMethod = localParams['NOTIFY_METHOD']
mailRecipients = localParams['MAIL_RECIPIENTS']
mailTemplatePath = 'com/nice/pipeline/templates/pipeline-email.template'
errorStack = localParams['ERROR_STACK']
mailTitle = PIPELINE_STASH_NAME
chatGroups = localParams['CHAT_GROUPS']
}
}

def testStatus =


pipelineHelperUtils.getTestsStatus()

if (testStatus) {
smStatus = (testStatus.failed > 0) ? 1: 0
                                        // Print
out
info
println("[testStatus]: Total:   ${testStatus.total}")
println("[testStatus]: Passed:  ${testStatus.total - testStatus.failed - testStatus.skipped}")
println("[testStatus]: Failed:  ${testStatus.failed}")
println("[testStatus]: Skipped: ${testStatus.skipped}")
}

// notification.verboseNotification(envArray, localParams)
// "smStatus is null"
means
sm
did
not started.If
so - no
need
to
post
metric
to
cloudwatch.
// Otherwise
lets
put
to
cloudwatch
what
we
've got from sm or from test results
if (smStatus != null) {
envArray.add("smStatus=${smStatus}")
smCloudwatchMetric.postCloudWatchMetric(envArray)
}
pipelineHelperUtils.setSplunkData('')
pipelineHelperUtils.sendSplunkEvent('Pipeline End', "${JOB_NAME}", "${BUILD_ID}", currentBuild.result)
}

return this
