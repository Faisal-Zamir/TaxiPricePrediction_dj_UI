import sys
import os

# Debug: Track imports
original_import = __builtins__.__import__

def debug_import(name, *args, **kwargs):
    if 'tkinter' in name or '_tkinter' in name:
        print(f"ATTEMPTING TO IMPORT: {name}")
        print("Stack trace:")
        import traceback
        traceback.print_stack()
    return original_import(name, *args, **kwargs)

__builtins__.__import__ = debug_import

# Now set backend
os.environ['MPLBACKEND'] = 'Agg'


from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TaxiPriceMLProj.settings')

application = get_wsgi_application()
