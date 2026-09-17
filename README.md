# positional-bias-eval

Analisar a presença de viés posicional, usando a prova da OAB como base.

## Contexto

Esse experimento é importante porque esse tipo de viés, que prejudica o desempenho do modelo e usuarios, tem muito pouca documentação e estudo para quando é usado o PT-BR. Ou seja, não sabemos direito quanto usuarios brasileiros sofrem com isso e se é necessario que isso receba uma atenção maior para solucionar isso.

## Desenho experimental
O experimento foi feito com um primeiro teste de respostas com as posições originais da prova (aproximadamente 25% de cada alternativa), depois uma com todas as respostas em A, depois em B, depois em C, e por ultimo em  D. Dessa forma temos o primeiro teste como um grupo controle e os outros com casos especificos, com  a comparação entre eles no mostrando a presença ou não de um viés.

## Dados
eduagarcia/oab_exams, 2.210 questões, 2010–2018 (disponivel no hugging face)

## Limitações 

- gabaritos de 2010 a 2018; mudança legislativa posterior torna parte deles desatualizada
- provas públicas desde 2010, então contaminação de treino é provável
- respostas fora do formato ANSWER: X não são pontuáveis; essa taxa é reportada como métrica, não descartada

## Status

Trabalho em andamento.

## Como rodar

Instale as dependências:

```
pip install inspect-ai openai datasets
```

Configure a chave da API do seu provedor em um arquivo `.env` na raiz do projeto. Exemplo com OpenRouter:

```
OPENROUTER_API_KEY=sua_chave_aqui
```

Condição de controle, com as alternativas na ordem original da prova:

```
inspect eval oab.py@oab_r --model PROVEDOR/MODELO
```

Condições com a alternativa correta em posição fixa. O parâmetro `posicao` vai de 0 a 3 e corresponde às letras A, B, C e D:

```
inspect eval oab.py@oab_fixedchoice --model PROVEDOR/MODELO -T posicao=2
```

Substitua `PROVEDOR/MODELO` pelo modelo que você quer avaliar. O Inspect aceita vários provedores, e a lista de identificadores está na documentação oficial: https://inspect.aisi.org.uk

Durante o desenvolvimento, use `--limit N` para rodar apenas as N primeiras questões e economizar tokens:

```
inspect eval oab.py@oab_fixedchoice --model PROVEDOR/MODELO -T posicao=2 --limit 20
```

Para visualizar os logs de uma rodada:

```
inspect view
```
