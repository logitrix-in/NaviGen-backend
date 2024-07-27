# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import AirConditioners, AllAppliances, AllBooks, AllCarAndMotorbikeProducts, AllElectronics, AllEnglish, AllExerciseAndFitness, AllGroceryAndGourmetFoods, AllHindi, AllHomeAndKitchen, AllMoviesAndTvShows, AllMusic, AllPetSupplies, AllSportsFitnessAndOutdoors, AllVideoGames, AmazonFashion, AmazonPharmacy, AmazonProducts, BabyBathSkinAndGrooming, BabyFashion, BabyProducts, Backpacks, Badminton, BagsAndLuggage, Ballerinas, BeautyAndGrooming, BedroomLinen, BluRay, CameraAccessories, Cameras, CampingAndHiking, CarAccessories, CarElectronics, CarParts, CarAndBikeCare, CardioEquipment, CasualShoes, ChildrensBooks, Clothing, CoffeeTeaAndBeverages, Cricket, Cycling, Diapers, DietAndNutrition, DogSupplies, EntertainmentCollectibles, EthnicWear, ExamCentral, FashionSalesAndDeals, FashionSandals, FashionAndSilverJewellery, FictionBooks, FilmSongs, FineArt, FitnessAccessories, Football, FormalShoes, Furniture, GamingAccessories, GamingConsoles, GardenAndOutdoors, GoldAndDiamondJewellery, HandbagsAndClutches, Headphones, HealthAndPersonalCare, HeatingAndCoolingAppliances, HomeAudioAndTheater, HomeDcor, HomeEntertainmentSystems, HomeFurnishing, HomeImprovement, HomeStorage, HouseholdSupplies, IndianClassical, IndianLanguageBooks, IndoorLighting, IndustrialAndScientificSupplies, Innerwear, InternationalMusic, InternationalToyStore, JanitorialAndSanitationSupplies, Jeans, Jewellery, KidsClothing, KidsFashion, KidsShoes, KidsWatches, KindleEbooks, KitchenStorageAndContainers, KitchenAndDining, KitchenAndHomeAppliances, LabAndScientific, LingerieAndNightwear, LuxuryBeauty, MakeUp, MensFashion, MotorbikeAccessoriesAndParts, MusicalInstrumentsAndProfessionalAudio, NursingAndFeeding, PcGames, Pantry, PersonalCareAppliances, Refrigerators, RefurbishedAndOpenBox, Rucksacks, Running, StemToysStore, SchoolBags, SchoolTextbooks, SecurityCameras, SewingAndCraftSupplies, Shirts, Shoes, SnackFoods, Speakers, SportsCollectibles, SportsShoes, Sportswear, StrengthTraining, StrollersAndPrams, SubscribeAndSave, SuitcasesAndTrolleyBags, Sunglasses, TShirtsAndPolos, Televisions, TestMeasureAndInspect, Textbooks, TheDesignerBoutique, ToysGiftingStore, ToysAndGames, TravelAccessories, TravelDuffles, ValueBazaar, VideoGamesDeals, Wallets, WashingMachines, Watches, WesternWear, WomensFashion, Yoga


@admin.register(AirConditioners)
class AirConditionersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AllAppliances)
class AllAppliancesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AllBooks)
class AllBooksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AllCarAndMotorbikeProducts)
class AllCarAndMotorbikeProductsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AllElectronics)
class AllElectronicsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AllEnglish)
class AllEnglishAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AllExerciseAndFitness)
class AllExerciseAndFitnessAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AllGroceryAndGourmetFoods)
class AllGroceryAndGourmetFoodsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AllHindi)
class AllHindiAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AllHomeAndKitchen)
class AllHomeAndKitchenAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AllMoviesAndTvShows)
class AllMoviesAndTvShowsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AllMusic)
class AllMusicAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AllPetSupplies)
class AllPetSuppliesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AllSportsFitnessAndOutdoors)
class AllSportsFitnessAndOutdoorsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AllVideoGames)
class AllVideoGamesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AmazonFashion)
class AmazonFashionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AmazonPharmacy)
class AmazonPharmacyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(AmazonProducts)
class AmazonProductsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(BabyBathSkinAndGrooming)
class BabyBathSkinAndGroomingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(BabyFashion)
class BabyFashionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(BabyProducts)
class BabyProductsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Backpacks)
class BackpacksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Badminton)
class BadmintonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(BagsAndLuggage)
class BagsAndLuggageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Ballerinas)
class BallerinasAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(BeautyAndGrooming)
class BeautyAndGroomingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(BedroomLinen)
class BedroomLinenAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(BluRay)
class BluRayAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(CameraAccessories)
class CameraAccessoriesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Cameras)
class CamerasAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(CampingAndHiking)
class CampingAndHikingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(CarAccessories)
class CarAccessoriesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(CarElectronics)
class CarElectronicsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(CarParts)
class CarPartsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(CarAndBikeCare)
class CarAndBikeCareAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(CardioEquipment)
class CardioEquipmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(CasualShoes)
class CasualShoesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(ChildrensBooks)
class ChildrensBooksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(CoffeeTeaAndBeverages)
class CoffeeTeaAndBeveragesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Cricket)
class CricketAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Cycling)
class CyclingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Diapers)
class DiapersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(DietAndNutrition)
class DietAndNutritionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(DogSupplies)
class DogSuppliesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(EntertainmentCollectibles)
class EntertainmentCollectiblesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(EthnicWear)
class EthnicWearAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(ExamCentral)
class ExamCentralAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(FashionSalesAndDeals)
class FashionSalesAndDealsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(FashionSandals)
class FashionSandalsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(FashionAndSilverJewellery)
class FashionAndSilverJewelleryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(FictionBooks)
class FictionBooksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(FilmSongs)
class FilmSongsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(FineArt)
class FineArtAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(FitnessAccessories)
class FitnessAccessoriesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Football)
class FootballAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(FormalShoes)
class FormalShoesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(GamingAccessories)
class GamingAccessoriesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(GamingConsoles)
class GamingConsolesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(GardenAndOutdoors)
class GardenAndOutdoorsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(GoldAndDiamondJewellery)
class GoldAndDiamondJewelleryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(HandbagsAndClutches)
class HandbagsAndClutchesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Headphones)
class HeadphonesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(HealthAndPersonalCare)
class HealthAndPersonalCareAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(HeatingAndCoolingAppliances)
class HeatingAndCoolingAppliancesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(HomeAudioAndTheater)
class HomeAudioAndTheaterAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(HomeDcor)
class HomeDcorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(HomeEntertainmentSystems)
class HomeEntertainmentSystemsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(HomeFurnishing)
class HomeFurnishingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(HomeImprovement)
class HomeImprovementAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(HomeStorage)
class HomeStorageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(HouseholdSupplies)
class HouseholdSuppliesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(IndianClassical)
class IndianClassicalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(IndianLanguageBooks)
class IndianLanguageBooksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(IndoorLighting)
class IndoorLightingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(IndustrialAndScientificSupplies)
class IndustrialAndScientificSuppliesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Innerwear)
class InnerwearAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(InternationalMusic)
class InternationalMusicAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(InternationalToyStore)
class InternationalToyStoreAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(JanitorialAndSanitationSupplies)
class JanitorialAndSanitationSuppliesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Jeans)
class JeansAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Jewellery)
class JewelleryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(KidsClothing)
class KidsClothingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(KidsFashion)
class KidsFashionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(KidsShoes)
class KidsShoesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(KidsWatches)
class KidsWatchesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(KindleEbooks)
class KindleEbooksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(KitchenStorageAndContainers)
class KitchenStorageAndContainersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(KitchenAndDining)
class KitchenAndDiningAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(KitchenAndHomeAppliances)
class KitchenAndHomeAppliancesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(LabAndScientific)
class LabAndScientificAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(LingerieAndNightwear)
class LingerieAndNightwearAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(LuxuryBeauty)
class LuxuryBeautyAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(MakeUp)
class MakeUpAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(MensFashion)
class MensFashionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(MotorbikeAccessoriesAndParts)
class MotorbikeAccessoriesAndPartsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(MusicalInstrumentsAndProfessionalAudio)
class MusicalInstrumentsAndProfessionalAudioAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(NursingAndFeeding)
class NursingAndFeedingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(PcGames)
class PcGamesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Pantry)
class PantryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(PersonalCareAppliances)
class PersonalCareAppliancesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Refrigerators)
class RefrigeratorsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(RefurbishedAndOpenBox)
class RefurbishedAndOpenBoxAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Rucksacks)
class RucksacksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Running)
class RunningAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(StemToysStore)
class StemToysStoreAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(SchoolBags)
class SchoolBagsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(SchoolTextbooks)
class SchoolTextbooksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(SecurityCameras)
class SecurityCamerasAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(SewingAndCraftSupplies)
class SewingAndCraftSuppliesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Shirts)
class ShirtsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Shoes)
class ShoesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(SnackFoods)
class SnackFoodsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Speakers)
class SpeakersAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(SportsCollectibles)
class SportsCollectiblesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(SportsShoes)
class SportsShoesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Sportswear)
class SportswearAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(StrengthTraining)
class StrengthTrainingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(StrollersAndPrams)
class StrollersAndPramsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(SubscribeAndSave)
class SubscribeAndSaveAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(SuitcasesAndTrolleyBags)
class SuitcasesAndTrolleyBagsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Sunglasses)
class SunglassesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(TShirtsAndPolos)
class TShirtsAndPolosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Televisions)
class TelevisionsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(TestMeasureAndInspect)
class TestMeasureAndInspectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Textbooks)
class TextbooksAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(TheDesignerBoutique)
class TheDesignerBoutiqueAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(ToysGiftingStore)
class ToysGiftingStoreAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(ToysAndGames)
class ToysAndGamesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(TravelAccessories)
class TravelAccessoriesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(TravelDuffles)
class TravelDufflesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(ValueBazaar)
class ValueBazaarAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(VideoGamesDeals)
class VideoGamesDealsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Wallets)
class WalletsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(WashingMachines)
class WashingMachinesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Watches)
class WatchesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(WesternWear)
class WesternWearAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(WomensFashion)
class WomensFashionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)


@admin.register(Yoga)
class YogaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'main_category',
        'sub_category',
        'image',
        'link',
        'ratings',
        'no_of_ratings',
        'discount_price',
        'actual_price',
    )
    search_fields = ('name',)
