import os
os.environ['MPLBACKEND'] = 'Agg'

# If using matplotlib anywhere
try:
    import matplotlib
    matplotlib.use('Agg')
except ImportError:
    pass


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TaxiPriceMLProj.settings')

application = get_wsgi_application()
