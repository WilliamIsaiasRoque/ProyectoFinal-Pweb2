from django.shortcuts import render
from django.http import JsonResponse
from .models import Comment
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def comment(request):
    comments = Comment.objects.all()
    return render(request, 'contacto.html', {'comments': comments})

def form_comment(request):
    return render(request, 'comentario_form.html')

def add_comments(request):
    user = request.user
    content = request.POST.get('content', None)

    if content:
        comment = Comment.objects.create(user=user, content=content)
        return JsonResponse({'success': True, 'comment_id': comment.id})
    else:
        return JsonResponse({'success': False, 'error': 'Content is required.'})

@csrf_protect 
def send_email(request):
    if request.method == "POST":
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message') + email

        try:
            send_mail(
                subject,
                message,
                'jescobedooc@unsa.edu.pe',  # Reemplaza con la dirección de correo del remitente
                ['jluislab@gmail.com'],
                fail_silently=False,
            )
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Invalid request method'})