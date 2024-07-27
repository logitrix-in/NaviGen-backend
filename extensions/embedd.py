import os
import subprocess

models = [
    "AirConditioners", "AllAppliances", "AllBooks", "AllCarAndMotorbikeProducts", "AllElectronics", "AllEnglish",
    "AllExerciseAndFitness", "AllGroceryAndGourmetFoods", "AllHindi", "AllHomeAndKitchen", "AllMoviesAndTvShows",
    "AllMusic", "AllPetSupplies", "AllSportsFitnessAndOutdoors", "AllVideoGames", "AmazonFashion", "AmazonPharmacy",
    "AmazonProducts", "BabyBathSkinAndGrooming", "BabyFashion", "BabyProducts", "Backpacks", "Badminton", "BagsAndLuggage",
    "Ballerinas", "BeautyAndGrooming", "BedroomLinen", "BluRay", "CameraAccessories", "Cameras", "CampingAndHiking",
    "CarAccessories", "CarElectronics", "CarParts", "CarAndBikeCare", "CardioEquipment", "CasualShoes", "ChildrensBooks",
    "Clothing", "CoffeeTeaAndBeverages", "Cricket", "Cycling", "Diapers", "DietAndNutrition", "DogSupplies",
    "EntertainmentCollectibles", "EthnicWear", "ExamCentral", "FashionSalesAndDeals", "FashionSandals",
    "FashionAndSilverJewellery", "FictionBooks", "FilmSongs", "FineArt", "FitnessAccessories", "Football", "FormalShoes",
    "Furniture", "GamingAccessories", "GamingConsoles", "GardenAndOutdoors", "GoldAndDiamondJewellery",
    "HandbagsAndClutches", "Headphones", "HealthAndPersonalCare", "HeatingAndCoolingAppliances", "HomeAudioAndTheater",
    "HomeDcor", "HomeEntertainmentSystems", "HomeFurnishing", "HomeImprovement", "HomeStorage", "HouseholdSupplies",
    "IndianClassical", "IndianLanguageBooks", "IndoorLighting", "IndustrialAndScientificSupplies", "Innerwear",
    "InternationalMusic", "InternationalToyStore", "JanitorialAndSanitationSupplies", "Jeans", "Jewellery", "KidsClothing",
    "KidsFashion", "KidsShoes", "KidsWatches", "KindleEbooks", "KitchenStorageAndContainers", "KitchenAndDining",
    "KitchenAndHomeAppliances", "LabAndScientific", "LingerieAndNightwear", "LuxuryBeauty", "MakeUp", "MensFashion",
    "MotorbikeAccessoriesAndParts", "MusicalInstrumentsAndProfessionalAudio", "NursingAndFeeding", "PcGames", "Pantry",
    "PersonalCareAppliances", "Refrigerators", "RefurbishedAndOpenBox", "Rucksacks", "Running", "StemToysStore", "SchoolBags",
    "SchoolTextbooks", "SecurityCameras", "SewingAndCraftSupplies", "Shirts", "Shoes", "SnackFoods", "Speakers",
    "SportsCollectibles", "SportsShoes", "Sportswear", "StrengthTraining", "StrollersAndPrams", "SubscribeAndSave",
    "SuitcasesAndTrolleyBags", "Sunglasses", "TShirtsAndPolos", "Televisions", "TestMeasureAndInspect", "Textbooks",
    "TheDesignerBoutique", "ToysGiftingStore", "ToysAndGames", "TravelAccessories", "TravelDuffles", "ValueBazaar",
    "VideoGamesDeals", "Wallets", "WashingMachines", "Watches", "WesternWear", "WomensFashion", "Yoga"
]

app_name = "products"

for model in models:
    command = f"python manage.py vectordb_sync {app_name} {model}"
    print(f"Executing: {command}")
    subprocess.run(command, shell=True)
