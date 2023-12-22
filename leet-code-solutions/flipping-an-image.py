class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        image = [img[::-1] for img in image]
        for img in image:
            for i in range(len(img)):
                img[i] = img[i]^1
        return image
        

        