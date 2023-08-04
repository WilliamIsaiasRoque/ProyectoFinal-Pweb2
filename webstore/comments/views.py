from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Comment
from django.core.mail import send_mail
from .forms import EmailForm
from django.contrib import messages

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
            subject = form.cleaned_data['subject']
            sender_email = form.cleaned_data['sender_email']
            message = form.cleaned_data['message']

            # Agrega aquí la dirección de correo del receptor
            recipient_email = 'jluisLAB@gmail.com'
            
            all_message = f"De: {sender_email}\n\n{message}"

            # Envía el correo
            send_mail(subject, all_message, sender_email, [recipient_email], fail_silently=False)

            messages.success(request, '¡Correo enviado con éxito!')
            
            return redirect('send_email')
    else:
        form = EmailForm()

    return render(request, 'send_email.html', {'form': form})