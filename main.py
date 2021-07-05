from importing_modules import *

load_dotenv()

pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_EXECUTABLE')

# _______LISTA PRZYKLADOWYCH GRAFIK
clean_img = os.getenv('EXAMPLE_IMAGES_PATH')

# _______OTWARCEI GRAFIKI DO PRZETWARZANIA W CV2
img = cv.imread(clean_img)

# _______WYŚWIETLANIE WYBRANEJ GRAFIKI
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("test_image.png", img)

# _______UTWORZENIE TEKSTU W PYTESSERACT
text = pytesseract.image_to_string(img)


# _______FUNKCJE PRZETWARZAJĄCE TEKST
# podstawowe czyszczenie kodu. Zwraca listę elementów. Każdy z nich to linijka kodu.
def text_cleaner(text):
    list = text.split("\n")
    for elem in list:
        if elem == "" or elem == " " or elem == "\x0c":
            list.remove(elem)
    return list


# zwraca listę z listami elementów w tekście. Każdy element jest linijką kodu. Ważne do tworzenia stringów
def elements_iterator(text):
    elements_lists = []
    for elem in text:
        elements_list = []
        elements_list.append(elem)
        elements_lists.append(elements_list)
    return elements_lists


# tworzy string z listy elemnentów i zapisuje plik w formacie py
def file_writer(ready_text):
    string_of_list = ""
    for item in ready_text:
        string_of_list += item[0]
        string_of_list += "\n"

    with open('test_ready_file.py', mode='w') as file:
        file.write(string_of_list)


# _______WYWOLYWANIE FUNKCJI
cleaned_text = text_cleaner(text)
elements = elements_iterator(cleaned_text)
created_file = file_writer(elements)
print(elements)