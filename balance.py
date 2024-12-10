import os
import requests
import hmac
import base64
import time
import json
from urllib.parse import urlencode

# Configuration
CONFIG = {
    'PRODUCT_TYPE': 'COIN-FUTURES',
    'MARGIN_COIN': 'BTC'
}

# API credentials from environment variables
creds = dict(
    bangbox=dict(ACCESS_KEY = os.environ.get('ACCESS_KEY_BBOX'),
                 SECRET_KEY = os.environ.get('SECRET_KEY_BBOX'),
                 PASSPHRASE = os.environ.get('PASSPHRASE_BBOX')
                 ),
    mri=dict(ACCESS_KEY=os.environ.get('ACCESS_KEY_MRI'),
                 SECRET_KEY=os.environ.get('SECRET_KEY_MRI'),
                 PASSPHRASE=os.environ.get('PASSPHRASE_MRI')
                 ),
)

# API endpoint
BASE_URL = 'https://api.bitget.com'
ENDPOINT = '/api/v2/mix/account/accounts'

def get_timestamp():
    return str(int(time.time() * 1000))

def generate_signature(timestamp, method, request_path, body, secret_key):
    message = timestamp + method.upper() + request_path + (body or '')
    mac = hmac.new(bytes(secret_key, encoding='utf8'), bytes(message, encoding='utf-8'), digestmod='sha256')
    d = mac.digest()
    return base64.b64encode(d).decode()

def api_request(method, endpoint, access_key, passphrase, secret_key, params=None):
    timestamp = get_timestamp()

    request_path = endpoint
    if method == 'GET' and params:
        query_string = urlencode(params)
        request_path = f"{endpoint}?{query_string}"

    body = json.dumps(params) if method == 'POST' else ''

    signature = generate_signature(timestamp, method, request_path, body, secret_key)

    headers = {
        'ACCESS-KEY': access_key,
        'ACCESS-SIGN': signature,
        'ACCESS-TIMESTAMP': timestamp,
        'ACCESS-PASSPHRASE': passphrase,
        'Content-Type': 'application/json'
    }

    url = BASE_URL + request_path

    response = requests.request(method, url, headers=headers, data=body)
    return response

def main():
    params = {
        'productType': CONFIG['PRODUCT_TYPE']
    }

    for key_name, cred_values in creds.items():

        response = api_request('GET', ENDPOINT,
                               cred_values['ACCESS_KEY'],
                               cred_values['PASSPHRASE'],
                               cred_values['SECRET_KEY'],
                               params)

        if response.status_code == 200:
            data = response.json()
            if data.get('code') == '00000':
                btc_account = next((account for account in data['data'] if account['marginCoin'] == CONFIG['MARGIN_COIN']), None)

                if btc_account:
                    print(f"{key_name.upper()}: {btc_account['available']} BTC")
                    '''
                    print(f"####### {key_name.upper()} account #######")
                    print(f"{btc_account['available']} BTC available balance")
                    print(f"Total Equity: {btc_account['accountEquity']} BTC")
                    print(f"Unrealized PNL: {btc_account['unrealizedPL']} BTC")
                    print(f"Max Transferable: {btc_account['maxTransferOut']} BTC")
                    print(f"Equity in USDT: {btc_account['usdtEquity']} USDT")
                    print(f"Equity in BTC: {btc_account['btcEquity']} BTC")
                    '''
                else:
                    print(f"No account found with Margin Coin {CONFIG['MARGIN_COIN']}")
            else:
                print(f"API request failed: {data.get('msg', 'Unknown error')}")
        else:
            print(f"API request failed with status code: {response.status_code}")
            print(f"Response Content: {response.text}")

if __name__ == "__main__":
    main()
