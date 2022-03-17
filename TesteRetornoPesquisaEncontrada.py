import Controller as c


bot = c.Controller("https://blogdoagi.com.br/",3)
bot.clicar("button","class","search-open search-btn")
bot.preencher("input","class","search-field","Invesimnos")
bot.clicar("input","class","search-submit")
if bot.valida_item("h1","class","archive-title"):
    print("[Success] Teste de resultado de busca realizado com sucesso")
else:
    print("[Error] Pesquisa não encontrada")

bot.fechar()

