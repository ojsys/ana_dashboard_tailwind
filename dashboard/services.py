# main/services.py
import requests
from datetime import datetime
from .models import DashboardData

class APIService:
    @staticmethod
    def fetch_and_store_data():
        # Replace with your actual API endpoint
        API_URL = "https://api.ona.io/api/v1/data"
        
        try:
            response = requests.get(API_URL)
            data = response.json()
            
            # Process and store the data
            for item in data:
                DashboardData.objects.create(
                    title=item['title'],
                    value=item['value'],
                    category=item['category']
                )
                
            return True
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
            return False
        

