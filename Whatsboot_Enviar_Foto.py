from selenium import webdriver
import time
import os


class WhastsappBot:
    def __init__(self):
        self.mensagem = ["Procura-se, mesangem automática"]
        self.grupos = ["Nome do contato"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def EnviarMensagens(self):

        self.driver.get("https://web.whatsapp.com/")
        time.sleep(10)

        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            time.sleep(3)
            grupo.click()
            chat_box = self.driver.find_element_by_xpath("//span[@data-icon='clip']")

            time.sleep(3)
            chat_box.click()
            time.sleep(3)
            chat_box.find_element_by_xpath("//button[@class='_1dxx-']").click()
            time.sleep(3)
           
            #Chama o caminho da imagem através do Autoit.
            os.startfile ("C://Users/casa/PycharmProjects/Whatsbot/AbrirUploadOpi.exe")
            time.sleep(3)
            chat_foto = self.driver.find_element_by_class_name("_3WjMU")
            chat_foto.click()

            time.sleep(3)
            chat_foto.send_keys(self.mensagem)
            time.sleep(3)


            botao_enviar = self.driver.find_element_by_xpath("//span[@data-icon='send']")
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)