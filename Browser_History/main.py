from module import *
from GUI import *

class Application:
    @staticmethod
    def run() -> None:
        """
        Запускае программу и основной ее жизненный цикл, распределяет и делегирует обработку полученных данных и команд методам другого класса в зависимости от ввода пользователя
        :return: None
        """
        bh = BrowserHistory()

        output_data(output_data_message['program_info'])

        output_data(output_data_message['info'])

        while True:

            data = input_data('Введите команду >> ')

            if not bh.validate_input_data(data):
                output_data(output_data_message['err_comand'])
                continue

            if data == 'exit': return

            if data == '':
                output_data(output_data_message['err_empty'])
                continue

            if data == 'visit':
                url = input(output_data_message['visit'])
                if not bh.visit(url):
                    output_data(output_data_message['err_input'])
                    continue
                output_data(output_data_message['add'])
                continue

            if data == 'back':
                if not bh.back():
                    output_data(output_data_message['err_data'])
                    continue
                output_data(f'{output_data_message['mess']} {bh.back()}')
                continue

            if data == 'all':
                if not bh.all():
                    output_data(output_data_message['err_list'])
                    continue
                output_data(bh.all())
                continue

            if data == 'clear':
                if not bh.clear():
                    output_data(output_data_message['err_clear'])
                bh.clear()
                output_data(output_data_message['clear'])
                continue

            if data == 'forward':
                if not bh.forward():
                    output_data(output_data_message['err_empty'])
                    continue
                output_data(f'{output_data_message['mess']} {bh.forward()}')
                continue

            if data == 'info':
                output_data(output_data_message['info'])
                continue

Application.run()






