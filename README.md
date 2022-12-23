# serverless-with-django

Integrating Django Web Application with AWS Serverless and Deploying ✨

Live Link : https://bv7732t16k.execute-api.us-east-1.amazonaws.com/dev/ 💻

Steps 😇 : 

1. Install node>=v16
2. Clone repository or make your own django application
3. npm install -g serverless
4. Inside project run :  npm install --save-dev serverless-wsgi serverless-python-requirements
5. To check application : sls wsgi serve
6. Create AWS IAM user with S3bucketFullAccess, CloudFormationFullAccess and LambdaFullAccess 
7. Download IAM user credentials in csv
8. Configure on your system by using command aws configure  and enter credetials( if not then install aws-cli on your system ) 
9. Create serverless.yaml file do configuration same as in file ( chose version and region accordingly )
10. Run : sls deploy 

Note : You can use same DB or can create from https://www.elephantsql.com/ for free 😍
