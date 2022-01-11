import requests

# test get api result code


def test_getuser():
    p = {'page': 2}
    resp = requests.get("https://reqres.in/api/users", params=p)
    code = resp.status_code
    assert code == 200, "Code doesn't match"

# test get api result values


def test_getuser_result():
    p = {'page': 2}
    resp = requests.get("https://reqres.in/api/users", params=p)
    json_response = resp.json()
    assert json_response['total'] == 12

# test get api results data


def test_getuser_resultdata():
    p = {'page': 2}
    resp = requests.get("https://reqres.in/api/users", params=p)
    json_response = resp.json()
    assert (json_response['data'][0]['email']).endswith(
        "reqres.in"), "email format is not matching"

# test post api result


def test_postuser():
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    resp = requests.post("https://reqres.in/api/users", data=payload)
    assert resp.json()['job'] == "leader"

# test delete api


def test_deleteuser():
    resp = requests.delete("https://reqres.in/api/users/2")
    code = resp.status_code
    assert code == 204, "User deletion failed"

# test slow api , the below test case should pass


def test_get_delayedapi():
    resp = requests.get("https://httpbin.org/delay/3", timeout=5)
    code = resp.status_code
    assert code == 200, "Code doesn't match"

# test api with authentication


def test_user_authentication():
    resp = requests.get("https://the-internet.herokuapp.com/basic_auth", auth=('admin','admin'))
    code = resp.status_code
    assert code == 200, "User is unauthorized"
