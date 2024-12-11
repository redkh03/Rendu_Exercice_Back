from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Appeler le gestionnaire d'exceptions de DRF
    response = exception_handler(exc, context)
    
    # Exemple de personnalisation du message d'erreur
    if response is not None:
        response.data['status'] = 'error'
        response.data['message'] = str(exc)
    
    return response
