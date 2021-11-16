# RestApi-With-Django-3.2-And-Django-Rest-Framework

## Description

This repository is a Software of Development with Python.

## Virtual

Using pipenv, virtualenv preferably.

## Installation

Using Django, Django Rest Framework preferably.

![alt text](https://icannhas.com/media/images/services/ic-django-rest-framework.png)

## DataBase

Using SQLite3, PostgreSQL, MySQL, MongoDB,etc.

## Apps

Using Postman, Insomnia, Talend API Tester,etc.



## Usage

```shell
$ git clone https://github.com/DanielArturoAlejoAlvarez/RestApi-With-Django-3.2-And-Django-Rest-Framework.git [NAME 
$ source env/bin/activate
$ python manage.py makemigrations
$ pthyon manage.py migrate
$ python manage.py runserver
```

Follow the following steps and you're good to go! Important:

![alt text](https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/138128606/original/734a623bfc7b361d1ecb2418178936ab9bf358e2/make-optimize-rest-apis-using-django-rest-framework.png)

## Coding

### Config

```python
DATABASE_URI='mysql+pymysql://{}:{}@{}/{}'.format(DB_USER,DB_PASSWORD,DB_HOST,DB_NAME)
```

### Authentication

```python
```

### Middlewares

```python
```

### Models

```python
class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('The user must have an email!')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True 
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name 

    def __str__(self):
        return self.email
```

### Views

```python
class HelloAPIView(APIView):
    serializer_class = serializers.HelloSerializer


    def get(self, request, format=None):

        an_apiview = [
            'We use HTTP methods like get,post,put,patch,delete,etc',
            'It is similar a to traditional view in django',
            'It gives us greater control over the logic of the application',
            'It is manually mapped to Urls'
        ]

        return Response({
            'msg': 'Hello World!', 
            'an_apiview': an_apiview
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'Hello {name}'

            return Response({
                'msg': msg
            })

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method': 'DELETE'})
```

### Controllers

```python
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/DanielArturoAlejoAlvarez/RestApi-With-Django-3.2-And-Django-Rest-Framework. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.

## License

The gem is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

```

```