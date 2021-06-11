![title4.png](https://www.dropbox.com/s/kg32b53g16zd9q0/title4.png?dl=0&raw=1)

----
# Sumário
 - [Sobre o plugin]()
 - [Instalação]()
    - [QGIS]()
	- [ZIP]()
	- [Erros de instalação]()

----
## 1. Sobre o plugin
Esse plugin tem como objetivo fornecer _data augmentation_ dado uma imagem e pontos de interesse fornecidos.

---
## 2. Instalação
### 2.1 QGIS
Para instalar este _plugin_ é necessário habilitar as opção para mostrar os complementos experimentais em **Complementos > Gerenciar e Instalar Complementos > Opções** e checar a opção  **Mostrar também os complementos experiementais**

![habilitar_opcoes.jpg](https://www.dropbox.com/s/1fk64xkba4n8oke/habilitar_opcoes.jpg?dl=0&raw=1)

Feito isto, basta procurar por **Data Augmentation** no filtro de busca e depois em **Instalar Complemento Experimental**.

![instalar_qgis.jpg](https://www.dropbox.com/s/ec9jxhgszqqyi8t/instalar_qgis.jpg?dl=0&raw=1)
### 2.2 ZIP

Também é possível fazer a instalação manualmente com o projeto no formato zip, para isto basta fazer o download dos códigos neste repostório e selecionar a opção **Instalar a partir do ZIP** na janela de plugins do QGIS e depois em **Instalar Complemento**.

![ZIP](https://i.imgur.com/BoDNix8.png)


### 2.3 Erros de instalação
Caso ocorra algum erro na instalação do _plugin_ relacionado as dependências, recomendamos que tente primeiro instalar os pacotes _scikit-image_ e _opencv_ manualmente pelo _Terminal Python_ do QGIS (Ctrl + Alt + P) usando os comandos:
```
import os
os.system("pip install scikit-image")
os.system("pip install opencv-python")
```
Após isso encerre o _QGIS_, abra novamente e tente reinstalar _plugin_.

![errocv2.jpg](https://www.dropbox.com/s/vchmvwepc4auism/errocv2.jpg?dl=0&raw=1)
**Figura 1:** Exemplo de erro na instalação do plugin.
#

## 3. Exemplo de métodos

> Nota: Os dados que foram usados para teste podem ser acessados na branch **teste** deste 

### 3.1. 



## 3 Acessar os _scripts_:
### 3.1 pelo [_Git_ ](https://git-scm.com/downloads):
#
```
git clone https://github.com/prog-geo/augmentation.git
```
#
> Nota: caso não tenha o Git instalado é necessário baixar o [projeto](https://github.com/prog-geo/augmentation) e acessar a pasta contendo os arquivos baixados pelo prompt antes de seguir os próximos passos.
#### 

## Técnicas aplicadas/ de _data augmentation_

## 4 Execução
### 4.1 Criar o diretório
#### 4.1.1 Linux/Mac:
```
chmod +x setup.sh     
./setup.sh
```

#### 4.1.2 Windows:
```
mkdir augumentedOutput & 
mkdir augumentedOutput\rotated & 
mkdir augumentedOutput\flipped & 
mkdir augumentedOutput\trimmed & 
mkdir augumentedOutput\rescaled & 
mkdir augumentedOutput\hazed & 
mkdir augumentedOutput\cropped & 
mkdir augumentedOutput\segmented & 
mkdir augumentedOutput\truncated & 
mkdir augumentedOutput\edged & 
mkdir augumentedOutput\clouded & 
mkdir augumentedOutput\mosaics & 
mkdir augumentedOutput\original
```

### 4.2 Executar o plugin


## 7  Plugin
Data Augmentation também se encontra na versão de pacote com _Graphical User Interface_ (GUI) e _command-line interface_ (CLI) em linguagem _python_.
As instruções sobre como usa-lo em seu próprio aplicativo estão no link abaixo.

| Pacote | README |
| ------ | ------ |
| Python | [https://github.com/prog-geo/augmentation/blob/main/README.md][PlDb] |

## License

MIT

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
