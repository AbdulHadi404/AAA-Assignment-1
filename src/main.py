from Product import Product
from BasicProductManager import BasicProductManager
from DynamicProductManager import DynamicProductManager
from ExponentialSearch import exponential_search
from KWayMergeSort import k_way_merge_sort
from HashTable import HashTableChaining, HashTableOpenAddressing
from SupplierGraph import SupplierGraph

def main():
    # Part 1: Data Structures and Types
    print("=== Part 1: Data Structures and Types ===")
    # Initialize BasicProductManager instance
    basic_manager = BasicProductManager()

    # Define a list of sample products
    products = [
        Product(101, "Smart TV 50 inch", "Electronics", 499.99, 120, 10, 4.5, 350, 300, 2.5, 201, 5, True, "Premium", 10, 15, "2023-09-01"),
        Product(102, "Leather Jacket", "Apparel", 199.99, 80, 20, 4.8, 120, 150, 3.0, 202, 3, False, "Retail", 5, 25, "2023-08-20"),
        Product(103, "Vacuum Cleaner", "Home Appliances", 129.99, 150, 15, 4.3, 210, 180, 2.2, 203, 4, False, "Wholesale", 7, 18, "2023-07-25"),
        Product(104, "Wireless Headphones", "Electronics", 89.99, 200, 5, 4.7, 500, 100, 2.0, 201, 7, True, "Premium", 8, 20, "2023-09-05"),
        Product(105, "Microwave Oven", "Home Appliances", 69.99, 100, 10, 4.1, 90, 80, 1.5, 203, 5, False, "Wholesale", 4, 18, "2023-08-30"),
        Product(106, "Coffee Maker", "Home Appliances", 49.99, 180, 25, 4.4, 75, 100, 2.8, 202, 2, False, "Retail", 3, 27, "2023-08-15"),
        Product(107, "Gaming Console", "Electronics", 299.99, 60, 12, 4.6, 220, 220, 1.9, 205, 10, True, "Premium", 6, 30, "2023-09-10"),
        Product(108, "Denim Jeans", "Apparel", 59.99, 90, 7, 4.0, 130, 140, 2.1, 203, 4, False, "Wholesale", 6, 22, "2023-08-05"),
        Product(109, "Blender", "Home Appliances", 49.99, 180, 25, 4.4, 75, 100, 2.8, 202, 2, False, "Retail", 3, 27, "2023-07-15"),
        Product(110, "Air Purifier", "Home Appliances", 199.99, 50, 18, 4.5, 200, 200, 1.6, 204, 3, True, "Premium", 7, 25, "2023-09-12"),
    ]

    # Add products to BasicProductManager
    for product in products:
        basic_manager.add_product(product)

    # Display all products in BasicProductManager
    print("Basic Product Manager Products:")
    for product in basic_manager.products:
        print(vars(product))
    
    # Update and delete operations
    print("\nUpdating product with ID 101...")
    basic_manager.update_product(101, price=450.00, stock=100)

    print("\nDeleting product with ID 102...")
    basic_manager.delete_product(102)

    # Part 2: Dynamic Memory Allocation
    print("\n=== Part 2: Dynamic Memory Allocation ===")
    # Initialize DynamicProductManager instance
    dynamic_manager = DynamicProductManager()
    
    # Add products to DynamicProductManager
    for product in products:
        dynamic_manager.add_product(product)

    # Display all products in DynamicProductManager
    print("Dynamic Product Manager Products:")
    for product in dynamic_manager.products:
        if product is not None:
            print(vars(product))

    # Delete product from DynamicProductManager
    print("\nDeleting product with ID 102...")
    dynamic_manager.delete_product(102)

    # Display products after deletion
    print("Products after deletion:")
    for product in dynamic_manager.products:
        if product is not None:
            print(vars(product))

    # Part 3: Recursion and Backtracking
    print("\n=== Part 3: Recursion and Backtracking ===")
    # Calculate total revenue
    total_revenue = dynamic_manager.calculate_total_revenue()
    print(f"Total Revenue: {total_revenue}")

    # Find product combinations within a budget
    budget = 700  
    print(f"\nFinding combinations within the budget of {budget}:")
    dynamic_manager.find_combinations_within_budget(budget)

    # Part 4: Searching Algorithms
    print("\n=== Part 4: Searching Algorithms ===")
    # Linear search for a product by name
    product_name_search = "Smart TV 50 inch"
    found_product = basic_manager.linear_search(product_name_search)
    if found_product:
        print(f"Linear search: Found product by name: {vars(found_product)}\n")

    # Binary search for a product by ID
    product_id_search = 103
    basic_manager.products.sort(key=lambda x: x.product_id) 
    found_product_id = basic_manager.binary_search(product_id_search)
    if found_product_id:
        print(f"Binary search: Found product by ID: {vars(found_product_id)}\n")

    # Interpolation search for a product by price
    product_price_search = 129.99
    basic_manager.products.sort(key=lambda x: x.price) 
    found_product_price = basic_manager.interpolation_search(product_price_search)
    if found_product_price:
        print(f"Interpolation search: Found product by price: {vars(found_product_price)}\n")

    # Part 5: Sorting Algorithms
    print("\n=== Part 5: Sorting Algorithms ===")
    print("Sorting products by Price...")

    basic_manager.products = products.copy()
    print("Bubble Sort:")
    bubble_sorted = basic_manager.bubble_sort()
    print(bubble_sorted)

    basic_manager.products = products.copy()
    print("Merge Sort:")
    merge_sorted = basic_manager.merge_sort()
    print(merge_sorted)

    basic_manager.products = products.copy()
    print("Quick Sort:")
    quick_sorted = basic_manager.quick_sort()
    print(quick_sorted)

    # Part 6: Graph Algorithms
    print("\n=== Part 6: Graph Algorithms ===")
    # Initialize SupplierGraph
    supplier_graph = SupplierGraph()
    # Add categories for each supplier
    supplier_graph.add_product(1, "Electronics")
    supplier_graph.add_product(1, "Home Appliances")
    supplier_graph.add_product(2, "Electronics")
    supplier_graph.add_product(2, "Apparel")
    supplier_graph.add_product(3, "Apparel")
    supplier_graph.add_product(4, "Home Appliances")
    supplier_graph.create_graph()

    # Display Minimum Spanning Tree using Prim's Algorithm
    print("\nMinimum Spanning Tree using Prim's Algorithm:")
    prim_mst = supplier_graph.prim_mst()
    for edge in prim_mst:
        print(f"Supplier {edge[0]} - Supplier {edge[1]}")

    # Display Minimum Spanning Tree using Kruskal's Algorithm
    kruskal_mst = supplier_graph.kruskal_mst()
    print("\nMinimum Spanning Tree using Kruskal's Algorithm:")
    for u, v in kruskal_mst:
        print(f"Supplier {u} -- Supplier {v}")

    print("\n=== Part 7: Hashing ===")

    collision_products = [
    *products,
    Product(201, "Extra Smart TV", "Electronics", 599.99, 150, 12, 4.7, 400, 300, 2.5, 201, 5, True, "Premium", 10, 15, "2023-09-01"),
    Product(202, "Extra Vacuum Cleaner", "Home Appliances", 149.99, 160, 18, 4.2, 220, 180, 2.2, 203, 4, False, "Wholesale", 7, 18, "2023-07-25"),
    ]

    # Hash Table with Chaining
    print("\nUsing Hash Table with Chaining:")
    hash_table_chaining = HashTableChaining(size=10)  
    for product in collision_products:
        hash_table_chaining.insert(product.product_id, product.product_name)

    print("\nHash Table Chaining Contents:")
    hash_table_chaining.display() 

    search_product_id = 101
    found_product_name = hash_table_chaining.search(search_product_id)
    print(f"Search for Product ID {search_product_id}: {found_product_name}")
    print(f"Probing attempts: {hash_table_chaining.probing_count}, Collisions: {hash_table_chaining.collisions}")

    # Hash Table with Open Addressing
    print("\nUsing Hash Table with Open Addressing:")
    hash_table_open_addressing = HashTableOpenAddressing(size=10)  
    for product in basic_manager.products:
        hash_table_open_addressing.insert(product.product_id, product.product_name)

    print("\nHash Table Open Addressing Contents:")
    hash_table_open_addressing.display() 

    found_product_name_open_addressing = hash_table_open_addressing.search(search_product_id)
    print(f"Search for Product ID {search_product_id} in Open Addressing: {found_product_name_open_addressing}")
    print(f"Probing attempts: {hash_table_open_addressing.probing_count}, Collisions: {hash_table_open_addressing.collisions}")

    # Part 8: Bonus Challenge
    print("\n=== Part 8: Bonus Challenge ===")
    # K-Way Merge Sort by Sales Volume
    k_sorted_products = k_way_merge_sort(basic_manager.products, k=3)
    print("K-Way Merge Sorted Products by Sales Volume (Descending):")
    for product in k_sorted_products:
        print(vars(product))

    # Exponential Search for a specific rating
    basic_manager.products.sort(key=lambda x: x.rating)
    print("\nExponential Search for Rating 4.7:")
    found_rating = exponential_search(basic_manager.products, 4.7)
    if found_rating:
        print(f"Found product by rating: {vars(found_rating)}")

if __name__ == "__main__":
    main()
