from selenium import webdriver
from time import sleep

class ChromeAuto:
    def __init__(self):
        self.driver_path = './chromedriver' #caminho onde está do driver
        self.options = webdriver.ChromeOptions() #salva os dados de login
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )

    def clica_sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element_by_link_text('Sign in')
            btn_sign_in.click()
        except Exception as e:
            print('Erro ao clicar em Sign in:', e)

    def acessa(self, site):
        self.chrome.get(site)

    def sair(self):
        self.chrome.quit()

    def faz_login(self):
        try:
            input_login = self.chrome.find_element_by_id('email')
            input_password = self.chrome.find_element_by_id('pass')
            btn_login = self.chrome.find_element_by_name('login')

            input_login.send_keys('SEU USUARIO AQUI')
            input_password.send_keys('SUA SENHA AQUI')
            sleep(3)
            btn_login.click()

        except Exception as e:
            print('Erro ao fazer login:', e)

    def clica_perfil(self):
        try:
            perfil = self.chrome.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[4]/div[1]/span/div/div[1]/i')
            perfil.click()
        except Exception as e:
            print('Erro ao clicar no perfil:', e)

    def faz_logout(self):
        try:
            logout = self.chrome.find_element_by_css_selector('#mount_0_0 > div > div:nth-child(1) > div.rq0escxv.l9j0dhe7.du4w35lb > div:nth-child(4) > div.n7fi1qx3.hv4rvrfc.b3onmgus.poy2od1o.kr520xx4.ehxjyohh > div:nth-child(2) > div > div > div.j34wkznp.qp9yad78.pmk7jnqg.kr520xx4 > div.iqfcb0g7.tojvnm2t.a6sixzi8.k5wvi7nf.q3lfd5jv.pk4s997a.bipmatt0.cebpdrjk.qowsmv63.owwhemhu.dp1hu0rb.dhp61c6y.l9j0dhe7.iyyx5f41.a8s20v7p > div > div > div > div > div > div > div > div > div.kr520xx4.pedkr2u6.ms05siws.pnx7fd3z.b7h9ocf4.pmk7jnqg.j9ispegn.k4urcfbm > div > div.a8nywdso.sj5x9vvc.rz4wbd8a.ecm0bbzt > div > div:nth-child(4) > div > div.ow4ym5g4.auili1gw.rq0escxv.j83agx80.buofh1pr.g5gj957u.i1fnvgqd.oygrvhab.cxmmr5t8.hcukyx3x.kvgmc6g5.nnctdnn4.hpfvmrgz.qt6c0cv9.jb3vyjys.l9j0dhe7.du4w35lb.bp9cbjyn.btwxx1t3.dflh9lhu.scb9dxdr > div.ow4ym5g4.auili1gw.rq0escxv.j83agx80.buofh1pr.g5gj957u.i1fnvgqd.oygrvhab.cxmmr5t8.hcukyx3x.kvgmc6g5.tgvbjcpo.hpfvmrgz.qt6c0cv9.rz4wbd8a.a8nywdso.jb3vyjys.du4w35lb.bp9cbjyn.btwxx1t3.l9j0dhe7 > div')
            logout.click()
        except Exception as e:
            print('Erro ou clicar em Logout:', e)
'''
    def verifica_usuario(self, usuario):
        profile_link = self.chrome.find_element_by_class_name('user-profile-link')
        profile_link_html = profile_link.get_attribute('innerHTML')
        assert usuario in profile_link_html
'''

if __name__=='__main__':
    chrome = ChromeAuto()
    sleep(1)
    chrome.acessa('https://www.facebook.com/')
    sleep(2)
    chrome.faz_login()
                               # chrome.clica_sign_in()
                               # sleep(2)
    sleep(5)
    chrome.clica_perfil()
                               # sleep(2)
                               # chrome.verifica_usuario('pierrialexander')
    sleep(2)
    chrome.faz_logout()
    sleep(5)
    chrome.sair()



