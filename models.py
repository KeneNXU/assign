from pymongo import MongoClient
import pandas as pd


class User:
    def __init__(self, db_name, collection_name, mongo_uri='mongodb://localhost:27017/'):
        """
        Initialize the User class with MongoDB connection details.
        :param db_name: The name of the database.
        :param collection_name: The name of the collection.
        :param mongo_uri: The MongoDB connection URI.
        """
        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def fetch_data(self):
        """
        Fetch data from the MongoDB collection.
        :return: A list of dictionaries containing the data from the collection.
        """
        return list(self.collection.find({}))

    def save_to_csv(self, csv_file_path):
        """
        Save the fetched data to a CSV file.
        :param csv_file_path: The path to the CSV file where data should be saved.
        """
        data = self.fetch_data()
        if data:
            # Convert list of dictionaries to DataFrame
            df = pd.DataFrame(data)
            # Write DataFrame to CSV
            df.to_csv(csv_file_path, index=False)
            print(f"Data successfully saved to {csv_file_path}")
        else:
            print("No data found to save.")


# Run
if __name__ == "__main__":
    # Create an instance of the User class
    user = User(db_name='mydatabase', collection_name='users')
    # Save the data to a CSV file
    user.save_to_csv('users_data.csv')
