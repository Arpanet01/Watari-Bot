# Watari-Bot
Bot de administração criado para o meu servidor do Discord

Aviso: Para que o sistema de registro funcione, você precisa criar um dicionário e salva-lo dentro de um arquivo json. As regras são puxadas de dentro desse arquivo.
Se você preferir não usar o sistema de registro do bot, pode apenas deletar a função `on_member_join`.

## Comandos

### lock

Use esse comando para fechar um canal.
Adicione a configuração `all_channels` para fechar todos os canais dos servidor.

Ex: `$lock all_channels`

### unlock

Usee esse comando para abrir um canal.
Adicione a configuração `all_channels` para abrir todos os canais do servidor.

### whois

Use esse comando para ver informações sobre um usuário.

Ex: `$whois @membro`

### avatar

Use esse comando para ver o avatar de um usuário.

Ex: `$avatar @membro`

### deter

Use esse comando para "prender" um usuário.
Esse comando precisa ter os canais configurados no código fonte do bot.

Ex: `$deter id_do_usuário`

### tell

Use esse comando para mandar "mensagens globais" no servidor.
Você pode enviar a mesma mensagem em vários canais em categorias específicas do servidor, ou pode enviar em todos os canais de maneira simultânea.

#### Como usar? 

Execute `tell` e siga as instruçoẽs.

### watari

Use para ver algumas informações sobre o bot.

### ban

Use esse comando para banir um usuário.

Ex: $ban id_do_usuário

### Vídeo de demonstração do sistema de registro:

