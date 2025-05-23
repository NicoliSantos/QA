from pages.login_page import LoginPage

def test_login_com_dados_validos(driver):
    login = LoginPage(driver)
    login.load("https://exemplo.com/login")
    login.login("usuario_teste", "senha_correta")
    assert "Dashboard" in driver.title

def test_login_com_senha_incorreta(driver):
    login = LoginPage(driver)
    login.load("https://exemplo.com/login")
    login.login("usuario_teste", "senha_errada")
    assert "Usuário ou senha inválidos" in login.get_error_message()

def test_campos_vazios(driver):
    login = LoginPage(driver)
    login.load("https://exemplo.com/login")
    login.login("", "")
    assert "Campos obrigatórios" in login.get_error_message()
