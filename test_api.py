import requests

BASE_URL = "http://127.0.0.1:8000"


def test(name, method, endpoint, data=None, expected=200):
    if method == "GET":
        response = requests.get(
            BASE_URL + endpoint,
            timeout=30
        )
    else:
        response = requests.post(
            BASE_URL + endpoint,
            json=data,
            timeout=120
        )

    print(f"\n--- {name} ---")
    print("HTTP Status:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == expected
    return response.json()


test("Home", "GET", "/")

health = test("Health", "GET", "/health")
assert health["model_loaded"] is True

positive = test(
    "Positive sentiment",
    "POST",
    "/predict",
    {"text": "I love studying computer science!"}
)
assert positive["label"] == "POSITIVE"

negative = test(
    "Negative sentiment",
    "POST",
    "/predict",
    {"text": "This is the worst experience ever!"}
)
assert negative["label"] == "NEGATIVE"

test(
    "Empty input",
    "POST",
    "/predict",
    {"text": ""},
    expected=422
)

test(
    "Missing input",
    "POST",
    "/predict",
    {},
    expected=422
)

test(
    "Whitespace-only input",
    "POST",
    "/predict",
    {"text": "   "},
    expected=400
)

print("\nAll 7 API tests passed!")
