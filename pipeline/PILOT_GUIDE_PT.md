# Piloto no Claude — Research Assistant Pipeline 0.1.0

Esta skill ajuda você e sua IA a transformar uma ideia em um protocolo próprio,
desenvolver a pesquisa em 12 fases e preservar fontes, decisões e autoria científica.
Você pode começar sem uma pergunta definida.

## 1. Instalar

1. Abra o [pacote do piloto](dist/research-assistant-pipeline-0.1.0-pilot.zip) e use
   o botão de download do GitHub para baixar o ZIP.
2. No Claude, habilite execução de código/criação de arquivos quando disponível.
3. A orientação oficial atual é **Customize → Skills → Create skill → Upload a skill**.
   Carregue o ZIP inteiro e habilite a skill. Se a interface for diferente, consulte
   a [ajuda oficial](https://support.claude.com/en/articles/12512180-use-skills-in-claude).
4. Em Claude Code, a pasta da skill também pode ser instalada em `.claude/skills/`
   no projeto ou `~/.claude/skills/` na conta local.

O ZIP deve conter uma pasta `research-assistant-pipeline/`, com `SKILL.md` e os
recursos dentro dela. Não carregue o ZIP de todo o repositório CAN-CCHD como skill.

## 2. Começar

Peça ao Claude para usar **Research Assistant Pipeline** e informe seu campo de
interesse, uma dúvida ou caso que motivou a pesquisa. Diga se ainda não tem uma ideia.
Ele deve explorar a pergunta, os recursos e a viabilidade antes de propor um desenho.

Ele ajudará a criar um protocolo com justificativas, fontes metodológicas, regras
operacionais, critérios de conclusão e decisões que dependem de você. Revise e aprove
o protocolo antes de iniciar a coleta/seleção formal. Buscas exploratórias iniciais
devem ser identificadas como tais.

## 3. Criar seu projeto

A skill inclui um gerador de projeto vazio. Se o Claude puder executar Python:

```bash
python3 scripts/bootstrap_project.py /caminho/novo-projeto --title "Título provisório" --language pt-BR
```

O comando deve ser executado a partir da pasta da skill, com um destino novo/vazio.
O Claude pode localizar a pasta no ambiente dele. Sem execução, ele pode montar os
arquivos equivalentes e informar quais verificações não foram executadas.

Crie então um repositório **na sua própria conta do GitHub**, privado por padrão.
Com ferramentas autorizadas de escrita, o assistente pode ajudar na criação e no envio.
Com acesso somente de leitura, ele deve preparar os arquivos e orientar o envio manual.
Instalar a skill não concede acesso ao GitHub. Não informe senhas/tokens em mensagens.

Este repositório do CAN-CCHD **não é um template vazio**. Use o projeto gerado,
sem copiar o estudo, seus resultados, banco de dados ou histórico. Documentos clínicos
identificáveis devem permanecer em ambiente apropriado e autorizado; privado no GitHub
não significa adequado para armazenar prontuários.

## 4. Retomar em outra conversa

Disponibilize o repositório/arquivos atuais e peça para começar por `START_HERE.md`.
O assistente deve conferir o protocolo, as decisões, o estado e a versão fixada da
skill. O trabalho deve ser retomado pelos arquivos, sem depender da memória do chat.

Se aparecer uma versão nova da ferramenta, a migração é explícita, com avaliação de
impacto. Não atualize automaticamente as regras no meio do estudo.

## 5. Crédito e publicação

Se o pipeline contribuir substancialmente, solicitamos sua citação conforme
[CITATION.cff](CITATION.cff), com a versão utilizada. O artigo deve descrever também
qual IA foi usada, em quais tarefas e como os pesquisadores revisaram e decidiram.
Os criadores da ferramenta não se tornam coautores do seu estudo pelo uso da skill.
Ainda não há DOI atribuído ao piloto.

## 6. O que avaliar no piloto

- A IA ajuda a formular uma pergunta viável sem impor o desenho?
- As regras propostas correspondem ao objetivo e têm justificativa?
- Ela distingue propostas da IA e decisões humanas reais?
- Ela preserva fontes, incertezas e versões?
- Uma nova conversa consegue retomar o estado correto?
- Ela informa honestamente limites de ferramentas, buscas e verificações?

Anote a versão, o ponto em que houve dificuldade, o comportamento observado e o
resultado esperado. Compartilhe apenas exemplos sem dados identificáveis ou material
confidencial. Consulte [EVALUATION.md](EVALUATION.md) para o alcance dos testes atuais.
