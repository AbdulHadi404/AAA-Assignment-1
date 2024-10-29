def binary_search(arr, left, right, rating):
    # Perform a binary search for a product with a specific rating
    while left <= right:
        # Calculate the middle index
        mid = left + (right - left) // 2
        # Check if the middle element matches the desired rating
        if arr[mid].rating == rating:
            return arr[mid]  # Return the found product
        # If the middle element's rating is less than the desired rating,
        # search in the right half of the array
        elif arr[mid].rating < rating:
            left = mid + 1
        # If the middle element's rating is greater than the desired rating,
        # search in the left half of the array
        else:
            right = mid - 1
    # If no product with the desired rating is found, return None
    return None

def exponential_search(products, rating):
    # Perform an exponential search for a product with a specific rating
    if len(products) == 0:
        return None  # Return None if the product list is empty

    # Check if the first product matches the desired rating
    if products[0].rating == rating:
        return products[0]

    index = 1
    # Increase the index exponentially to find the range where the product might exist
    while index < len(products) and products[index].rating <= rating:
        index *= 2  # Double the index

    # Perform binary search on the identified range
    return binary_search(products, index // 2, min(index, len(products)) - 1, rating)
