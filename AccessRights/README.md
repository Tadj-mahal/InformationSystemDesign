# Access Rights in Django
  

### Step 1

**1)** Open project with Bash, I'm using VSCode (you can also download https://git-scm.com/download/win)

**2)** Enter the commands one by one:

> python -m venv venv

> source venv/scripts/activate

> pip install -r requirements.txt

### Step 2
**1)** Before you run project you can create new superuser

> python manage.py createsuperuser

**2)** Run project with next command:

> python manage.py runserver


### Step 3


**1)** Input http://127.0.0.1:8000/ in browser

**2)** Login in site with your superuser data and in http://127.0.0.1:8000/admin choose position 'Director':

![login](/lab1/images/login.png)
![login2](/lab1/images/login2.png)
![position](/lab1/images/position.png)


**3)** You can also create and delete users in 'Director' role:
![create](/lab1/images/create.png)
![create2](/lab1/images/create2.png)

![delete](/lab1/images/delete.png)
![delete2](/lab1/images/delete2.png)

**4)** And you can update user inforamtion in 'Director' and 'Associate Director' roles:

![update](/lab1/images/update.png)
![update2](/lab1/images/update2.png)


