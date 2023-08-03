from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Comment

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
    
    