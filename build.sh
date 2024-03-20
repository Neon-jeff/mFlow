 echo "BUILD START"
 mkdir staticfiles
 python3.10 -m pip install -r requirements.txt
 python3.10 manage.py collectstatic --noinput --clear
 python3.10 manage.py migrate
 echo "BUILD END"
