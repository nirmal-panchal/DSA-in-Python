def flipAndInvertImage(image):
        m = len(image)
        for i in range(m):
            n = len(image[i])
            image[i].reverse()

            for j in range(n):
                if image[i][j] == 0:
                    image[i][j] = 1
                else: image[i][j] = 0
        return image

print(flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))