import pickle
import json
import pandas as pd
import numpy as np
import config1

class MagicHome():
    def __init__(self, Area, BHK, Bathroom, Parking, Per_Sqft, Type, Furnishing, Status, Transaction):
        self.Area = Area
        self.BHK = BHK
        self.Bathroom = Bathroom
        self.Parking = Parking
        self.Per_Sqft = Per_Sqft
        self.Type = Type
        self.Furnishing = Furnishing
        self.Status = Status
        self.Transaction = Transaction

    def load_save_data(self):
        with open(config1.MODEL_FILE_PATH, "rb") as f:
            self.model = pickle.load(f)

        with open(config1.PROJECT_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

    def get_predicted_price(self):

        self.load_save_data()  # Calling load_save_data to get model and json_data

        array = np.zeros(len(self.json_data['Columns']))

        array[0] = self.Area
        array[1] = self.BHK
        array[2] = self.Bathroom
        array[3] = self.Parking
        array[4] = self.Per_Sqft
        array[5] = self.json_data['Type'][self.Type]
        array[6] = self.json_data['Furnishing'][self.Furnishing]
        array[7] = self.json_data['Status'][self.Status]
        array[8] = self.json_data['Transaction'][self.Transaction]

        print("Test Array -->\n",array)
        predicted_price = self.model.predict([array])[0]
        print("Predicted_price",predicted_price)
        return np.around(predicted_price, 2)


if __name__ == "__main__":
    Area     =  800
    BHK      =  3
    Bathroom =  2
    Parking  =  1
    Per_Sqft =  6667
    Type     =    "Apartment"
    Furnishing  = "Semi-Furnished"
    Status      = "Ready_to_move"
    Transaction = "New_Property"

    imp_data = MagicHome(Area, BHK, Bathroom, Parking, Per_Sqft, Type, Furnishing, Status, Transaction)
    price = imp_data.get_predicted_price()
    print()
    print(f"Predicted Prices for MagicHome Houses is { price }/- Rs. Only")