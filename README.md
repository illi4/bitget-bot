# Bitget scripts

## Balance

This script fetches and displays futures transactions from the Bitget cryptocurrency exchange API. 
It allows you to view your recent futures trading activity across different product types.

## Features

- Fetches futures transactions for a specified time range
- Supports different product types (USDT-FUTURES, COIN-FUTURES, USDC-FUTURES)
- Displays transactions sorted by time (most recent first)
- Configurable time range and transaction limit

## Prerequisites

- Python 3.6 or higher
- `requests` library (install with `pip install requests`)
- Bitget API credentials (API Key, Secret Key, and Passphrase)

## Configuration

The script uses a `CONFIG` dictionary for customization:

```python
# Configuration
CONFIG = {
    'PRODUCT_TYPE': 'COIN-FUTURES',
    'MARGIN_COIN': 'BTC'
}
```
See [bitget api](https://www.bitget.com/api-doc/contract/account/Get-Account-List).

## Setup

1. Clone this repository or download the scripts.
2. Install Python 3 and virtualenv if you do not have it installed yet. The easiest way is to download and install from the [official website](https://www.python.org/downloads/). Instructions to install virtualenv are published on the [python packaging website](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/). 
3. Change to the cloned folder, create a python3 venv and activate it. 
    
    Linux / Mac: 
    ```
    python3 -m venv venv
    . venv/bin/activate
    ```
   
4. Install the required libraries: `pip install -r requirements.txt` 
5. Set up your Bitget API credentials as environment variables (see Environment setup with direnv section). 
5. Run referring to the usage instructions.

## Usage

Modify the CONFIG dictionary in the script if you want to change the product type, time range, or transaction limit.
Run the script:
`python balance.py`

The script will display the fetched transactions, showing the timestamp, transaction type, symbol, amount, and fee for each transaction.
After displaying all transactions, the script will show a summary of closing balances for close_long transactions, grouped by minute.

## Customization

To change the product type, modify the PRODUCT_TYPE value in the CONFIG dictionary.
To adjust the time range, change the TIME_RANGE_DAYS value in the CONFIG dictionary.
To modify the maximum number of transactions fetched, adjust the LIMIT value in the CONFIG dictionary.

## Security Note
Never share your API credentials. The script uses environment variables for security, but make sure to keep your credentials confidential.
Disclaimer
This script is for educational purposes only. Use it at your own risk. Always verify the transactions with your official Bitget account.

## Environment setup with direnv

This project uses `direnv` to manage environment variables. `direnv` is an extension for your shell that loads environment variables from a `.envrc` file when you enter a directory.

### Installing direnv

To install direnv, follow the instructions on the [official direnv website](https://direnv.net/).

### Setting up .envrc

1. Create a file named `.envrc` in your project root directory.
2. Add the following content to the `.envrc` file:

```
export ACCESS_KEY=XXXXX
export SECRET_KEY=XXXXX
export PASSPHRASE=XXXXX
```

3. Replace `XXXXX` with your actual Bitget API credentials.

### Using direnv

1. After creating the `.envrc` file, run the following command in your project directory:
direnv allow
Copy
This command tells direnv that it's safe to load the environment variables from this `.envrc` file.

2. Whenever you enter the project directory, direnv will automatically load these environment variables.

### Security Note

- Never commit your `.envrc` file to version control.
- Add `.envrc` to your `.gitignore` file to prevent accidental commits.

### Troubleshooting

If your environment variables are not being loaded:

1. Ensure direnv is properly installed and hooked into your shell.
2. Make sure you've run `direnv allow` in the project directory.
3. Try restarting your terminal or running `direnv reload`.

For more information on using direnv, refer to the [direnv documentation](https://direnv.net/docs/usage.html).
This section provides a comprehensive guide on setting up and using direnv with your project. It covers installation, configuration of the .envrc file, usage instructions, security considerations, and basic troubleshooting steps. This information will help users of your project set up their environment correctly and securely.
