def grey_value(image):
    count_pixel = 0
    sum = 0
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            if image[i][j] == 1:
                sum += image[i][j]
            count_pixel += 1
    grey_value = sum/count_pixel
    return grey_value