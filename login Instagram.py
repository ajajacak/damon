import requests
import time
import json
import urllib.parse

def login():
    username = input("Enter username: ")
    pas = input("Enter password: ")

    ti = int(time.time())
    pas = f"#PWD_INSTAGRAM:0:{ti}:{pas}"

    url = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/"

    headers = {
        "Host": "i.instagram.com",
        "x-pigeon-session-id": f"UFS-{ti}-35b4-4020-8505-615056274505",
        "x-ig-timezone-offset": "10800",
        "x-ig-connection-type": "WIFI",
        "x-ig-app-id": "567067343352427",
        "x-ig-android-id": "android-67a22a43f4d570e3",
        "x-ig-device-id": "3b3e2317-2a5f-4991-9ed8-8752b7c9b253",
        "x-bloks-version-id": "083f38c334f42c5e3322bb77464c601e8882cd9ff2d30ac915ba7a497539d604",
        "user-agent": "Instagram 369.0.0.46.101 Android (34/14; 320dpi; 720x1440; INFINIX; Infinix X6531; Infinix-X6531; mt6768; en_US; 377314413)",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8"
    }

    params_data = {
        "client_input_params": {
            "contact_point": username,
            "password": pas,
            "device_id": "android-67a22a43f4d570e3",
            "family_device_id": "b0bc78fa-94f2-4a42-9f1c-77102acde7ab",
            "login_attempt_count": 1,
            "event_flow": "login_manual"
        },
        "server_params": {
            "credential_type": "password",
            "login_source": "Login",
            "waterfall_id": "78f5d99a-9659-4b65-8be8-974fdaf9477c"
        }
    }

    payload = {
        "params": json.dumps(params_data),
        "bk_client_context": json.dumps({
            "bloks_version": "083f38c334f42c5e3322bb77464c601e8882cd9ff2d30ac915ba7a497539d604",
            "styles_id": "instagram"
        }),
        "bloks_versioning_id": "083f38c334f42c5e3322bb77464c601e8882cd9ff2d30ac915ba7a497539d604"
    }

    data= urllib.parse.urlencode(payload)

    re = requests.post(url, headers=headers, data=data)

    if "two_step_verification" in re.text:
        print("GOOD (2FA)")
    elif "logged_in_user" in re.text:
        print("GOOD (LOGIN)")
    else:
        print("BAD")


if __name__ == "__main__":
    login()