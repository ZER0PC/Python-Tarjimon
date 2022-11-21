from googletrans import Translator
from os import system

while True:
	system("cls")

	first_text = str(input("Tarjima qilmoqchi bo'lgan gapni kiriting: "))
	dest_language = str(input("Qaysi tilga tarjima qilmoqchisiz: "))

	try:
		translator = Translator()
		translation = translator.translate(first_text, dest = dest_language)
		print("")
		print(translation.text)
		print("")

		input("Yana tarjima qilish uchun Enterni bosing...")
	except:
		print("Xatolik :( -> Qaytadan urinib ko'ring *")
input("")
input("")