from dfir_iris_client.case import Case
from dfir_iris_client.session import ClientSession
from dfir_iris_client.helper.utils import get_data_from_resp, assert_api_resp

import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# API Key and IRIS host configuration
api_key = 'kYM-yjNGz4Yr5KkBvlrKuxoHrgaveFDvU6bmNR1jzQVXRuwCn99NKVPX2u_WzXc7U609AZTvubXmGWeBk-LpTg'
host = 'https://192.168.101.14/'  # Adjust if your IRIS instance is hosted on a different address

# Initialize Client Session with IRIS
session = ClientSession(apikey=api_key, host=host, ssl_verify=False)  # Consider proper SSL verification in production

# Initialize the Case instance with the session
case = Case(session=session)

# Case creation parameters
case_params = {
    'case_name': 'Open on 2024-02-13 by administrator',
    'case_description': 'test',  # Assuming you want the 'Case summary' as the description
    'case_customer': 'IrisInitialClient',
    'case_classification': 'Abusive-Content:spam',  # Ensure this classification is valid in your setup
    'soc_id': 'test',
    'create_customer': False  # Set to True if you want to create a new customer if it doesn't exist
}

# Create a new case
status = case.add_case(**case_params)

# Check if the case was created successfully
assert_api_resp(status, soft_fail=False)  # Will raise an exception if the case creation was unsuccessful

# Extract the case ID from the response
case_data = get_data_from_resp(status)
case_id = case_data.get('case_id')

logger.info(f'Successfully created case ID: {case_id}')

