import django
django.setup()
from myApp.seed import run
if __name__=='__main__':
    run()