{\rtf1\ansi\ansicpg1252\cocoartf2753
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 """Django's command-line utility for administrative tasks."""\
import os\
import sys\
\
\
def main():\
    """Run administrative tasks."""\
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LittleLemon.settings')\
    try:\
        from django.core.management import execute_from_command_line\
    except ImportError as exc:\
        raise ImportError(\
            "Couldn't import Django. Are you sure it's installed and "\
            "available on your PYTHONPATH environment variable? Did you "\
            "forget to activate a virtual environment?"\
        ) from exc\
    execute_from_command_line(sys.argv)\
\
\
if __name__ == '__main__':\
    main()}