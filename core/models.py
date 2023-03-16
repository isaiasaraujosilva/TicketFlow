from django.db import models

# Create your models here.
class People(models.Model):

    cpf = models.CharField(max_length=11)
    fires_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    sex = models.CharField(max_length=25)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=25)
    email = models.CharField(max_length=255)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.fires_name
    

class User(models.Model):
    user = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    active = models.BooleanField()
    people = models.OneToOneField(People, on_delete=models.CASCADE, related_name='user_profile')


    def __str__(self):
        return self.user

class Room(models.Model):
    identifier = models.CharField(max_length=255)
    avaliable = models.BooleanField()

    def __str__(self):
        return self.identifier

class Session(models.Model):
    imdb_id = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.DateField()
    room_id = models.ManyToManyField(Room)

    def __str__(self):
        return self.imdb_id
    
class Seat (models.Model):
    row = models.CharField(max_length=10)
    number = models.IntegerField()
    available = models.BooleanField()
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)

class Ticket(models.Model):
    session_id = models.ManyToManyField(Session)
    people_id = models.ForeignKey(People,on_delete=models.CASCADE)
    seat_id = models.OneToOneField(Seat, on_delete=models.CASCADE)

    
class InTheaters(models.Model):
    imdb_id = models.CharField(max_length=25)
    end_time = models.TimeField() 


