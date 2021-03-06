import http.client, urllib.request, urllib.parse, urllib.error, base64, sys

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '9e1ddaad5fae4b75829557f669d5e230',
}

params = urllib.parse.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
body = "{ 'url': 'http://everyday-e-news.com/wp-content/uploads/2014/07/6a0120a6812388970b014e8a8ea1e9970d.jpg' }"

try:
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the
    #   URL below with "westcentralus".
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print(e.args)
