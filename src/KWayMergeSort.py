def k_way_merge_sort(products, k):
    # Sort the products using k-way merge sort
    # If the input list has less than 2 elements, it is already sorted
    if len(products) < 2:
        return products

    # Calculate the size of each partition
    part_size = len(products) // k
    parts = []
    
    # Split the products into k parts
    for i in range(0, len(products), part_size):
        parts.append(products[i:i + part_size])

    # Recursively sort each part
    sorted_parts = [k_way_merge_sort(part, k) for part in parts]

    # Merge the sorted parts into a single sorted list
    return merge_k_sorted_lists(sorted_parts)

def merge_k_sorted_lists(sorted_parts):
    # Merge k sorted lists into one sorted list using a min-heap
    import heapq
    
    min_heap = []  # Initialize a min-heap to keep track of the smallest elements
    result = []    # This will hold the final merged result

    # Push the first element of each sorted part into the min-heap
    for i, part in enumerate(sorted_parts):
        if part:  # Check if the part is not empty
            heapq.heappush(min_heap, (part[0].sales_volume, i, 0))  # Store (value, part index, element index)

    # While there are elements in the min-heap
    while min_heap:
        # Get the smallest element from the heap
        sales_volume, part_index, element_index = heapq.heappop(min_heap)
        result.append(sorted_parts[part_index][element_index])  # Add the smallest element to the result

        # If there are more elements in the current part, add the next element to the heap
        if element_index + 1 < len(sorted_parts[part_index]):
            next_element = sorted_parts[part_index][element_index + 1]
            heapq.heappush(min_heap, (next_element.sales_volume, part_index, element_index + 1))

    return result  # Return the merged sorted list
