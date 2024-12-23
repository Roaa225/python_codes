def calculate_area_of_rectangle(width: float, height: float) -> float:
    """
    This function calculates the area of a rectangle given its width and height.

    Parameters:
    width (float): The width of the rectangle.
    height (float): The height of the rectangle.

    Returns:
    float: The area of the rectangle (width * height).
    """
    return width * height

width = 5.0
height = 10.0
area = calculate_area_of_rectangle(width, height)
print(f"The area of the rectangle is: {area}")
