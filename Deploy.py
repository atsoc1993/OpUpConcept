from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient
from algokit_utils import ApplicationClient, OnUpdate
from algosdk.atomic_transaction_composer import AccountTransactionSigner
from algosdk.account import address_from_private_key
from pathlib import Path
import os
from dotenv import load_dotenv, set_key

load_dotenv()

algod_token = os.getenv('algod_token')
algod_server = os.getenv('algod_server')
algod_client = AlgodClient(algod_token, algod_server)

indexer_token = os.getenv('indexer_token')
indexer_server = os.getenv('indexer_server')
indexer_client = IndexerClient(indexer_token, indexer_server)

app_spec = Path(__file__).parent / './contract/TestOpcodeBudget.arc32.json'

private_key = os.getenv('private_key')
signer = AccountTransactionSigner(private_key)

address = address_from_private_key(private_key)

params = algod_client.suggested_params()

app_client = ApplicationClient(
    algod_client=algod_client,
    indexer_client=indexer_client,
    app_spec=app_spec,
    app_id=0,
    signer=signer,
    creator=address,
    suggested_params=params,
)

generated_application = app_client.deploy()

#If app is already deployed, update the existing app (assuming you have no boxes or global/local states that must be reset)
#(This requires at least one method with allow_actions=['UpdateApplication'])
#generated_application = app_client.deploy(on_update=OnUpdate.UpdateApp)

#If you need to clear current states like box storage and global/local states, you must replace the app (delete the previous, and create a new app)
#(This requires at least one or more methods with allow_actions=['UpdateApplication', 'DeleteApplcation'] collectively)
#generated_application = app_client.deploy(on_update=OnUpdate.ReplaceApp)

#If you did not include a method with allow actions of 'UpdateApplication' or 'DeleteApplication, you will need to create a new one
#Make sure to include 'UpdateApplication' and 'DeleteApplication' to recycle next time!
#generated_application = app_client.deploy(on_update=OnUpdate.AppendApp)

#Set the 'app_Id' key in our .env to the application ID generated
set_key(
    '.env', 
    key_to_set='app_id', 
    value_to_set=str(generated_application.app.app_id)
)

print(generated_application)

'''
DeployResponse(app=AppMetaData(name='TestOpcodeBudget', version='v1.0', deletable=None, updatable=None, app_id=730541011,
app_address='KSZPHMKBXMCDG6F5FB6YD3X3QJU6OCNUP56JAMXP72VWR3EYQPWENWTZVI', created_round=46546426, updated_round=46546426, 
created_metadata=AppDeployMetaData(name='TestOpcodeBudget', version='v1.0', deletable=None, updatable=None), deleted=False),
create_response=TransactionResponse(tx_id='ASWCVEIT5CSDVTISZVWQMGPPXRNXQUY65SG63BSI4XA2WF4QD53Q', confirmed_round=46546426),
delete_response=None, update_response=None, action_taken=<OperationPerformed.Create: 1>)
'''
