from django.db import models

# Create your models here.
class room (models.Model):
    id_room = models.IntegerField(primary_key=True,unique=True,default=0000000)
    room_name = models.CharField(max_length=50)
    number_of_sensors = models.IntegerField(default=00000)
    room_pass = models.CharField(max_length=30,default='.....')


class temperature(models.Model):
    id_temp = models.IntegerField(primary_key=True,unique=True,default=0000000)
    value_temp = models.FloatField(default=000.0000)
    date_temp = models.DateTimeField(auto_now_add=True)
    time_temp =  models.TimeField(auto_now_add=True)
    roomid = models.ForeignKey(room,on_delete=models.CASCADE)

class humidity(models.Model):
    id_hum = models.IntegerField(primary_key=True,unique=True,default=0000000)
    value_hum = models.FloatField(default=000.0000)
    date_hum = models.DateTimeField(auto_now_add=True)
    time_hum =  models.TimeField(auto_now_add=True)
    roomid = models.ForeignKey(room,on_delete=models.CASCADE)


class air_press (models.Model):
    id_air = models.IntegerField(primary_key=True, unique=True, default=0000000)
    value_air = models.FloatField(default=000.0000)
    date_air = models.DateTimeField(auto_now_add=True)
    time_air = models.TimeField(auto_now_add=True)
    roomid = models.ForeignKey(room, on_delete=models.CASCADE)

class co2 (models.Model):
    id_co2 = models.IntegerField(primary_key=True,unique=True,default=0000000)
    value_co2 = models.FloatField(default=000.0000)
    date_co2 = models.DateTimeField(auto_now_add=True)
    time_co2 =  models.TimeField(auto_now_add=True)
    roomid = models.ForeignKey(room,on_delete=models.CASCADE)