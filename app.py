"""
This script is intended to gather AWS Cognito user information and add new attributes with default values to them.
The script assumes that the attributes have already been added to the user pool in AWS.
"""
import boto3

#Set your credentials here:
aws_access_key_id = ''
aws_secret_access_key = ''

aws_region = ''
user_pool_id = ''  # Use this variable to identity the user_pool_id
user_list_limit = 1  # Use this variable to identify the limit of users returned from AWS. Maximum limit is 60 per AWS
pagination_token = None
done = False
total_users = 0
update_count = 0

# Use this variable to identify the attributes which you would like to set a default value for.
attrs = [
        {
            'Name': 'custom:test_attr',
            'Value': 'Value 1'
        },
        {
            'Name': 'custom:test_attr2',
            'Value': 'Value 2'
        }
    ]

client = boto3.client('cognito-idp',
                      aws_region,
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key
                      )

while not done:
    # Dynamically sets the parameters for the list_users function
    params = {
        'UserPoolId': user_pool_id,
        'Limit': user_list_limit
    }

    # If there is a pagination_token already defined, adds it to the dynamic parameters
    if pagination_token is not None:
        params["PaginationToken"] = pagination_token

    # Gets the list of users from AWS using the dynamic parameters
    user_list = client.list_users(**params)

    try:
        user_list['PaginationToken']
        pagination_token = user_list['PaginationToken']
    except KeyError:
        done = True

    # Iterates over all the users returned from AWS and updates their attributes as described
    for user in user_list['Users']:
        username = user['Username']
        update_count += 1
        total_users += 1

        try:
            new_attr = client.admin_update_user_attributes(
                UserPoolId=user_pool_id,
                Username=username,
                UserAttributes=attrs
            )

        except Exception as e:
            print(f'User {username} had the following issue: {e}')

print(f'Users updated: {update_count}')
print(f'Total users: {total_users}')

# Calculates effectiveness of attribute addition
effectiveness = (update_count/total_users)*100

print(f'Percent users affected: {effectiveness}%')

