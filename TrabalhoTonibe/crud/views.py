import requests as req
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import addForm
from .models import Banco


def buscar_foto_aleatoria():
    try:
        resp = req.get("https://dog.ceo/api/breeds/image/random", timeout=5)
        return resp.json().get("message")
    except Exception:
        return None


def principal(request):
    cachorros = Banco.objects.all()
    dados = [{
        "id": c.id,
        "nome": c.nomec,
        "idade": c.idadec,
        "raca": c.raca,
        "doenca": c.doenca,
        "imagem": c.imagem
    } for c in cachorros]
    return JsonResponse(dados, safe=False)


def paginahome(request):
    return HttpResponse('API rodando')


@csrf_exempt
def cadastrar(request):
    if request.method == "POST":
        form = addForm(request.POST)
        if form.is_valid():
            obj = form.save()
            foto = buscar_foto_aleatoria()
            if foto:
                obj.imagem = foto
                obj.save()
            return JsonResponse({
                "nome": obj.nomec,
                "idade": obj.idadec,
                "raca": obj.raca,
                "doenca": obj.doenca,
                "imagem": obj.imagem
            }, status=201)
        return JsonResponse({"erro": "Dados inválidos"}, status=400)
    return JsonResponse({"erro": "Método não permitido"}, status=405)
    


