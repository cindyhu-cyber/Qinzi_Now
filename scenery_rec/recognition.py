"""
Copyright: Qinzi Now, Tencent Cloud.
"""
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tiia.v20190529 import tiia_client, models

import base64
from utils.config_helper import get_info

s_id, s_key = get_info()
cred = credential.Credential(s_id, s_key)


def rec_main(input_pic):
    try:
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tiia.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = tiia_client.TiiaClient(cred, "ap-beijing", clientProfile)

        req = models.DetectLabelRequest()
        params = {
            "ImageUrl": input_pic
        }
        req.from_json_string(json.dumps(params))

        resp = client.DetectLabel(req)
        return resp.to_json_string()

    except TencentCloudSDKException as err:
        print(err)
