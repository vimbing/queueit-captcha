import easyocr
import base64
from flask import Response


class Solver:
    def __init__(self, imageb64):
        self.imageb64 = imageb64
        self.image = None
        self.text = ""

    async def getText(self):
        reader = easyocr.Reader(['en'])
        text = reader.readtext(image=self.image, detail=0,
                               decoder="greedy", adjust_contrast=1, contrast_ths=1)

        self.text = text[0].upper()

    async def b64ToImg(self):
        decoded_data = base64.b64decode((self.imageb64))
        self.image = decoded_data

    async def formatToken(self):
        notAllowedChars = '!@#$%^&*()_+=-}{\';:/.,?\\| '

        for char in notAllowedChars:
            if char in self.text:
                self.text = self.text.replace(char, "")

        return self.text

    async def solve(self):
        try:
            await self.b64ToImg()
            await self.getText()
            return {"token": await self.formatToken()}
        except:
            return Response(status=500)
