import face_detect_CVega as cv


def main():
    while True:
        main_menu()
        choose_option()


def main_menu():
    print("------------------")
    print("------OpenCV------")
    print("------------------")
    print("\n¿Qué desea hacer?")
    print("\n1. Detectar caras en foto de ABBA")
    print("2. Detectar caras en foto personal con calibración de scaleFactor")
    print("3. Detectar caras utilizando webcam")
    print("4. Detectar caras utilizando webcam con ingreso de scaleFactor")
    print("0. Salir")


def choose_option():
    option = input("Opción: ")
    if option == "1":
        option1()
    elif option == "2":
        option2()
    elif option == "3":
        option3()
    elif option == "4":
        option4()
    elif option == "0":
        exit()
    else:
        print("Opción inválida")
        choose_option()


def option1():
    """Detectar caras en foto de ABBA (abba.png)"""
    cv.detect('./FaceDetect/abba.png')


def option2():
    """Detectar caras en foto personal con calibración de scaleFactor"""
    src = input("Path: ")
    scaleFactor = input("scaleFactor: ")
    cv.detect(src, float(scaleFactor))


def option3():
    """Detectar caras desde webcam con scaleFactor=1.1"""
    cv.detect_webcam()


def option4():
    """Detectar caras desde webcam con ingreso de scaleFactor"""
    scaleFactor = input("scaleFactor: ")
    cv.detect_webcam(int(scaleFactor))


main()
