from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            country = form.cleaned_data['country']
            university = form.cleaned_data['university']
            career = form.cleaned_data['career']
            email = form.cleaned_data['email']

            message = f"Nombre: {name}\nApellido: {surname}\nPaís: {country}\nUniversidad: {university}\nCarrera: {career}\nEmail: {email}"

            try:
                send_mail(
                    "Confirmación de recepción de correo y pronta respuesta - Residencias Atlántico",
                    message,
                    email,
                    ["cfb751d4cc4301@inbox.mailtrap.io"],
                    fail_silently=False
                )

                return render(request, 'success.html')

            except Exception as e:
                error_message = f"Error al enviar el correo electrónico: {str(e)}"
                context = {'form': form, 'error_message': error_message}
                return render(request, 'contact.html', context)
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact.html', context)
