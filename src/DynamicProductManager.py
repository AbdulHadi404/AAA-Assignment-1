from typing import List, Optional
from Product import Product

class DynamicProductManager:
    def __init__(self, initial_capacity: int = 5):
        # Initialize the product manager with a specified capacity
        self.capacity = initial_capacity
        self.size = 0
        # Create a list to store products, initialized with None up to the initial capacity
        self.products: List[Optional[Product]] = [None] * self.capacity

    def add_product(self, product: Product):
        # Add a product to the list, reallocating if capacity is reached
        if self.size >= self.capacity:
            self._reallocate()
        self.products[self.size] = product
        self.size += 1
        print(f"Product {product.product_name} added.")

    def delete_product(self, product_id: int):
        # Delete a product by product ID, shifting remaining products down
        for i in range(self.size):
            if self.products[i] and self.products[i].product_id == product_id:
                # Shift elements to fill the gap
                for j in range(i, self.size - 1):
                    self.products[j] = self.products[j + 1]
                # Remove last product reference and reduce size
                self.products[self.size - 1] = None
                self.size -= 1
                print(f"Product with ID {product_id} deleted.")
                return

    def _reallocate(self):
        # Double the capacity of the product list when more space is needed
        self.capacity *= 2
        new_storage = [None] * self.capacity
        # Copy old products into new storage with increased capacity
        for i in range(self.size):
            new_storage[i] = self.products[i]
        self.products = new_storage
        print(f"Reallocated to new capacity: {self.capacity}")
    
    def calculate_total_revenue(self, index=0) -> float:
        # Recursively calculate the total revenue of all products
        if index >= self.size:
            return 0
        # Calculate revenue for the current product, if it exists
        current_product = self.products[index]
        current_revenue = current_product.sales_volume * current_product.price if current_product else 0
        # Recursively add revenue of remaining products
        return current_revenue + self.calculate_total_revenue(index + 1)
    
    def find_combinations_within_budget(self, budget: float):
        # Use backtracking to find all product combinations within a given budget
        def backtrack(start: int, current_combination: List[Product], current_price: float):
            # Print valid combinations within budget
            if current_price <= budget:
                print(f"Valid combination: {[p.product_name for p in current_combination]} - Total Price: {current_price:.2f}")
            # Add each product to the combination if within budget
            for i in range(start, self.size):
                product = self.products[i]
                if product and current_price + product.price <= budget:
                    backtrack(i + 1, current_combination + [product], current_price + product.price)
        
        # Start backtracking from the first product
        backtrack(0, [], 0)
        
    def linear_search(self, product_name: str) -> Optional[Product]:
        # Perform a linear search to find a product by name
        for product in self.products:
            if product and product.product_name.lower() == product_name.lower():
                return product
        return None

    def binary_search(self, product_id: int) -> Optional[Product]:
        # Perform a binary search for a product by product_id after filtering and sorting products
        self.products = [product for product in self.products if product is not None]  
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
        # Perform interpolation search for a product by price after filtering and sorting products
        if not self.products:
            return None
        
        # Filter out None products for sorting
        valid_products = [product for product in self.products if product is not None]  
        valid_products.sort(key=lambda p: p.price) 
        low, high = 0, len(valid_products) - 1

        while low <= high and price >= valid_products[low].price and price <= valid_products[high].price:
            # Handle single-element case if the search is narrowed down to one
            if low == high:
                if valid_products[low].price == price:
                    return valid_products[low]
                return None
            
            # Calculate estimated position using interpolation formula
            pos = low + ((high - low) // (valid_products[high].price - valid_products[low].price) * (price - valid_products[low].price))
            if valid_products[pos].price == price:
                return valid_products[pos]
            if valid_products[pos].price < price:
                low = pos + 1
            else:
                high = pos - 1

        return None 
    
    def bubble_sort(self):
        # Sort the products by price using bubble sort
        n = self.size
        for i in range(n):
            for j in range(0, n-i-1):
                # Swap products if out of order
                if self.products[j] and self.products[j+1] and self.products[j].price > self.products[j+1].price:
                    self.products[j], self.products[j+1] = self.products[j+1], self.products[j]
        print("Products sorted using Bubble Sort.")

    def merge_sort(self):
        # Sort the products by price using merge sort
        self.products = self._merge_sort(self.products[:self.size])
        print("Products sorted using Merge Sort.")

    def _merge_sort(self, products: List[Optional[Product]]) -> List[Optional[Product]]:
        # Helper function for merge sort (recursive), excluding None values
        products = [p for p in products if p is not None]  
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

    def quick_sort(self):
        # Sort the products by price using quick sort
        self._quick_sort(0, self.size - 1)
        print("Products sorted using Quick Sort.")

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
            # Place smaller elements on the left of the pivot
            if self.products[j] and self.products[j].price < pivot:
                i += 1
                self.products[i], self.products[j] = self.products[j], self.products[i]
        # Place pivot element in correct position
        self.products[i + 1], self.products[high] = self.products[high], self.products[i + 1]
        return i + 1
