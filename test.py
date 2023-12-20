import json
def azure_test(event, context):
    return{
        "statusCode": 200,
        'body': json.dumps("What's up Jamell")
    }
    