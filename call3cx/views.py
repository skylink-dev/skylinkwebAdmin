import json
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

CALLUS_URL = "https://skylink.3cx.in/callus/call"
API_SECRET = "super-secret-token"  # your secret to protect your Django endpoint


@csrf_exempt
@require_POST
def trigger_3cx_call(request):
    # ---- Security check ----
    #auth = request.headers.get("Authorization", "")
    if not auth.startswith("Token ") or auth.split(" ", 1)[1] != API_SECRET:
        return JsonResponse({"error": "unauthorized"}, status=401)

    # ---- Validate JSON ----
    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"error": "invalid_json"}, status=400)

    number = data.get("number")
    party = data.get("party", "cs")  # default "cs"

    if not number:
        return JsonResponse({"error": "number_required"}, status=400)

    # ---- Forward request to 3CX CallUs API ----
    try:
        resp = requests.post(CALLUS_URL, json={
            "number": number,
            "party": party
        }, timeout=10)

        return JsonResponse({
            "status": resp.status_code,
            "response": resp.text
        })

    except Exception as e:
        return JsonResponse({
            "error": "3cx_unreachable",
            "detail": str(e)
        }, status=502)
