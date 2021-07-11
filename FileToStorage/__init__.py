import logging
import json
import datetime
import azure.functions as func
from azure.storage.blob import BlobClient
from get_config import load_config

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    req_body = req.get_json()
    message = req_body.get('message')
    logging.info('[HTTP] Message created at: %s with name: %s', message, req_body)

    config = load_config()
    timestamp = datetime.datetime.utcnow()
    # logging.info('[HTTP] Message created at: %s with name: %s', timestamp, message)

    # blobContent = {
    #     "message": message,
    #     "processedTime": f'{timestamp}'
    #     }

    # blobName=f'{blobContent["message"]}-file'


    # sa_conn_str = config["storage_account_connection_string"]
    # sa_container = config["container_name"]

    # blob = BlobClient.from_connection_string(conn_str=sa_conn_str, container_name=sa_container, blob_name=blobName)

    # blob.upload_blob(json.dumps(blobContent))

    return  '{"items": [{"code": 200}), {"result": "done"}]}'
