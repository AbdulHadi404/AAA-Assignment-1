from typing import List, Optional
from Product import Product

class BasicProductManager:
    def __init__(self):
        # Initialize an empty list to store products
        self.products: List[Product] = [] 

    def add_product(self, product: Product):
        # Add a new product to the product list
        self.products.append(product)
        print(f"Product {product.product_name} added.")

    def update_product(self, product_id: int, **updates):
        # Update specific fields of a product identified by product_id
        for product in self.products:
            if product.product_id == product_id:
                # Update each specified field if it exists on the product
                for key, value in updates.items():
                    if hasattr(product, key):
                        setattr(product, key, value)
                        print(f"Updated {key} of Product ID {product_id} to {value}.")
                    else:
                        print(f"Field {key} does not exist on Product.")
                return
        print(f"Product with ID {product_id} not found.")
    
    def delete_product(self, product_id: int):
        # Delete a product by filtering out the product with the given ID
        self.products = [p for p in self.products if p.product_id != product_id]
        print(f"Product with ID {product_id} deleted.")

    def calculate_total_revenue(self, index=0) -> float:
        # Recursively calculate the total revenue of all products
        if index >= len(self.products):
            return 0
        # Calculate revenue for the current product
        current_product = self.products[index]
        current_revenue = current_product.sales_volume * current_product.price
        # Recursively add revenue of remaining products
        return current_revenue + self.calculate_total_revenue(index + 1)
    
    def find_combinations_within_budget(self, budget: float):
        # Use backtracking to find all product combinations within a given budget
        def backtrack(start: int, current_combination: List[Product], current_price: float):
            if current_price <= budget:
                # Print a valid combination if within budget
                print(f"Valid combination: {[p.product_name for p in current_combination]} - Total Price: {current_price:.2f}")
            # Try adding each product to the combination if within budget
            for i in range(start, len(self.products)):
                product = self.products[i]
                if current_price + product.price <= budget:
                    backtrack(i + 1, current_combination + [product], current_price + product.price)
        
        # Start backtracking from the first product
        backtrack(0, [], 0)
        
    def linear_search(self, product_name: str) -> Optional[Product]:
        # Perform a linear search to find a product by name
        for product in self.products:
            if product.product_name.lower() == product_name.lower():
                return product
        return None

    def binary_search(self, product_id: int) -> Optional[Product]:
        # Perform a binary search for a product by product_id; assumes products are sorted by product_id
        self.products.sort(key=lambda p: p.product_id)
        low, high = 0, len(self.products) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.products[mid].product_id == product_id:
                return self.products[mid]
            elif self.products[mid].product_id < product_id:
                low = mid + 1
            else:
                high = mid - 1
        return None

    def interpolation_search(self, price: float) -> Optional[Product]:
        # Perform interpolation search for a product by price; assumes products are sorted by price
        if not self.products:
            return None

        self.products.sort(key=lambda p: p.price)  
        low, high = 0, len(self.products) - 1

        while low <= high and price >= self.products[low].price and price <= self.products[high].price:
            # If all elements are equal, handle single element case
            if low == high:
                if self.products[low].price == price:
                    return self.products[low]
                return None

            # Calculate the position using interpolation formula
            pos = low + int((high - low) / (self.products[high].price - self.products[low].price) * (price - self.products[low].price))
            
            if self.products[pos].price == price:
                return self.products[pos]
            if self.products[pos].price < price:
                low = pos + 1
            else:
                high = pos - 1

        return None

    def bubble_sort(self) -> List[Product]:
        # Sort the products by price using bubble sort
        n = len(self.products)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.products[j].price > self.products[j + 1].price:
                    # Swap products if they are out of order
                    self.products[j], self.products[j + 1] = self.products[j + 1], self.products[j]
        print("Products sorted using Bubble Sort.")
        return self.products

    def merge_sort(self) -> List[Product]:
        # Sort the products by price using merge sort
        sorted_products = self._merge_sort(self.products)
        print("Products sorted using Merge Sort.")
        return sorted_products

    def _merge_sort(self, products: List[Product]) -> List[Product]:
        # Helper function for merge sort (recursive)
        if len(products) > 1:
            mid = len(products) // 2
            left_half = products[:mid]
            right_half = products[mid:]

            left_half = self._merge_sort(left_half)
            right_half = self._merge_sort(right_half)

            i = j = k = 0
            # Merge the sorted halves
            while i < len(left_half) and j < len(right_half):
                if left_half[i].price < right_half[j].price:
                    products[k] = left_half[i]
                    i += 1
                else:
                    products[k] = right_half[j]
                    j += 1
                k += 1

            # Add remaining elements from left and right halves
            while i < len(left_half):
                products[k] = left_half[i]
                i += 1
                k += 1
            while j < len(right_half):
                products[k] = right_half[j]
                j += 1
                k += 1
        return products

    def quick_sort(self) -> List[Product]:
        # Sort the products by price using quick sort
        self._quick_sort(0, len(self.products) - 1)
        print("Products sorted using Quick Sort.")
        return self.products

    def _quick_sort(self, low: int, high: int):
        # Helper function for quick sort (recursive)
        if low < high:
            # Partition the array and sort the partitions
            pi = self._partition(low, high)
            self._quick_sort(low, pi - 1)
            self._quick_sort(pi + 1, high)

    def _partition(self, low: int, high: int) -> int:
        # Partition function for quick sort using last element as pivot
        pivot = self.products[high].price
        i = low - 1
        for j in range(low, high):
            if self.products[j].price < pivot:
                i += 1
                # Swap products to place smaller elements on left
                self.products[i], self.products[j] = self.products[j], self.products[i]
        # Place pivot element in correct position
        self.products[i + 1], self.products[high] = self.products[high], self.products[i + 1]
        return i + 1
