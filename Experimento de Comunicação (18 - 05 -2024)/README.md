No dia 18 de Maio de 2024, Sábado, foi realizado um experimento de comunicação entre três pontos de importância no CSELA, a Administração, a Cisterna e uma das caixas d'água. 
O objetivo do experimento era confirmar a viabilidade de comunicação sem fio, LoRa, entre estes três pontos. 
O dia estava chuvoso e o bairro estava sem energia elétrica, motivo pelo qual não foi possível salvar um log das mensagens trocadas. 
Foram utilizados dois esps32 LoRa TTGO para o experimento, um com o papel de enviar as mensagens (sender) e o outro com o papel de captar as mensagens (receiver). O receiver estava munido de um led, que acendia ao receber uma mensagem, o que possibilitou confirmar
que havia comunicação entre os dois dispositivos. Para o experimento foram utilizadas duas antenas Stellbras AP3900 7 dBi. <br />
![Imagem do Sender](https://github.com/gabrielToledanoF/Experimentos-IoTS---CSELA/blob/main/Experimento%20de%20Comunica%C3%A7%C3%A3o%20(18%20-%2005%20-2024)/Imagens/esp32-lora-ttgo-sender.jpg?raw=true)
![Imagem do Receiver](https://github.com/gabrielToledanoF/Experimentos-IoTS---CSELA/blob/main/Experimento%20de%20Comunica%C3%A7%C3%A3o%20(18%20-%2005%20-2024)/Imagens/esp32-lora-ttgo-receiver.jpg?raw=true)
![Imagem das Antenas](https://github.com/gabrielToledanoF/Experimentos-IoTS---CSELA/blob/main/Experimento%20de%20Comunica%C3%A7%C3%A3o%20(18%20-%2005%20-2024)/Imagens/antenas-stellbras-3900-7dbi.jpg?raw=true)
Na realização do experimento, o sender foi fixado na admnistração, com sua antena presa a uma janela, enquanto o receiver foi movido lentamente dentro de um carro, no trajeto visto abaixo, em verde. Durante todo o percurso houve comunicação.<br />
![Area do Experimento](https://github.com/gabrielToledanoF/Experimentos-IoTS---CSELA/blob/main/Experimento%20de%20Comunica%C3%A7%C3%A3o%20(18%20-%2005%20-2024)/Imagens/area-experimento.png?raw=true)
Pontos interessantes do experimento:<br />
  -Comunicação LoRa foi configura com Spreading Factor 12 e Coding Rate 8.<br />
  -Apesar de não marcado no trajeto, foi realizado teste de comunicação com o sender dentro da cisterna. A comunicação ocorreu sem problemas.<br />
  -Pouco antes de chegar na caixa d'água o sender parou de receber mensagens por alguns instantes, voltando a receber depois. Não há confirmação se foi devido a interferência climática, antrópica ou urbana (alguma construção). Quando voltou a haver comunicação o sender (dentro do carro) já estava na frente da caixa d'água. <br />
  -Não foi realizado um deste dentro do terreno/construção da caixa d'água, apenas de frente para ela. <br />
  -Ao seguir com o carro para fazer o retorno, um pouco adiante da caixa d'água, parou de ter comunicação, o que pode indicar um possível limite do alcance. <br />
  -O experimento não foi realizado em condições ideias, devido a chuva, falta de visibilidade do log das mensagens, falta de estrutura para instalar as antenas. <br />
