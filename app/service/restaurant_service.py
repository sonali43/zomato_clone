from app.repo.restaurant_repo import RestaurantRepo


class RestaurantService:
    def __init__(self, repository:RestaurantRepo):
        self.repository: RestaurantRepo= repository
        
    def get_restaurant(self):
        return 
    
    def get_restaurant_by_id(self, restaurant_id):
        return
    
    def create_restaurant(self, restaurant_data):
        restaurant = self.repository.get_restaurant_by_email(restaurant_data.email)
        if restaurant:
            raise ValueError("Restaurant with this email already exists")
        
        return self.repository.create_restaurant(
            name=restaurant_data.name,
            email_input= restaurant_data.email,
            location = restaurant_data.location
        )
        
        def update_restaurant(self,restaurant_id, restaurant_data):
            return
        
        def delete_restaurant(Self, restaurant_id):
            return