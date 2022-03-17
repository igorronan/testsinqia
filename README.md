# Teste Automatizado Sinqia

Teste automatizado sobre a pesquisa do blog https://blogdoagi.com.br/


## Preparando Ambiente

* Python 3
        - https://www.python.org/downloads/

* Pacotes necessarios do Python
    ```sh
        #Selenium
        pip3 install selenium
    ```

* Google Chrome
        - https://www.google.pt/intl/pt-PT/chrome/

Verificar a versão do Chrome e realizar o downalod do ChromeDriver compatível
Versão chrome: Menu > Ajuda > Sobre o Google Chrome 

* ChromeDriver (Manter na mesma pasta do app)
        - https://chromedriver.chromium.org/downloads



## Cenários possiveis

Como usuario: Ao clicar na lupa de pesquisa:
Criterios:

1) 
    1.1 Abrir modal de pesquisa;
2) 
    2.1 Habilitar input de texto para inserção;
        2.1.1 Permitir inserir textos, numeros e caracteres;
3)
    3.1 Habilitar Botão de pesquisa;
4)
    4.1 redireciona a pesquisa a pagina de resultados;
5)
    5.1 Exibe as informações, em divs, dos itens encontrados;
    5.2 Cada div deverá conter:
        5.2.1 Data do artigo;
        5.2.2 Titulo;
        5.2.3 Breve descrição;
        5.2.4 Caso tenha, imagem do artigo;
        
    5.3 Exibe pagina informando que nenhum item foi encontrado;
        5.3.1 Titulo;
        5.3.2 Descrição;
        5.3.3 Input para nova pesquisa, com a pesquisa anterior já preenchida;


## Utilização

No prompt de comando:
```sh
    python3 TesteRetornoPesquisaEncontrada.py
```