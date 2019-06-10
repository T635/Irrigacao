# Irrigacao 1.0
Este é um projeto para automatização de um sistema de irrigação, desenvolvido no primeiro semestre de Eng. Elétrica na Unesp de Ilha Solteira, nele serão implementados conceitos de Controle, Automação, IoT, programação em Python e em C++.
Inicialmente, gostaria de deixar claro que este não é o método mais barato e eficaz de se produzir algo do tipo. Entretanto devido a fatores externos, este foi o modo escolhido para o desenvolvimento.
Enfim, a partir dos conceitos explicitados acima, e dos seguintes itens, desenvolveu-se o projeto.
## Objetivo
Introduzir conceitos de IoT e Automação para o agricultor facilitando sua vida, assim como diminuir o consumo de água na agricultura.
## Resumo
O projeto foi desenvolvido com um Raspberry(Rpi) e uma Arduino, o primeiro foi responsável por decidir quando ligar ou nao a irrigação,através da umidade do solo, o segundo foi responsável por ligá-la.
## Itens Usados
###### Raspberry Pi 3 B+                           
###### Módulo frequência de rádio 433MHz
###### Arduino Uno                                  
###### Contator 70 amperes
###### Módulo Relé                                  
###### Relé termico
###### Sensor de umidade do solo
#
## Montagem
A princípio dividi o projeto em duas partes, na primeira ficam o Rpi, o módulo emissor de frequência de rádio (Rf)e o sensor de umidade do solo, os dois últimos ficam acoplados ao primeiro da seguinte forma:

![Alt Text](https://raw.githubusercontent.com/T635/Irrigacao/master/Imagens/Circuito%20raspberry.png)

Na segunda parte foram usados o Arduino e nele acoplados o módulo de relé, módulo receptor de frequência de rádio(Rf), o relé termico, o contator e o motor da irrigação da seguinte forma:

![Alt Text](https://raw.githubusercontent.com/T635/Irrigacao/master/Imagens/arduino.png)
Feita a montagem, irei a parte da programação.
## Programação
Para que a irrigação fosse ligada quando a umidade do solo chegasse a um nível, foi necessário que o Rpi a aferisse de tempos em tempos, assim quando ela estivesse em baixo nível ele enviaria um sinal, pelo módulo de Rf, o Arduino detectando este sinal ligaria um módulo relé acionando o motor responsável por bombear a água para os aspersores.

O módulo Rf, foi desenvolvido para uma interação Arduino-Arduino, entretanto, devido a seu custo benefício, ele foi usado em uma interação Rpi-Arduino.
