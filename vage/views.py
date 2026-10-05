from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe


def recaipe_list(request):

    if request.method == "POST":

        name = request.POST.get('recipe_name')
        description = request.POST.get('recipe_description')
        image = request.FILES.get('recipe_image')

        Recipe.objects.create(
            name=name,
            description=description,
            image=image
        )

        return redirect('/recaipe/')

    recipes = Recipe.objects.all()

    return render(request, 'recaipe_list.html', {
        'recipes': recipes
    })


def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

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


def delete_recipe(request, id):

    if request.method == "POST":
        recipe = get_object_or_404(Recipe, id=id)
        recipe.delete()

    return redirect('/recaipe/')