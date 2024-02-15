# traballo_ud2_sbd
_Bot de telegram para a asinatura de sistemas_ 

## Instruccións de Instalación
Tras clonar o repositorio, crear un environment en conda con python 3.9.

```
conda create -n nome_do_environment python=3.9
```

Activar o environment e situarse no directorio creado ao clonar o repositorio.

Instalar os paquetes necesarios (indicados no ficheiro requirements.txt).

> [!TIP]
> Podes empregar o seguinte comando.

```
pip install -r requirements.txt
```

Unha vez instalados os paquetes requeridos imos establecer a key necesaria para executar o bot. Para iso debes ter unha key propia e executar o seguinte comando con ela.

```
export TOKEN=o-teu-token
```

E a continuación executar o script que pon en marcha o bot.

```
python3 telegram_bot.py
```

## Comandos e funcións dispoñíbeis

### Lista dos distintos comandos:

- **/tempo**
    - Mostra a predición meteorolóxica para a localidade de Corme.
- **/nasa**
    - Mostra a imaxe do día da Nasa (APOD) co seu título e descrición.
- **/chiste**
    - Conta un chiste.
> [!CAUTION]
> Non podemos garantir que sexan bos chistes.
- **/poke**
    - Mostra a información principal dun pokemos aleatorio.
- **/titulares**
    - Mostra os titulares do día de ElDiario.es.
- **/cartelera**
    - Mostra as películas en cartelera do Marineda City. 
- **/inferno**
    - Mostra o estado de admisión no inferno do autor do bot. 