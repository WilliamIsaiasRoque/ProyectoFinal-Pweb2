from django.shortcuts import render
from django.http import JsonResponse
from .models import Comment
from .forms import EmailForm

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
    
def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            # Agregar el código de envío de correo si lo deseas
    else:
        form = EmailForm()

    return render(request, 'send/send_email.html', {'form': form})