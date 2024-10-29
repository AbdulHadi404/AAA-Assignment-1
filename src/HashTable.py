class Node:
    def __init__(self, product_id: int, product_name: str):
        """Initialize a node with product ID and product name."""
        self.product_id = product_id
        self.product_name = product_name
        self.next = None  # Pointer to the next node in the chain


class HashTableChaining:
    def __init__(self, size: int):
        """Initialize the hash table with a specified size and attributes for collisions and probing."""
        self.size = size
        self.table = [None] * self.size  # Create a list to hold the chains
        self.collisions = 0  # Track the number of collisions
        self.probing_count = 0  # Track the number of probing attempts

    def _hash(self, product_id: int) -> int:
        """Hash function to calculate the index for the given product ID."""
        return product_id % self.size

    def insert(self, product_id: int, product_name: str):
        """Insert a new product into the hash table, using chaining to handle collisions."""
        index = self._hash(product_id)  # Get the index using the hash function
        self.probing_count += 1  # Increment probing attempts for insertion

        if not self.table[index]:
            # If no chain exists at the index, insert the new node directly
            self.table[index] = Node(product_id, product_name)
        else:
            # Collision occurred; increment collision count
            self.collisions += 1  
            current = self.table[index]
            # Traverse to the end of the chain and append the new node
            while current.next:
                current = current.next
            current.next = Node(product_id, product_name)

    def search(self, product_id: int) -> str:
        """Search for a product by its ID using chaining."""
        index = self._hash(product_id)  # Get the index using the hash function
        self.probing_count += 1  # Increment probing attempts for searching

        current = self.table[index]  # Start at the beginning of the chain
        while current:
            if current.product_id == product_id:
                return current.product_name  # Return product name if found
            current = current.next  # Move to the next node
            self.probing_count += 1  # Count each probing step
        return "Product not found"  # Return message if not found

    def display(self):
        """Display the contents of the hash table."""
        for i in range(self.size):
            current = self.table[i]  # Start at the current index
            if current:
                products = []
                # Traverse the chain and collect product details
                while current:
                    products.append(f"{current.product_id}: {current.product_name}")
                    current = current.next
                # Print the index and all products in that chain
                print(f"Index {i}: " + " -> ".join(products))


class HashTableOpenAddressing:
    def __init__(self, size: int):
        """Initialize the hash table with a specified size and attributes for collisions and probing."""
        self.size = size
        self.table = [None] * self.size  # Create a list to hold the products
        self.collisions = 0  # Track the number of collisions
        self.probing_count = 0  # Track the number of probing attempts

    def _hash(self, product_id: int) -> int:
        """Hash function to calculate the index for the given product ID."""
        return product_id % self.size

    def insert(self, product_id: int, product_name: str):
        """Insert a new product into the hash table, using open addressing to handle collisions."""
        index = self._hash(product_id)  # Get the index using the hash function
        self.probing_count += 1  # Increment probing attempts for insertion

        while self.table[index] is not None:
            self.probing_count += 1  # Increment probing attempts
            if self.table[index][0] == product_id:
                # If the product ID already exists, update the product name
                self.table[index] = (product_id, product_name)
                return
            self.collisions += 1  # Collision occurred
            index = (index + 1) % self.size  # Move to the next index (wrap around)

        # Place the new product in the found index
        self.table[index] = (product_id, product_name)

    def search(self, product_id: int) -> str:
        """Search for a product by its ID using open addressing."""
        index = self._hash(product_id)  # Get the index using the hash function
        self.probing_count += 1  # Increment probing attempts for searching

        while self.table[index] is not None:
            if self.table[index][0] == product_id:
                return self.table[index][1]  # Return product name if found
            self.probing_count += 1  # Count each probing step
            index = (index + 1) % self.size  # Move to the next index (wrap around)
        return "Product not found"  # Return message if not found

    def display(self):
        """Display the contents of the hash table."""
        for i in range(self.size):
            if self.table[i] is not None:
                # Print the index and product details
                print(f"Index {i}: {self.table[i][0]}: {self.table[i][1]}")
