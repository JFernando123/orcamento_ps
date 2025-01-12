# Vaga Interna - Tester na Ponto.Sys

Estamos abrindo uma oportunidade interna para a posição de **Tester** aqui na Ponto.Sys! Essa vaga é destinada exclusivamente aos nossos colaboradores que desejam explorar e contribuir com a área de qualidade de software na empresa. 🚀

## Sobre a Vaga

Como Tester, você terá um papel fundamental em garantir que nossos produtos atendam aos mais altos padrões de qualidade. Para participar da seleção, será realizada uma **avaliação técnica prática**, descrita abaixo.

## Desafio Técnico

Você deverá criar um cenário de teste automatizado que simula o seguinte fluxo no site do Virtual Store Web:

1. **Acessar o Virtual Store Web:** [https://virtualstore.pontosys.com:4433](https://virtualstore.pontosys.com:4433).
2. **Realizar a configuração inicial:**
   - CNPJ: **11.111.111/1111-11**
   - Filial: **3**
   - Transação padrão: **Orçamento**
   - Transações permitidas: **Apenas orçamento**
   - Dados supervisor: **Usuário: 15 e Senha: 2**
3. **Realizar o login no sistema:** (Caso esteja dando conflito de login, pois outras pessoas podem estar utilizando o mesmo acesso, basta criar um usuário manualmente pelo sistema e utilizá-lo na automação)
   - Usuário: **elvis@pontosys.com**
   - Senha: **Elv@135790**
4. **Abrir o menu Venda:**
   - Validar se o tipo de transação é "Orçamento".
   - Adicionar o produto "SALMÃO" no orçamento e clicar em "Finalizar venda".
   - Informar o Vendedor "NENHUM".
   - Manter o Cliente "Consumidor".
   - Clicar em continuar para finalizar o orçamento.
   - Aguardar impressão do cupom na tela, e depois fechar pela seta <- localizada no header da aplicação.
   - Aguardar voltar para a tela inicial do Orçamento e aguardar limpar todos os dados da tela para finalizar o teste.
5. **Observação:** Utilizar asserts, para definir se o teste passou ou falhou.

### Requisitos da Entrega

- **Automação:** Utilizar Python
- **Código Fonte:** Suba o código no GitHub e compartilhe o link para avaliação.
- **Prazo de Entrega:** 17/01/2025.
- **Envio do Projeto:** Enviar o link do repositório GitHub para **Elvis**.

## O que Será Avaliado?

- **Capacidade Técnica:** Uso adequado de ferramentas e práticas de automação.
- **Cobertura de Cenário:** Garantir que todos os passos do fluxo sejam contemplados.
- **Organização do Código:** Boa estruturação e clareza no código.
- **Documentação:** Caso necessário, inclua um README no repositório explicando como executar o teste.

Boa sorte a todos os candidatos! 🍀

---
Ponto.Sys 🚀
