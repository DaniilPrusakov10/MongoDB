from bson import ObjectId
from django.shortcuts import render, redirect
from django.conf import settings

# Получение коллекции MongoDB
collection = settings.MONGO_COLLECTION

def paper_list(request):
    papers = list(collection.find())

    for paper in papers:
        paper['id'] = str(paper['_id'])  
        del paper['_id'] 
    print(papers)

    reversed_papers = list(reversed(papers))

    return render(request, 'papers/paper_list.html', {'papers': reversed_papers})

# Добавление нового документа
def paper_create(request):
    if request.method == 'POST':
        data = {
            'Title': request.POST.get('Title'),
            'Author': request.POST.get('Author'),
            'Description_short': request.POST.get('Description_short'),
            'Description': request.POST.get('Description'),
            'Date': request.POST.get('Date'),
            'Link': request.POST.get('Link'),
        }
        collection.insert_one(data)
        return redirect('paper_list')
    return render(request, 'papers/paper_form.html')

# Редактирование документа
def paper_update(request, paper_id):
    # Преобразуем строковый id обратно в ObjectId
    paper = collection.find_one({'_id': ObjectId(paper_id)})
    if request.method == 'POST':
        updated_data = {
             'Title': request.POST.get('Title'),
            'Author': request.POST.get('Author'),
            'Description_short': request.POST.get('Description_short'),
            'Description': request.POST.get('Description'),
            'Date': request.POST.get('Date'),
            'Link': request.POST.get('Link'),
        }
        collection.update_one({'_id': ObjectId(paper_id)}, {'$set': updated_data})
        return redirect('paper_list')
    return render(request, 'papers/paper_form.html', {'paper': paper})

# Удаление документа
def paper_delete(request, paper_id):
    # Преобразуем строковый id обратно в ObjectId
    collection.delete_one({'_id': ObjectId(paper_id)})
    return redirect('paper_list')