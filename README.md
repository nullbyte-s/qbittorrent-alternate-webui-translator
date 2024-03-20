# qBittorrent Alternate WebUI Translator

Este projeto tem como objetivo traduzir qualquer interface WebUI do qBittorrent do inglês para o português brasileiro. O qBittorrent é um cliente de torrent de código aberto e multiplataforma, e a tradução da sua interface permite que os usuários brasileiros tenham uma experiência mais amigável e acessível.

## Instruções de Uso

- Clone este repositório para o seu ambiente local usando o seguinte comando:

```
git clone https://github.com/nullbyte-s/qbittorrent-alternate-webui-translator.git
```

- Após clonar o repositório, navegue até a pasta raiz do projeto:

```
cd qbittorrent-alternate-webui-translator
```

- Copie as pastas “private” e “public” da WebUI que você deseja traduzir para a pasta "webui" desse projeto:

#### Linux
```
cp -r private public caminho/para/qbittorrent-alternate-webui-translator/webui/
```

#### Windows
```
xcopy /E /I private caminho\para\qbittorrent-alternate-webui-translator\webui\
xcopy /E /I public caminho\para\qbittorrent-alternate-webui-translator\webui\
```

- Certifique-se de ter o Python instalado em seu sistema.

- No terminal (ou prompt de comando no Windows), navegue até a pasta onde está o arquivo “translator.pyw” e execute:

#### Linux
```
python3 translator.pyw
```

#### Windows
```
python translator.pyw
```

- Se preferir uma execução discreta, basta clicar duas vezes no arquivo “translator.pyw” no explorador de arquivos, e ele aplicará a tradução sem exibir a janela do terminal.


Espero que esta tradução torne a experiência do qBittorrent mais acessível para a comunidade brasileira 🚀

-------------

<h5 align="center">
  Made with 💜 by <a href="https://github.com/nullbyte-s/">nullbyte-s</a><br>
  <a href="https://choosealicense.com/licenses/mit/"><br>
  <img src="https://img.shields.io/badge/License-MIT-green.svg">
  </a>
</h5>
