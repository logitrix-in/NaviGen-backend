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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AirConditioners"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AllAppliances"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AllBooks"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AllCarAndMotorbikeProducts"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AllElectronics"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AllEnglish"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AllExerciseAndFitness"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AllGroceryAndGourmetFoods"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AllHindi"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AllHomeAndKitchen"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AllMoviesAndTvShows"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AllMusic"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AllPetSupplies"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AllSportsFitnessAndOutdoors"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AllVideoGames"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AmazonFashion"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AmazonPharmacy"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "AmazonProducts"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "BabyBathSkinAndGrooming"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "BabyFashion"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "BabyProducts"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Backpacks"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Badminton"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "BagsAndLuggage"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Ballerinas"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "BeautyAndGrooming"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "BedroomLinen"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "BluRay"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "CameraAccessories"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Cameras"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "CampingAndHiking"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "CarAccessories"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "CarElectronics"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "CarParts"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "CarAndBikeCare"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "CardioEquipment"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "CasualShoes"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "ChildrensBooks"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Clothing"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "CoffeeTeaAndBeverages"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Cricket"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Cycling"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Diapers"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "DietAndNutrition"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "DogSupplies"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "EntertainmentCollectibles"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "EthnicWear"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "ExamCentral"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "FashionSalesAndDeals"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "FashionSandals"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "FashionAndSilverJewellery"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "FictionBooks"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "FilmSongs"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "FineArt"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "FitnessAccessories"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Football"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "FormalShoes"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Furniture"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "GamingAccessories"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "GamingConsoles"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "GardenAndOutdoors"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "GoldAndDiamondJewellery"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "HandbagsAndClutches"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Headphones"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "HealthAndPersonalCare"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "HeatingAndCoolingAppliances"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "HomeAudioAndTheater"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "HomeDcor"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "HomeEntertainmentSystems"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "HomeFurnishing"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "HomeImprovement"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "HomeStorage"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "HouseholdSupplies"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "IndianClassical"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "IndianLanguageBooks"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "IndoorLighting"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "IndustrialAndScientificSupplies"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Innerwear"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "InternationalMusic"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "InternationalToyStore"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "JanitorialAndSanitationSupplies"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Jeans"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Jewellery"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "KidsClothing"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "KidsFashion"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "KidsShoes"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "KidsWatches"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "KindleEbooks"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "KitchenStorageAndContainers"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "KitchenAndDining"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "KitchenAndHomeAppliances"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "LabAndScientific"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "LingerieAndNightwear"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "LuxuryBeauty"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "MakeUp"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "MensFashion"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "MotorbikeAccessoriesAndParts"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "MusicalInstrumentsAndProfessionalAudio"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "NursingAndFeeding"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "PcGames"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Pantry"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "PersonalCareAppliances"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Refrigerators"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "RefurbishedAndOpenBox"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Rucksacks"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Running"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "StemToysStore"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "SchoolBags"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "SchoolTextbooks"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "SecurityCameras"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "SewingAndCraftSupplies"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Shirts"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Shoes"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "SnackFoods"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Speakers"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "SportsCollectibles"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "SportsShoes"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Sportswear"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "StrengthTraining"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "StrollersAndPrams"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "SubscribeAndSave"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "SuitcasesAndTrolleyBags"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Sunglasses"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "TShirtsAndPolos"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Televisions"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "TestMeasureAndInspect"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Textbooks"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "TheDesignerBoutique"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "ToysGiftingStore"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "ToysAndGames"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "TravelAccessories"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "TravelDuffles"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "ValueBazaar"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "VideoGamesDeals"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Wallets"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "WashingMachines"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Watches"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "WesternWear"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "WomensFashion"}


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

    def get_vectordb_text(self):
        # Use name and main_category for vector search
        return f"{self.name} \n\n {self.main_category}"

    def get_vectordb_metadata(self):
        # Enable filtering by any of these metadata
        return {"name": self.name, "main_category": self.main_category, "model": "Yoga"}
