# Resumo Detalhado da Dissertação

> Nota de fidelidade: a dissertação apresenta algumas divergências internas. O resumo e o abstract tratam o modelo-base como "U-Net", enquanto o Capítulo 4 detalha a comparação entre `U-Net multitarefa` e `U-Net Fuzzy`. Há também inconsistências na cardinalidade do conjunto de dados e em parte dos consolidados de EGL e EGG entre resumo, texto corrido e tabelas. Nas sínteses quantitativas abaixo, priorizo as Tabelas 4.3, 4.4 e 4.5, por serem os quadros consolidados mais detalhados, e aponto as divergências quando necessário.

## 1. Informações Gerais

| Item | Informação |
|---|---|
| Título | Comparação entre Modelos de Redes Neurais U-Net e U-Net Fuzzy para Mensurar Regiões de Imagens de Ultrassonografia Bovina |
| Autor | Victor Patrick Sena Barbosa Lima |
| Instituição | Universidade Federal de Uberlândia |
| Unidade | Faculdade de Matemática |
| Programa | Programa de Pós-Graduação em Matemática |
| Área de pesquisa | Matemática |
| Linha de pesquisa | Matemática Aplicada |
| Ano | 2026 |
| Orientadora | Profa. Dra. Rosana Sueli da Motta Jafelice |
| Coorientador | Prof. Dr. Caio Augusto Rodrigues dos Santos |

## 2. Contexto e Motivação

A dissertação parte da relevância econômica da pecuária bovina para o Brasil e do papel estratégico da avaliação de carcaça na cadeia produtiva da carne. O trabalho destaca que a ultrassonografia de carcaça permite mensurar, in vivo, indicadores fenotípicos importantes, especialmente a Área de Olho de Lombo (AOL), a Espessura de Gordura subcutânea no Lombo (EGL) e a Espessura de Gordura subcutânea na Garupa (EGG).

O problema central é que a delimitação dessas regiões em imagens de ultrassom ainda depende, em grande medida, da atuação manual de especialistas. Esse processo é descrito como subjetivo, demorado e sensível à experiência do avaliador, o que limita padronização, escalabilidade e rapidez.

A motivação científica decorre de dois fatores principais. O primeiro é a oportunidade de automatizar a segmentação e a mensuração de estruturas anatômicas relevantes usando visão computacional e aprendizado profundo. O segundo é a incerteza intrínseca das imagens ultrassonográficas, nas quais contornos nem sempre são nítidos, o que torna atraente a incorporação de lógica fuzzy.

A lacuna de pesquisa explicitada pelo autor é clara: até onde foi possível verificar na literatura, não havia trabalhos que combinassem segmentação de imagens de ultrassom bovino com uma arquitetura `U-Net Fuzzy` integrada a `ANFIS` para mensurar simultaneamente AOL, EGL e EGG. O texto afirma também que os trabalhos localizados abordavam principalmente a AOL e comparavam U-Net com outras arquiteturas, mas não com uma variante fuzzy do tipo proposta.

## 3. Objetivos

### Objetivo Geral

Desenvolver e comparar dois modelos para delimitação automática e mensuração dos indicadores AOL, EGL e EGG em imagens de ultrassom de bovinos das raças Nelore e Caracu, avaliando uma arquitetura `U-Net multitarefa` e uma arquitetura `U-Net Fuzzy` integrada ao `ANFIS`.

### Objetivos Específicos

- Compreender os conceitos fundamentais de redes neurais, teoria dos conjuntos fuzzy, sistemas baseados em regras fuzzy e a integração entre U-Net e ANFIS.
- Padronizar o banco de dados das imagens de ultrassom e desenvolver as respectivas máscaras de segmentação.
- Aplicar técnicas de pré-processamento e aumento de dados para adequar o conjunto ao treinamento.
- Desenvolver e treinar os modelos com Python 3.11.15, TensorFlow 2.21.0 e Keras 3.13.2.
- Produzir um aplicativo computacional em Tkinter para automatizar a segmentação e a mensuração de AOL, EGL e EGG.

## 4. Fundamentação Teórica

### Conceitos centrais

| Tema | Síntese |
|---|---|
| Redes neurais artificiais | A dissertação percorre neurônio biológico e artificial, perceptron, backpropagation, gradiente descendente estocástico, regularização, overfitting, momentum, Adam e vanishing gradient. |
| Redes neurais convolucionais | São introduzidas como base para análise de imagens, com discussão de convolução, padding, stride, pooling e convolução transposta. |
| U-Net | É apresentada como arquitetura encoder-decoder com skip connections, originalmente proposta para segmentação biomédica. Sua principal força, no contexto do trabalho, é segmentar pixel a pixel com bom desempenho mesmo em bases pequenas. |
| Conjuntos fuzzy | São usados para modelar incerteza e imprecisão, aspecto relevante em imagens de ultrassom. |
| SBRF e inferência fuzzy | O texto revisa regras fuzzy e os esquemas de inferência, com destaque para Takagi-Sugeno. |
| ANFIS | É descrito como sistema neuro-fuzzy adaptativo de cinco camadas, combinando aprendizado de redes neurais e representação fuzzy. |
| U-Net multitarefa | Recebe a informação da raça do animal via codificação one-hot e modula o bottleneck por uma camada densa seguida de multiplicação dos mapas de características. |
| U-Net Fuzzy | Mantém a base multitarefa e adiciona um módulo de inferência fuzzy no bottleneck para refinar os mapas de características antes do decoder. |

### Arquiteturas e técnicas utilizadas

A arquitetura-base dos experimentos preserva a lógica da U-Net, com encoder, bottleneck e decoder. No encoder, o modelo usa blocos com `Conv2D`, `ReLU` e `MaxPooling`. No decoder, utiliza `Conv2DTranspose`, concatenação com skip connections e novas convoluções, finalizando com uma camada `1 x 1` com ativação sigmoide para gerar a máscara de segmentação.

A `U-Net multitarefa` incorpora a raça do animal no baseline. Em termos práticos, a rede não aprende apenas a segmentação, mas condiciona a representação interna ao contexto categórico do animal.

A `U-Net Fuzzy` adiciona ao baseline um módulo inspirado em `ANFIS`, com pré-processamento das entradas, fuzzificação por funções de pertinência gaussianas, ativação de regras fuzzy e defuzzificação baseada em Takagi-Sugeno. A saída fuzzy é somada ao mapa multitarefa, controlada por um hiperparâmetro de influência:

$$
Y = Y_m + \alpha Y_f
$$

em que $Y_m$ é o mapa de características da camada multitarefa e $Y_f$ é a saída do módulo fuzzy.

### Métricas matemáticas relevantes

A dissertação formaliza as principais métricas de avaliação:

$$
Dice = \frac{2|A \cap B|}{|A| + |B|}
$$

$$
Acurácia = \frac{VP + VN}{VP + VN + FP + FN}
$$

$$
MAE = \frac{1}{n}\sum_{i=1}^{n} |y_i - \hat{y}_i|
$$

$$
R^2 = 1 - \frac{\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}{\sum_{i=1}^{n}(y_i - \bar{y})^2}
$$

Essas métricas avaliam duas dimensões distintas do problema: a qualidade da segmentação e a precisão numérica das medidas extraídas das máscaras.

### Trabalhos relacionados destacados

| Referência | Papel no trabalho |
|---|---|
| Ronneberger, Fischer e Brox (2015) | Base conceitual da U-Net original para segmentação biomédica. |
| Jang (1993) | Base teórica do ANFIS. |
| Melo et al. (2022) | Principal referência aplicada ao contexto bovino, focada em segmentação automática da AOL com `UNet++`. |
| Kirichev, Slavov e Momcheva (2021) | Exemplo de integração entre U-Net e lógica fuzzy em segmentação de imagens. |
| Purwono et al. (2025) | Referência contemporânea de U-Net com componentes fuzzy para segmentação em outro domínio biomédico. |

## 5. Metodologia

| Aspecto | Descrição |
|---|---|
| Tipo de pesquisa | Não informado explicitamente na dissertação. O desenho descrito é de desenvolvimento computacional com comparação experimental de modelos de segmentação. |
| Problema | Segmentação e mensuração automáticas de AOL, EGL e EGG em imagens de ultrassom bovino. |
| Base de dados | Imagens fornecidas pelo Centro Avançado de Pesquisa e Desenvolvimento de Bovinos de Corte, Instituto de Zootecnia, SAA-SA, Sertãozinho-SP. |
| Animais | Machos com cerca de 12 meses, das raças Nelore e Caracu. |
| Equipamento de aquisição | Aparelho de ultrassom Aloka SSD-500, com sonda linear de 3,5 MHz. |
| Quantidade de dados | Há inconsistência no texto. O resumo informa 135 imagens; a Seção 4.1.2 menciona 134 imagens e, ao mesmo tempo, informa 108 Nelore + 27 Caracu, soma que resulta em 135. A dissertação não resolve explicitamente essa divergência. |
| Medidas de referência | AOL, EGL e EGG, disponibilizadas em arquivo Excel e associadas às delimitações feitas por especialista. |
| Critérios de seleção | Imagens com identificação do animal, associação à raça e disponibilidade de delimitação/manual e medida numérica correspondente. |
| Ground truth | Criado com `Label Studio` a partir das demarcações da especialista. Para EGG, foram necessárias duas segmentações: gordura e músculo `Biceps Femoris`. |
| Pré-processamento | Recorte para remoção de informações irrelevantes, normalização para o intervalo `[0,1]` e redimensionamento para `256 x 256`. |
| Aumento de dados | Rotação aleatória em `[-15^\circ, 15^\circ]` e variações de brilho. O texto afirma que cada imagem foi modificada três vezes. |
| Divisão dos dados | `70%` treinamento, `20%` validação e `10%` teste. |
| Ferramentas computacionais | Python 3.11.15, TensorFlow 2.21.0 com GPU, Keras 3.13.2, Label Studio, ImageJ, Tkinter e Visual Studio Code. |
| Modelos | `U-Net multitarefa` e `U-Net Fuzzy`. Para AOL e EGL, um modelo por arquitetura. Para EGG, dois modelos por arquitetura, um para gordura e outro para `Biceps Femoris`. Total: 8 modelos. |
| Estratégia de treinamento | Otimizador Adam, taxa de aprendizado 0,001, batch size 4, até 100 épocas, `Binary Cross-Entropy`, `Dropout = 0,2`, `EarlyStopping` com 15 épocas de paciência monitorando Dice na validação. |
| Estratégia de repetição | Cada modelo foi treinado 4 vezes, e os resultados reportados são médias dessas execuções. |
| Configuração fuzzy | 3 conjuntos fuzzy e 9 regras fuzzy. |
| Ambiente computacional | Notebook Asus TUF Gaming F15, Intel Core i7-12700H, 8 GB RAM, SSD 512 GB, GPU NVIDIA GeForce RTX 3050 Mobile 4 GB, Linux Mint 22.3. |

## 6. Desenvolvimento da Pesquisa

1. O problema foi formulado como segmentação de imagens ultrassonográficas de regiões anatômicas bovinas, com posterior extração numérica de indicadores de carcaça.
2. As imagens originais foram delimitadas manualmente por especialista, com apoio do `ImageJ`, gerando a referência anatômica e os valores numéricos reais.
3. O autor construiu máscaras de segmentação para cada indicador. Para a EGG, foram produzidas duas máscaras distintas, uma para a gordura e outra para o músculo `Biceps Femoris`.
4. As imagens foram recortadas, normalizadas e redimensionadas, e em seguida ampliadas por técnicas de data augmentation.
5. A raça do animal foi incorporada ao pipeline por codificação `one-hot`, explorada diretamente na camada multitarefa.
6. Foram treinadas duas famílias de modelos. A primeira foi a `U-Net multitarefa`, que usa a raça no baseline. A segunda foi a `U-Net Fuzzy`, que usa a mesma base multitarefa e acrescenta inferência fuzzy.
7. Para AOL, a medida final foi obtida por contagem de pixels segmentados convertida para área. Para EGL, a espessura foi obtida da camada de gordura em posição específica. Para EGG, a medida depende da segmentação conjunta da gordura e do início do `Biceps Femoris`.
8. O desempenho foi analisado por curvas de custo, Dice, acurácia, MAE, reta de regressão linear e $R^2$, além de comparação visual das máscaras.
9. O trabalho foi concluído com o desenvolvimento de um aplicativo gráfico para uso prático dos modelos e exportação dos resultados em Excel.

## 7. Resultados

### Síntese comparativa

| Indicador | Melhor segmentação | Melhor medida numérica | Leitura geral |
|---|---|---|---|
| AOL | U-Net Fuzzy | U-Net Fuzzy | Ganho claro da inferência fuzzy. |
| EGL | U-Net multitarefa em Dice e acurácia; U-Net Fuzzy em MAE e $R^2$ | Sem vencedor absoluto | Tarefa difícil e fortemente desbalanceada. |
| EGG | U-Net Fuzzy com leve vantagem em Dice | U-Net multitarefa | A medida final é sensível à propagação de erros de duas segmentações. |

### AOL

A AOL foi o indicador em que a arquitetura fuzzy apresentou o ganho mais consistente. O modelo `U-Net Fuzzy` superou o `U-Net multitarefa` nas principais métricas de segmentação e nas métricas de mensuração numérica, embora tenha exigido mais épocas e mostrado curvas de treinamento mais oscilatórias.

| Modelo | Dice | Acurácia | Épocas | $R^2$ | MAE | Erro Máximo | Erro Mínimo | Média Predita | Média Real |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| U-Net multitarefa | 92,73% | 94,75% | 80 | 0,5578 | 2,988 cm² | 7,905 cm² | 0,005 cm² | 39,880 cm² | 40,559 cm² |
| U-Net Fuzzy | 93,29% | 95,15% | 89 | 0,7423 | 2,312 cm² | 6,644 cm² | 0,225 cm² | 39,865 cm² | 40,559 cm² |

Principais figuras mencionadas:
- Figura 4.8: regressão linear, custo, Dice e acurácia da U-Net multitarefa.
- Figura 4.9: regressão linear, custo, Dice e acurácia da U-Net Fuzzy.
- Figura 4.10: comparação visual entre ground truth e máscaras geradas.

Interpretação principal: a inferência fuzzy parece ter refinado a representação do baseline e melhorado a reconstrução da região da AOL, o que é reforçado pela análise de mapas de características em 4.17 a 4.20.

### EGL

A EGL foi a tarefa mais sensível ao desbalanceamento entre região de interesse e fundo. A dissertação observa explicitamente que a acurácia pode ser enganosa nesse cenário, porque a maior parte da imagem pertence ao fundo.

| Modelo | Dice | Acurácia | Épocas | $R^2$ | MAE | Erro Máximo | Erro Mínimo | Média Predita | Média Real |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| U-Net multitarefa | 70,25% | 99,85% | 88 | 0,6899 | 0,018 mm | 0,48 mm | 0,01 mm | 0,134 mm | 0,134 mm |
| U-Net Fuzzy | 69,39% | 99,50% | 94 | 0,7031 | 0,015 mm | 0,54 mm | 0,01 mm | 0,134 mm | 0,134 mm |

Observação importante: o texto corrido da subseção 4.3.2 informa, para a U-Net multitarefa, Dice médio de `60,78%` e acurácia de `99,99%`, mas a Tabela 4.4 consolida `70,25%` e `99,85%`. O resumo/abstract também enfatiza `70,25%`. O quadro acima segue a Tabela 4.4.

Principais figuras mencionadas:
- Figura 4.11: regressão e curvas de treinamento da U-Net multitarefa.
- Figura 4.12: regressão e curvas de treinamento da U-Net Fuzzy.
- Figura 4.13: comparação visual das máscaras.

Interpretação principal: não houve superioridade inequívoca de um modelo. A U-Net multitarefa foi ligeiramente melhor na segmentação consolidada, enquanto a U-Net Fuzzy teve leve vantagem em MAE e $R^2$.

### EGG

A EGG foi a tarefa metodologicamente mais complexa, porque depende de duas segmentações: uma da gordura e outra do músculo `Biceps Femoris`. Assim, pequenos erros em qualquer uma das duas etapas podem contaminar a medida final.

| Modelo | Dice `Biceps` | Dice gordura | Acurácia `Biceps` | Acurácia gordura | Épocas `Biceps` | Épocas gordura | $R^2$ | MAE | Erro Máximo | Erro Mínimo | Média Predita | Média Real |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| U-Net multitarefa | 82,74% | 79,84% | 98,75% | 96,87% | 31 | 61 | 0,4287 | 0,7 mm | 2,5 mm | 0,00 mm | 4,915 mm | 4,781 mm |
| U-Net Fuzzy | 84,60% | 79,99% | 98,60% | 96,88% | 45 | 76 | 0,3178 | 0,8 mm | 2,1 mm | 0,00 mm | 4,974 mm | 4,781 mm |

Principais figuras mencionadas:
- Figura 4.14: regressão linear da EGG com U-Net multitarefa.
- Figura 4.15: regressão linear da EGG com U-Net Fuzzy.
- Figura 4.16: comparação visual das segmentações para EGG.

Interpretação principal: a U-Net Fuzzy teve leve vantagem em Dice nas segmentações isoladas, mas a U-Net multitarefa foi melhor na medida final da EGG, com menor MAE e maior $R^2$.

### Comparação com trabalhos relacionados

A dissertação usa `Melo et al. (2022)` como referência aplicada para segmentação automática em ultrassonografia bovina, especialmente na AOL. No entanto, o texto não apresenta uma tabela quantitativa de comparação direta entre os resultados obtidos aqui e os valores desse trabalho. A contribuição comparativa do autor é mais de escopo e arquitetura: ampliar o problema para AOL, EGL e EGG e introduzir uma variante fuzzy integrada ao ANFIS.

## 8. Discussão

Os resultados sugerem que a inferência fuzzy foi mais útil quando a estrutura segmentada tinha contornos mais amplos e informação anatômica mais consistente, caso da AOL. A análise de mapas de características apresentada no Capítulo 4 indica que a U-Net Fuzzy produz representações mais discriminativas no decoder para esse indicador.

Na EGL, o problema é mais delicado. A região de interesse é fina, estreita e pouco contrastada, o que torna o coeficiente de Dice mais sensível e a acurácia menos confiável. Isso explica por que o trabalho insiste que valores muito altos de acurácia não significam, necessariamente, boa segmentação.

Na EGG, a dificuldade decorre menos da segmentação individual de uma estrutura e mais da composição geométrica entre duas estruturas. A medida depende da localização exata do início do `Biceps Femoris` e da espessura da gordura naquela coluna. Por isso, pequenas imprecisões acumuladas se propagam para a medida final.

Entre os pontos fortes da abordagem estão a integração entre aprendizado profundo e lógica fuzzy, o uso explícito da raça do animal como informação contextual, a análise visual das máscaras e mapas de características e a entrega de um aplicativo computacional funcional.

As principais limitações apontadas pelo autor são a qualidade heterogênea das imagens, a quantidade reduzida de dados, a escassez de literatura sobre U-Net Fuzzy aplicada ao problema e a dependência do formato do aparelho de ultrassom. O próprio texto reconhece que artefatos, ruídos e variações de aquisição podem comprometer a segmentação.

Também é relevante observar que o resumo/abstract tende a simplificar excessivamente os achados, sobretudo em EGL e EGG. O corpo do Capítulo 4 mostra um quadro mais nuançado: não houve superioridade uniforme da U-Net Fuzzy em todos os indicadores e em todas as métricas.

## 9. Conclusões

A dissertação conclui, na prática, que os objetivos centrais foram alcançados: os modelos foram desenvolvidos, treinados, comparados e incorporados em uma ferramenta computacional utilizável. O estudo mostra que a combinação entre segmentação profunda e inferência fuzzy é promissora, mas seu benefício depende fortemente do tipo de estrutura anatômica e da forma como a medida final é calculada.

O principal achado é que a `U-Net Fuzzy` foi claramente superior para a AOL e ligeiramente melhor em parte da segmentação da EGG, mas não dominou todas as tarefas. Para a EGG, a `U-Net multitarefa` foi mais precisa na medida numérica final. Para a EGL, os resultados ficaram equilibrados, sem vencedor absoluto.

Uma contribuição adicional relevante é a demonstração de viabilidade prática. O autor destaca que as redes são relativamente compactas, com a maior delas tendo 2.741.281 parâmetros, o que favorece eficiência computacional e futuras adaptações para ambientes com menos recursos.

## 10. Trabalhos Futuros

### Sugestões explícitas do autor

- Estudar e implementar modelos que combinem `U-Net` com mecanismos de atenção.
- Aplicar técnicas de `transfer learning` e `fine tuning` para melhorar o desempenho em cenários com poucos dados.

### Extensões coerentes com a discussão do texto

- Desenvolver técnicas para remover ou reduzir informações específicas do aparelho de ultrassom, aumentando a capacidade de generalização.
- Ampliar e padronizar a base com protocolo mais rigoroso de aquisição de imagens.
- Explorar adaptação do aplicativo para dispositivos móveis, aproveitando o porte relativamente compacto das redes.

## 11. Principais Contribuições

- Proposição e comparação de duas arquiteturas para ultrassonografia bovina: `U-Net multitarefa` e `U-Net Fuzzy`.
- Expansão do problema além da AOL, incluindo também EGL e EGG.
- Integração da informação de raça do animal ao processo de segmentação.
- Incorporação de um módulo de inferência fuzzy baseado em `ANFIS` no bottleneck da U-Net.
- Construção de `ground truths` específicos para diferentes estruturas anatômicas, inclusive com duas máscaras para a EGG.
- Avaliação experimental com múltiplas métricas de segmentação e mensuração numérica.
- Análise qualitativa de máscaras e mapas de características internos das redes.
- Desenvolvimento de um aplicativo em `Tkinter` para uso prático, com visualização dos resultados e exportação em Excel.
- Demonstração de que o ganho da inferência fuzzy não é uniforme e depende da natureza geométrica e anatômica do indicador.
- Identificação explícita de limitações de aquisição, base de dados e generalização entre equipamentos.

## 12. Resumo Executivo

A dissertação investiga um problema concreto da pecuária bovina: como medir, com mais rapidez e menos subjetividade, indicadores anatômicos relevantes em imagens de ultrassom de carcaça. Esses indicadores são a Área de Olho de Lombo, a espessura de gordura no lombo e a espessura de gordura na garupa. Eles têm impacto direto na avaliação zootécnica, na seleção animal e, em última instância, em decisões econômicas do setor.

O ponto de partida do autor é simples e forte: hoje, boa parte desse trabalho ainda depende da interpretação manual de especialistas. Isso torna o processo mais lento, menos padronizado e mais sujeito a variações entre avaliadores. A proposta da dissertação é usar inteligência artificial para automatizar essa etapa.

Para isso, o autor compara duas arquiteturas. A primeira é uma `U-Net multitarefa`, que faz segmentação de imagem e incorpora a raça do animal como informação contextual. A segunda é uma `U-Net Fuzzy`, que usa a mesma base, mas acrescenta um módulo de inferência fuzzy inspirado no `ANFIS`.

A escolha faz sentido porque imagens de ultrassom são naturalmente ruidosas e imprecisas. Em muitos casos, o contorno anatômico não aparece de forma nítida. A lógica fuzzy entra justamente para lidar com esse tipo de incerteza, tentando refinar a representação aprendida pela rede neural.

O conjunto de dados veio de imagens reais de bovinos Nelore e Caracu obtidas no Centro Avançado de Pesquisa e Desenvolvimento de Bovinos de Corte, em Sertãozinho. As imagens foram pré-processadas, receberam máscaras de segmentação construídas a partir das marcações da especialista e foram ampliadas por técnicas de aumento de dados, como rotação e alteração de brilho. O treinamento foi feito em Python, com TensorFlow e Keras, usando GPU.

A avaliação foi feita em duas frentes. Primeiro, o trabalho mede a qualidade da segmentação por métricas como `Dice` e `acurácia`. Segundo, avalia se as medidas numéricas extraídas das máscaras realmente se aproximam das medidas feitas pela especialista, usando `MAE` e `R²`.

O melhor resultado do trabalho aparece na AOL. Nesse indicador, a `U-Net Fuzzy` teve desempenho superior ao da `U-Net multitarefa`, com Dice mais alto, acurácia maior, menor erro absoluto médio e melhor coeficiente de determinação. Em termos práticos, isso significa que a versão fuzzy conseguiu tanto segmentar melhor quanto medir melhor a área de interesse.

Na EGL, o cenário foi mais equilibrado. A tarefa é difícil porque a camada de gordura é estreita e ocupa poucos pixels, o que torna a segmentação sensível e o desbalanceamento muito forte. Nesse caso, um modelo foi um pouco melhor em Dice e acurácia, enquanto o outro foi ligeiramente melhor em erro médio e em associação linear com a medida real.

Na EGG, o problema ficou ainda mais delicado porque a medida final depende de duas segmentações: gordura e músculo `Biceps Femoris`. A `U-Net Fuzzy` teve leve vantagem na segmentação isolada, mas isso não se converteu em melhor medida final. Para a EGG, a `U-Net multitarefa` acabou entregando o melhor resultado numérico.

Um resultado importante da dissertação é mostrar que inserir lógica fuzzy em uma rede profunda não garante ganho universal. Em algumas situações, como na AOL, a integração trouxe benefício claro. Em outras, como na EGL e na EGG, o comportamento foi mais dependente da geometria da estrutura, do desbalanceamento dos pixels e da sensibilidade do cálculo final.

Além dos modelos, o autor desenvolveu um aplicativo computacional com interface gráfica. Esse aplicativo permite escolher o indicador, selecionar o modelo, carregar imagens, visualizar as máscaras segmentadas sobrepostas e exportar os resultados para Excel. Isso dá ao trabalho um valor aplicado imediato, aproximando a pesquisa de uma ferramenta real de uso técnico.

A dissertação também é honesta quanto às limitações. O autor reconhece que a qualidade das imagens é um gargalo importante, que a base é pequena para aprendizado profundo e que o desempenho pode depender do aparelho de ultrassom usado. Também admite que havia pouca literatura disponível sobre U-Net Fuzzy, o que aumentou a dificuldade de implementação.

Como encaminhamento futuro, o trabalho sugere testar mecanismos de atenção e transferência de aprendizado. Essas duas linhas são coerentes com o problema: a primeira pode ajudar a destacar regiões mais relevantes da imagem, e a segunda pode melhorar o aproveitamento de bases pequenas. Em síntese, a dissertação entrega uma contribuição metodológica original, tecnicamente consistente e com potencial de aplicação prática na avaliação ultrassonográfica bovina.