from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def handle_home():
    return 'OK', 200


@app.route('/fulfilment', methods=['POST'])
def handle_fulfilment():
    body = request.get_json()
    print(body)
    '''TODO
    (1) get user information
    (2) store the user information
    (3) create a respone
    (4) send the response
    '''
    return jsonify(
        {
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "From my own server."
                        ]
                    }
                }
            ]
        }
    )
