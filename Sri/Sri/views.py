import requests
from django.http import HttpResponse

S3_BASE_URL = "https://project-unity-2.s3.amazonaws.com/static/static/"

def proxy_static_files(request, filename):
    s3_url = f"{S3_BASE_URL}{filename}"
    print(f"Fetching file from {s3_url}")
    try:
        s3_response = requests.get(s3_url)
        if s3_response.status_code == 200:
            return HttpResponse(s3_response.content, content_type=s3_response.headers['Content-Type'])
        else:
            return HttpResponse("File not found", status=404)
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Error fetching file: {str(e)}", status=500)
