# Guia para ChatGPT — Research Assistant Pipeline 0.1.0-pilot

[English](CHATGPT_GUIDE_EN.md) · [Guia para Claude](PILOT_GUIDE_PT.md)

Use este guia para começar uma pesquisa no ChatGPT, com ou sem uma ideia definida.
O método é o mesmo distribuído para Claude: 12 fases, protocolos personalizados,
fontes rastreáveis e decisões científicas humanas. Você mantém a autoria do seu trabalho.

## 1. Baixar os arquivos

Abra um dos links e use o botão **Download raw / Baixar arquivo** do GitHub,
geralmente representado por uma seta para baixo. Se aparecer apenas o texto,
salve o arquivo completo, preservando a extensão.

| Arquivo | Quando usar |
|---|---|
| [Pacote completo ZIP](dist/research-assistant-pipeline-0.1.0-pilot.zip) | Importação em ambientes com Skills; scripts Python e modelos de projeto |
| [Contexto único em Markdown](dist/research-assistant-pipeline-0.1.0-pilot-context.md) | Uso manual em Projetos do ChatGPT, sem instalar uma skill |

O ZIP contém `research-assistant-pipeline/SKILL.md`, referências, scripts e modelos.
O arquivo de contexto reúne integralmente `SKILL.md`, as 12 referências, a citação e a licença,
com uma lista de hashes das fontes; ele não contém os scripts e modelos de projeto.
Guarde o ZIP como cópia da versão original. Não é necessário baixar todo o repositório
CAN-CCHD. Colar um link no chat não comprova leitura dos arquivos nem instala a skill.

## 2. Escolher como carregar o método

### A. Sua conta oferece Skills

A documentação da OpenAI descreve Skills e o uso de `@skill-creator`. A interface,
as permissões e a disponibilidade precisam ser conferidas na sua conta; este guia
não pressupõe um botão universal de importação de ZIP.

1. Selecione `@skill-creator`, quando disponível, e forneça o pacote pelo mecanismo
   de arquivos aceito. Se o ZIP não for aceito, descompacte-o e forneça a pasta ou
   os arquivos pelo mecanismo suportado pelo ambiente.
2. Peça para importar a skill existente, preservando as regras e os recursos:

```text
Quero usar a Research Assistant Pipeline 0.1.0-pilot fornecida nestes arquivos.
Verifique se este ambiente permite importar e instalar uma skill existente.
Se permitir, preserve as instruções, referências, scripts, modelos, licença,
citação e identificação da versão. Não substitua o método por um resumo ou
por regras novas. Informe qualquer adaptação de empacotamento necessária.
Confirme onde foi salva, como ativá-la e quais recursos conseguiu ler.
Se não puder instalar, diga explicitamente e me ajude a usar o modo Projeto.
```

3. Confirme que a skill foi salva e está disponível para seleção/ativação. Peça ao
   assistente para identificar a versão, as 12 fases e os limites de decisão humana.
   Uma resposta de confirmação sem leitura dos recursos não demonstra instalação.
4. Comece o projeto pela seção 3. Instalar a skill não concede acesso ao GitHub,
   a bases bibliográficas ou a execução de código.

### B. Sua conta não oferece instalação de Skills: usar um Projeto

1. Crie um **Projeto** no ChatGPT para sua pesquisa.
2. Adicione o arquivo `research-assistant-pipeline-0.1.0-pilot-context.md` às fontes
   ou arquivos do Projeto. Verifique se o upload foi aceito. Se Markdown não for
   aceito pela interface, salve uma cópia em `.txt`, sem alterar o texto, e anexe-a.
3. Nas instruções do Projeto, coloque:

```text
Use a Research Assistant Pipeline 0.1.0-pilot do arquivo de contexto anexado
como método de pesquisa. Leia as instruções e as referências pertinentes antes
de executar cada fase. Preserve protocolos personalizados, rastreabilidade,
decisões humanas, versões e autoria. Comece pela Fase 0 em projetos novos.
Ao retomar um projeto, use seu estado, aprovações e snapshot fixado; não troque
automaticamente suas regras. Informe os arquivos que conseguiu ler e os recursos
disponíveis. Não invente execução, fontes ou aprovações. Este é uso por contexto,
não instalação nativa da skill.
```

4. Inicie uma conversa dentro desse Projeto e use a mensagem da seção 3.

Projetos mantêm arquivos e instruções disponíveis entre suas conversas. Uma pasta
no seu computador não fica acessível apenas por criar um Projeto: forneça os arquivos
ou uma conexão autorizada. No modo por contexto, scripts só podem ser executados se
o pacote completo e a ferramenta de execução estiverem efetivamente disponíveis.

## 3. Começar, inclusive sem ideia definida

Copie a mensagem abaixo e acrescente seu campo de interesse ou pergunta, se houver:

```text
Quero desenvolver uma pesquisa usando a Research Assistant Pipeline.
Comece pela Fase 0 e responda em português. Ainda não tenho uma pergunta
definida; ajude-me a explorar interesses, recursos, contribuição e viabilidade.
Primeiro confirme a versão e quais arquivos e ferramentas estão acessíveis.
Faça poucas perguntas úteis por vez. Ajude-me a escolher o desenho e construir
regras específicas, justificadas e verificáveis. Mantenha propostas da IA separadas
das decisões humanas. Não inicie coleta ou seleção formal sem minha aprovação
documentada de um protocolo concreto.
```

Se você já tem uma pergunta, substitua a frase sobre não ter uma pergunta pela sua
proposta. A IA deve discutir alternativas e limites, sem presumir que haverá metanálise
ou novidade científica. Buscas iniciais de viabilidade são exploratórias.

## 4. Criar e guardar seu projeto

Com Python 3.10+ e o pacote completo disponível, o assistente pode executar, a partir
da pasta da skill:

```bash
python3 scripts/bootstrap_project.py /caminho/novo-projeto --title "Título provisório" --language pt-BR
```

Use um destino novo/vazio. O gerador cria arquivos locais, uma cópia fixada da skill,
estado de Fase 0 e aprovações pendentes. Ele não cria um repositório remoto.
Sem execução, use os modelos de `assets/project-template/` do ZIP para preparar
arquivos equivalentes, registre o modo manual e mantenha a cópia original da ferramenta.
Um conjunto de arquivos incompleto não deve ser apresentado como projeto validado.

Use seu próprio repositório, privado por padrão, ou outro armazenamento autorizado
com controle de versões. O acesso de escrita ao GitHub precisa ser verificado.
Se só houver leitura, o assistente deve preparar os arquivos e orientar o envio manual.
Guarde/download os arquivos de estado, protocolo, decisões, evidências e handoff;
não dependa apenas da memória da conversa ou de caminhos temporários de execução.

Não copie os dados ou o histórico do estudo CAN-CCHD. Prontuários identificáveis
permanecem em ambiente clínico apropriado; GitHub privado não é, por si só, esse ambiente.
Não envie senhas ou tokens em mensagens.

## 5. Conferir funcionamento e retomar

Antes de prosseguir, confira se o assistente:

- Identifica a versão 0.1.0-pilot e a Fase 0, sem aprovações presumidas.
- Explica o modo usado: skill instalada ou contexto manual em Projeto.
- Ajuda a construir regras adequadas à sua pergunta, com justificativas e testes.
- Informa o que pode ler, buscar, executar, salvar e sincronizar.
- Mantém fontes, sugestões da IA e decisões humanas distinguíveis.

Quando houver um projeto gerado e Python, execute:

```bash
python3 _pipeline/skill/scripts/validate_project.py /caminho/do-projeto
```

Esse resultado verifica consistência estrutural; não autentica decisões humanas nem
valida a ciência. Sem execução, registre a verificação como manual ou não executada.

Em uma conversa nova no mesmo Projeto, disponibilize os arquivos atuais e peça para
começar por `START_HERE.md`, conferir `project.json`, `CURRENT_STATE.md`,
`PIPELINE_LOCK.json`, protocolo, aprovações e `handoff/LATEST.md`. Resolva divergências
antes do trabalho dependente. Atualizações da ferramenta exigem migração explícita.

## 6. Crédito, limitações e feedback

Se a ferramenta contribuir substancialmente, cite a versão conforme
[CITATION.cff](CITATION.cff). Declare separadamente a IA utilizada, as tarefas reais
e a supervisão humana. Não há coautoria automática para os criadores da ferramenta
nem DOI atribuído ao piloto.

Este guia adapta o carregamento do mesmo método ao ChatGPT. Sua publicação não
comprova instalação na sua conta nem equivalência de desempenho entre modelos.
Consulte [EVALUATION.md](EVALUATION.md). Registre dificuldades com versão, modo,
etapa, comportamento observado e esperado, sem informações identificáveis.

Documentação oficial consultada em 19/10/2026; nomes de menus podem variar:

- [Skills & Plugins — OpenAI](https://learn.chatgpt.com/docs/skills-and-plugins)
- [Projects and chats — OpenAI](https://learn.chatgpt.com/docs/projects)
