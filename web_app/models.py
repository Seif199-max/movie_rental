from django.db import models
from django.contrib.auth.models import User


class Movies(models.Model):
    movie_name = models.CharField(max_length=100)
    average_rating = models.FloatField()
    description = models.TextField(default="")
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.movie_name


class Rentals(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):

        if not self.pk:
            if self.movie.quantity >= self.quantity:
                self.movie.quantity -= self.quantity
                self.movie.save()
            else:
                raise ValueError("Not enough stock available!")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.username} rented {self.movie.movie_name}"


class Returns(models.Model):
    rental = models.OneToOneField(Rentals, on_delete=models.CASCADE)
    return_date = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):

        if not self.pk and self.rental:
            self.rental.movie.quantity += self.rental.quantity
            self.rental.movie.save()
            self.rental.delete()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Return of {self.rental.movie.movie_name} by {self.rental.customer.username}"







