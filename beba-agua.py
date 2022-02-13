import schedule
from time import sleep
from pynotifier import Notification

def gera_notificacao():
    Notification(
        title='Lembrete',
        description='Hidrate-se, beba água!',
        icon_path='F:\Programmer\Documentos\VSCode\notificacao-desktop\agua.png',
        duration=10).send()

def main():

    schedule.every(5).seconds.do(gera_notificacao)

    while True:
        schedule.run_pending()
        sleep(1)

if __name__ == '__main__':
    main()