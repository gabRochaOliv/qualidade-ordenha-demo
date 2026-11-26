# Qualidade de software — revisão de código com IA

Projeto fictício para a Avaliação III de Engenharia de Software. A investigação verifica se o CodeRabbit identifica alterações de código que tornam incorreto o total diário de produção de leite.

## Regra de negócio

O total diário de uma propriedade é a soma dos litros das suas ordenhas com status `confirmada`. Ordenhas `cancelada` e registros de outras propriedades ficam fora do cálculo.

No exemplo, a propriedade 1 tem 80 L confirmados e 20 L cancelados. A propriedade 2 tem 35 L confirmados. O resultado correto para a propriedade 1 é **80 L**.

## Executar

É necessário ter Python 3 instalado. Na pasta do projeto, execute:

```powershell
python exemplo.py
```

## Experimento com o CodeRabbit

1. Publique esta versão correta em um repositório público próprio no GitHub.
2. Conecte o CodeRabbit selecionando somente esse repositório.
3. Um integrante cria uma branch e abre um pull request com a mudança do cenário A. Registre a resposta da ferramenta antes de corrigir o código.
4. Repita o processo com uma branch nova para cada cenário. Não misture as mudanças em um único pull request.
5. Para cada PR, guardem o link, a captura da alteração, os comentários da IA e a conferência humana do resultado.

### Cenários propostos

- **A — Status ignorado.** Retirar da função o filtro `ordenha["status"] == "confirmada"`. O código passará a devolver 100 L para a propriedade 1. Verificar se a IA identifica a inclusão da ordenha cancelada.
- **B — Propriedade ignorada.** Em uma branch criada a partir da versão correta, retirar o filtro `ordenha["propriedade_id"] == propriedade_id`. O código passará a devolver 115 L para a propriedade 1. Verificar se a IA identifica a mistura de propriedades.
- **C — Mudança correta.** Em outra branch criada a partir da versão correta, alterar somente o texto da docstring da função para esclarecer a regra. O resultado continuará 80 L. Verificar se a IA apresenta algum alerta incorreto.

Em repositórios públicos novos com menos de 10 estrelas, o CodeRabbit exige o acionamento manual da revisão no PR. Use o botão **Trigger review** no comentário de status ou comente `@coderabbitai review`.

## Registro dos resultados

| PR | Resultado esperado | Resultado após a mudança | O CodeRabbit identificou o problema? | Conferência humana |
| --- | ---: | ---: | --- | --- |
| A | 80 L | 100 L | A preencher | A preencher |
| B | 80 L | 115 L | A preencher | A preencher |
| C | 80 L | 80 L | A preencher | A preencher |

A equipe deve registrar os resultados realmente observados. Os cenários acima são hipóteses para o experimento.

## Fontes da ferramenta

- [Guia de instalação do CodeRabbit](https://docs.coderabbit.ai/guide/repository)
- [Revisão de pull requests](https://docs.coderabbit.ai/overview/pull-request-review)
- [Planos e limites de revisão](https://docs.coderabbit.ai/management/plans)
