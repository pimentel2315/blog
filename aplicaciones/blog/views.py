from django.shortcuts import render
from .models import Post ,Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator 

def home(request):
	queryset = request.GET.get("buscar")
	posts = Post.objects.filter(estado = True)
	if queryset:
		posts = Post.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(decripcion__icontains = queryset)
		).distinct() 
	paginator = Paginator(posts,4)
	page = request.GET.get('page')
	posts = paginator.get_page(page)

	return render(request,'index.html',{'posts':posts})


def detallePost(request,slug):
	post = get_object_or_404(Post,slug=slug)
	return render(request,'post.html',{'detalle_post':post})


	

def generales(request):
	queryset = request.GET.get("buscar")
	posts = Post.objects.filter(
		estado = True,
		
	)
	if queryset:
		posts = Post.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(decripcion__icontains = queryset),
			estado = True,
			categoria = Categoria.objects.get(nombre__iexact = 'Generales')
			).distinct()
	paginator = Paginator(posts,4)
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request,'generales.html',{'posts':posts})

def elementos_pasivos(request):
	queryset = request.GET.get("buscar")
	posts = Post.objects.filter(
		estado = True,
		
	)
	if queryset:
		posts = Post.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(decripcion__icontains = queryset),
			estado = True,
			categoria = Categoria.objects.get(nombre__iexact = 'componentes pasivos')
			).distinct()
	paginator = Paginator(posts,4)
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request,'elementos_pasivos.html',{'posts':posts})

def elementos_activos(request):
	queryset = request.GET.get("buscar")
	posts = Post.objects.filter(
		estado = True,
		
	)
	if queryset:
		posts = Post.objects.filter(
			Q(titulo__icontains = queryset) |
			Q(decripcion__icontains = queryset),
			estado = True,
			categoria = Categoria.objects.get(nombre__iexact = 'componentes activos')
			).distinct()
	paginator = Paginator(posts,4)
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request,'elementos_activos.html',{'posts':posts})
