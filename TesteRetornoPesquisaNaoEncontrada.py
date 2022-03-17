import Controller as c


bot = c.Controller("https://blogdoagi.com.br/",3)
bot.clicar("button","class","search-open search-btn")
bot.preencher("input","class","search-field","WQTERYT@&%#&!Utyuq234324")
bot.clicar("input","class","search-submit")
if bot.valida_item("h1","class","entry-title"):
    print("[Success] Teste de pesquisa incorreta realizado com sucesso.")
else:
    print("[Error] Pesquisa não encontrada")

bot.fechar()

