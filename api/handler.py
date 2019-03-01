import json

from analysis import image_analyzer


def dummy(event, context):
    return {
        "statusCode": 200,
        "body": "Woho"
    }


def analyze_image(event, context):
    body = json.loads(event['body'])
    if 'image' not in body:
        return {"statusCode": 400,
                "body": "Missing arguments"}
    
    result = image_analyzer.read_image(body['image'])
    return {
        "statusCode": 200,
        "body": result
    }


def analyze_images(event, context):
    body = json.loads(event['body'])
    if 'images' not in body:
        return {"statusCode": 400,
                "body": "Missing arguments"}

    result = image_analyzer.read_images(body['images'])
    return {
        "statusCode": 200,
        "body": result
    }
