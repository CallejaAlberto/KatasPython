def main():
    try:
        configuration = open('C:\Users\Desktop\CursoIntroPython-main\Modulo10Manejodeerrores\config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")


if __name__ == '__main__':
    main()