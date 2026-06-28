import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Contract


def contract_to_json(contract):
    return {
        'name': contract.name,
        'email': contract.email,
        'whatsapp': contract.whatsapp,
        'requirement': contract.requirement,
    }


@csrf_exempt
def contract_content(request):
    if request.method == 'POST':
        try:
            payload = json.loads(request.body.decode('utf-8') or '{}')
        except json.JSONDecodeError:
            return JsonResponse({'errors': {'body': 'Invalid JSON.'}}, status=400)

        required_fields = ('name', 'email', 'whatsapp', 'requirement')
        errors = {
            field: 'This field is required.'
            for field in required_fields
            if not str(payload.get(field, '')).strip()
        }

        if errors:
            return JsonResponse({'errors': errors}, status=400)

        contract = Contract.objects.create(
            name=payload['name'].strip(),
            email=payload['email'].strip(),
            whatsapp=payload['whatsapp'].strip(),
            requirement=payload['requirement'].strip(),
        )
        data = {'id': contract.id, **contract_to_json(contract)}

        return JsonResponse(data, status=201)

    contract = Contract.objects.order_by('-id').first()
    data = {
        'name': '',
        'email': '',
        'whatsapp': '',
        'requirement': '',
    }

    if contract:
        data.update(contract_to_json(contract))

    return JsonResponse(data)
