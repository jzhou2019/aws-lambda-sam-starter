from hello_world import app

def test_lambda_handler():
    event = {}
    context = None
    response = app.lambda_handler(event, context)
    assert response["statusCode"] == 200
    assert response["body"] == "Hello World"