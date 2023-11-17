# Medidor de temperatura 

A solução criada consiste em um sensor de temperatura conectado ao Raspberry Pi Pico W. Após a leitura da temperatura, o microcontrolador envia uma requisição para a rota do [backend](./backend/README.md), que por sua vez cadastra o log de temperatura em um banco de dados no-sql.

Através do nosso [frontend](./frontend/README.md) podemos acessar uma dashboard, podendo assim verificar a última temperatura registrada. 

![](raspberry/IMG_0111.png)
![](raspberry/IMG_0112.png) 

Veja o vídeo de demonstração abaixo:

[Acesse o vídeo no YouTube](https://youtu.be/XEdLyp86nX0)
