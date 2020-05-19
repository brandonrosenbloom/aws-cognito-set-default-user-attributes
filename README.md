# aws-cognito-set-default-user-attributes
## Have you ever:
1. Created cognito users without enriching a custom attribute?
2. Created cognito users only to later realize you needed a new custom attribute?
3. Decided to just add a new custom attribute for your cognito users?

If the answer to any of these questions is yes, then this package is for you!

## What is this?
aws-cognito-set-default-user-attributes is a collection of code which will allow you to easily set attribute values for custom attributes in AWS Cognito.

## How tos:
1. Set the following variables as needed:
    * aws_access_key_id
    * aws_secret_access_key
    * user_pool_id
    * user_list_limit (This is where you define how many user records will be pulled from cognito at a time.)
2. Add your attributes in the attrs dictionary
3. Run app.py

Upon completion, app.py will return a summary of the updates it made and let you know if there were any errors.

Enjoy!
