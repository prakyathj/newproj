from django.db import models

Class Driver_Main(models.Model):
	driver_id=models.AutoField(primary_key=True)
	driver_name=models.CharField(null=False, max_length=100)
	driver_ph=models.PositiveIntegerField(null=False, max_length=10)
	driver_Address=models.TextField(null=False)

Class Car(models.Model):
	id=models.AutoField(primary_key=True)
	CAR_MAKE_CHOICES=(
	(Toyota,'toyota'),
	(Mahindra,'mahindra')	
	)
	carmodel=models.CharField(null=False)
	carmake=models.CharField(choices=CAR_MAKE_CHOICES)
	cartype=models.CharField(null=False)
	

Class Driver_sec(models.Model):
	driver_id=models.ForeignKey('Driver_Main')
	driver_star=models.FloatField(max_length=5)
	driver_rides=models.PositiveIntegerField()
	driver_kms=models.PositiveIntegerField()
	
	def updateStar(self,star):
		self.star+=star
		self.save()
	
	def updateNoOfRides(self,kms):
		self.driver_kms+=kms
		self.save()
	
Class Users(models.Model):
	
	
Class Ride(models.Model):
	ride_id=models.AutoField(primary_key=True)
	ride_from=models.CharField(max_length=50)