from django.shortcuts import render
from django.views import View


# Create your views here.
class Home(View):
    template_home = 'more/test.html'

    def get(self, request):
        user = {
            "name": "raul",
            "lastname": "sanchez"
        }
        context = {"user": user}
        return render(request, self.template_home, context)
