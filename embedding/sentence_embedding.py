import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models

import base64
from utils.config_helper import get_info

s_id, s_key = get_info()
cred = credential.Credential(s_id, s_key)


def sen_embedding(input_sentence):
    try:
        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = nlp_client.NlpClient(cred, "ap-beijing", clientProfile)

        req = models.SentenceEmbeddingRequest()
        message_bytes = input_sentence.encode('ascii')
        params = {
            "Content": str(base64.b64encode(message_bytes))[1:]
        }
        req.from_json_string(json.dumps(params))

        resp = client.SentenceEmbedding(req)
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        print(err)


def run():
    sen_embedding("Here we are, standing in the crowd.")


if __name__ == "__main__":
    run()
