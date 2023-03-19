#TicketFlow

# Sobre

    Api para implementação de um sistema de controle de venda de ingressos para eventos

## Como instalar:

### Docker no Windows:
    
1. Clique duas vezes em Docker Desktop Installer.exe para executar o instalador.
            
* Se você ainda não baixou o instalador (Docker Desktop Installer.exe), pode obtê-lo no Docker Hub https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe
        
2. Siga as instruções do assistente de instalação para concluir o processo.
3. Quando a instalação finalizar clique em **fechar**
4. Se sua conta de administrador for diferente de sua conta de usuário, você deverá adicionar o usuário ao grupo docker-users. Execute o Gerenciamento do computador como administrador e navegue até Usuários e grupos locais > Grupos > docker-users. Clique com o botão direito do mouse para adicionar o usuário ao grupo. Saia e entre novamente para que as alterações entrem em vigor.

5. Garanta que o WSL2 esteja funcionando, duvida sobre WSL2 > https://learn.microsoft.com/pt-br/windows/wsl/install
6. Execute o Docker Desktop
7. dentro do diretorio raiz do projeto execute o comando
    
    * **docker compose up --build**

8. Se tudo estiver executado corretamente acesso a url localhost:8000

### Docker no Ubuntu:

#### Execute os seguites comando no Terminal

        1. sudo apt update
        2. sudo apt install apt-transport-https ca-certificates curl software-properties-common
        3. curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        4. sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
        5. sudo apt update
        6. apt-cache policy docker-ce
        7. sudo systemctl status docker
 
 ##### Dentro do Diretorio Raiz do projeto
  
        8. sudo docker compose up --build


