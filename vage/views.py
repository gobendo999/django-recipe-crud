from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .models import Recipe


@login_required
def recaipe_list(request):

    if request.method == "POST":
        Recipe.objects.create(
            user=request.user,
            name=request.POST.get('recipe_name'),
            description=request.POST.get('recipe_description'),
            image=request.FILES.get('recipe_image'),
        )
        return redirect('/recaipe/')

    query = request.GET.get('q', '').strip()

    recipes = Recipe.objects.filter(user=request.user)

    if query:
        recipes = recipes.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    return render(request, 'recaipe_list.html', {
        'recipes': recipes,
        'query': query,
    })


@login_required
def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, user=request.user)

    if request.method == "POST":
        name = request.POST.get('recipe_name')
        description = request.POST.get('recipe_description')

        if name:
            recipe.name = name
        if description:
            recipe.description = description

        new_image = request.FILES.get('recipe_image')
        if new_image:
            recipe.image = new_image

        recipe.save()
        return redirect('/recaipe/')

    return render(request, 'update_recipe.html', {'recipe': recipe})


@login_required
def delete_recipe(request, id):

    if request.method == "POST":
        recipe = get_object_or_404(Recipe, id=id, user=request.user)
        recipe.delete()

    return redirect('/recaipe/')