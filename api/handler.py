from analysis import image_analyzer


def dummy(event, context):
    return {
        "statusCode": 200,
        "body": "Woho"
    }


def analyze_image(event, context):
    body = event['body']
    print(body.keys())
    if 'images' not in body:
        return {"statusCode": 400,
                "body": "Missing arguments"}
    
    result = image_analyzer.read_images(body['images'])
    return {
        "statusCode": 200,
        "body": result
    }
