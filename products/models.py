# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AirConditioners(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Air Conditioners'


class AllAppliances(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'All Appliances'


class AllBooks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'All Books'


class AllCarAndMotorbikeProducts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'All Car and Motorbike Products'


class AllElectronics(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'All Electronics'


class AllEnglish(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'All English'


class AllExerciseAndFitness(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'All Exercise and Fitness'


class AllGroceryAndGourmetFoods(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'All Grocery and Gourmet Foods'


class AllHindi(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'All Hindi'


class AllHomeAndKitchen(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'All Home and Kitchen'


class AllMoviesAndTvShows(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'All Movies and TV Shows'


class AllMusic(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'All Music'


class AllPetSupplies(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'All Pet Supplies'


class AllSportsFitnessAndOutdoors(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'All Sports Fitness and Outdoors'


class AllVideoGames(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'All Video Games'


class AmazonFashion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Amazon Fashion'


class AmazonPharmacy(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Amazon Pharmacy'


class AmazonProducts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Amazon-Products'


class BabyBathSkinAndGrooming(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Baby Bath Skin and Grooming'


class BabyFashion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Baby Fashion'


class BabyProducts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Baby Products'


class Backpacks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Backpacks'


class Badminton(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Badminton'


class BagsAndLuggage(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Bags and Luggage'


class Ballerinas(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ballerinas'


class BeautyAndGrooming(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Beauty and Grooming'


class BedroomLinen(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Bedroom Linen'


class BluRay(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Blu-ray'


class CameraAccessories(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Camera Accessories'


class Cameras(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cameras'


class CampingAndHiking(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Camping and Hiking'


class CarAccessories(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Car Accessories'


class CarElectronics(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Car Electronics'


class CarParts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Car Parts'


class CarAndBikeCare(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Car and Bike Care'


class CardioEquipment(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cardio Equipment'


class CasualShoes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Casual Shoes'


class ChildrensBooks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Childrens Books'


class Clothing(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Clothing'


class CoffeeTeaAndBeverages(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Coffee Tea and Beverages'


class Cricket(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cricket'


class Cycling(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cycling'


class Diapers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Diapers'


class DietAndNutrition(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Diet and Nutrition'


class DogSupplies(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Dog supplies'


class EntertainmentCollectibles(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Entertainment Collectibles'


class EthnicWear(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.FloatField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Ethnic Wear'


class ExamCentral(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Exam Central'


class FashionSalesAndDeals(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.FloatField(blank=True, null=True)
    no_of_ratings = models.FloatField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fashion Sales and Deals'


class FashionSandals(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fashion Sandals'


class FashionAndSilverJewellery(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fashion and Silver Jewellery'


class FictionBooks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fiction Books'


class FilmSongs(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Film Songs'


class FineArt(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fine Art'


class FitnessAccessories(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Fitness Accessories'


class Football(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Football'


class FormalShoes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Formal Shoes'


class Furniture(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Furniture'


class GamingAccessories(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Gaming Accessories'


class GamingConsoles(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Gaming Consoles'


class GardenAndOutdoors(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Garden and Outdoors'


class GoldAndDiamondJewellery(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Gold and Diamond Jewellery'


class HandbagsAndClutches(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Handbags and Clutches'


class Headphones(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Headphones'


class HealthAndPersonalCare(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Health and Personal Care'


class HeatingAndCoolingAppliances(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Heating and Cooling Appliances'


class HomeAudioAndTheater(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Home Audio and Theater'


class HomeDcor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Home Dcor'


class HomeEntertainmentSystems(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Home Entertainment Systems'


class HomeFurnishing(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Home Furnishing'


class HomeImprovement(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Home Improvement'


class HomeStorage(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Home Storage'


class HouseholdSupplies(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Household Supplies'


class IndianClassical(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Indian Classical'


class IndianLanguageBooks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Indian Language Books'


class IndoorLighting(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Indoor Lighting'


class IndustrialAndScientificSupplies(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Industrial and Scientific Supplies'


class Innerwear(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Innerwear'


class InternationalMusic(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'International Music'


class InternationalToyStore(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.FloatField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'International Toy Store'


class JanitorialAndSanitationSupplies(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Janitorial and Sanitation Supplies'


class Jeans(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Jeans'


class Jewellery(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Jewellery'


class KidsClothing(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kids Clothing'


class KidsFashion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kids Fashion'


class KidsShoes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kids Shoes'


class KidsWatches(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kids Watches'


class KindleEbooks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kindle eBooks'


class KitchenStorageAndContainers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kitchen Storage and Containers'


class KitchenAndDining(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kitchen and Dining'


class KitchenAndHomeAppliances(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Kitchen and Home Appliances'


class LabAndScientific(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Lab and Scientific'


class LingerieAndNightwear(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Lingerie and Nightwear'


class LuxuryBeauty(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Luxury Beauty'


class MakeUp(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Make-up'


class MensFashion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Mens Fashion'


class MotorbikeAccessoriesAndParts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Motorbike Accessories and Parts'


class MusicalInstrumentsAndProfessionalAudio(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Musical Instruments and Professional Audio'


class NursingAndFeeding(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Nursing and Feeding'


class PcGames(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PC Games'


class Pantry(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pantry'


class PersonalCareAppliances(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Personal Care Appliances'


class Refrigerators(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Refrigerators'


class RefurbishedAndOpenBox(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.FloatField(blank=True, null=True)
    no_of_ratings = models.FloatField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Refurbished and Open Box'


class Rucksacks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Rucksacks'


class Running(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Running'


class StemToysStore(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.FloatField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'STEM Toys Store'


class SchoolBags(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'School Bags'


class SchoolTextbooks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'School Textbooks'


class SecurityCameras(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Security Cameras'


class SewingAndCraftSupplies(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sewing and Craft Supplies'


class Shirts(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Shirts'


class Shoes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.FloatField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Shoes'


class SnackFoods(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Snack Foods'


class Speakers(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Speakers'


class SportsCollectibles(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sports Collectibles'


class SportsShoes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sports Shoes'


class Sportswear(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sportswear'


class StrengthTraining(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Strength Training'


class StrollersAndPrams(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Strollers and Prams'


class SubscribeAndSave(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Subscribe and Save'


class SuitcasesAndTrolleyBags(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Suitcases and Trolley Bags'


class Sunglasses(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Sunglasses'


class TShirtsAndPolos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'T-shirts and Polos'


class Televisions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Televisions'


class TestMeasureAndInspect(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Test Measure and Inspect'


class Textbooks(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Textbooks'


class TheDesignerBoutique(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.FloatField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'The Designer Boutique'


class ToysGiftingStore(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.FloatField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Toys Gifting Store'


class ToysAndGames(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Toys and Games'


class TravelAccessories(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Travel Accessories'


class TravelDuffles(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Travel Duffles'


class ValueBazaar(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.FloatField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Value Bazaar'


class VideoGamesDeals(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Video Games Deals'


class Wallets(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Wallets'


class WashingMachines(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Washing Machines'


class Watches(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Watches'


class WesternWear(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Western Wear'


class WomensFashion(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Womens Fashion'


class Yoga(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    main_category = models.TextField(blank=True, null=True)
    sub_category = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    ratings = models.TextField(blank=True, null=True)
    no_of_ratings = models.TextField(blank=True, null=True)
    discount_price = models.TextField(blank=True, null=True)
    actual_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Yoga'
