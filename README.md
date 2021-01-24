# DJANGO LINKDEV FREE

![GitHub repo size](https://img.shields.io/github/repo-size/fvitor7/Django_LinkDevFree?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/FVitor7/Django_LinkDevFree?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/FVitor7/Django_LinkDevFree?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/FVitor7/Django_LinkDevFree?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/FVitor7/Django_LinkDevFree?style=for-the-badge)

<img src="https://raw.githubusercontent.com/FVitor7/Django_LinkDevFree/master/capa.png" alt="preview Django LinkDevFree">

> Preview do projeto online.

---

## Clone
```bash
git clone https://github.com/FVitor7/Django_LinkDevFree.git
```

### Ajustes e melhorias

O projeto encontra-se em fase estável, porem é possivel adicionar novas melhorias.

- [x] Criação dos Models;
- [x] CRUD;
- [x] Sistema de usuários para gerenciamento de links;
- [x] Frontend BootStrap4;
- [x] Login e Cadastro com verificação no frontend;
- [x] Login e Cadastro com verificação no backend;
- [x] Personalização do gerenciamento e cadastro de links;
- [x] Personalização da página de preview dos links;


## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

* Você instalou a versão mais recente do `<Python3">`
* Você tem uma máquina `<Windows / Linux / Mac>`.
* Crie um ambiente virtual.
* Instale todas as dependências do `"requirements.txt"`.

```
pip install -r requirements.txt
```
## 🚀 Executando o Django LinkDevFree pela primeira vez:

```
python manage.py migrate # Inicia a database (executar apenas uma vez)
python manage.py makemigrations core (executar apenas uma vez)
python manage.py sqlmigrate core 0001 (executar apenas uma vez)
python manage.py createsuperuser # adiciona usuario admin  (executar apenas uma vez)
python manage.py migrate (executar apenas uma vez)

python manage.py runserver
```
URL para acessar o projeto no navegador:

```
http://localhost:8000
````

Painel ADMIN: (é possível cadastrar/ deletar usuários e gerenciar links).

```
http://localhost:8000/admin
````

API:

```
http://localhost:8000/api/v1/
```
Buscando links pelo username:
```
http://localhost:8000/api/v1/links/?username=username
```


## ☕ Usando o Django LinkDevFree

Para usar, siga estas etapas:

```
Você pode cadatrar um usuário,
Realizar login ou logout do sistema,
Gerenciar seus links (Acessar, Criar, Atualizar, Deletar),
Visualizar suas alterações na página final de preview quepoderá se compartilhada para outros usuários:
```

### Para visualizar e divulgar sua página de links, acesse:
```
http://localhost:8000/linkfree/username
```


## 📫 Contribuindo para Django LinkDevFree
<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado--->
Para contribuir com Django LinkDevFree, siga estas etapas:

1. Faça o fork do projeto
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/FVitor7">
        <img src="https://avatars2.githubusercontent.com/u/48036134?s=460&u=83e0e7eb1fe80c60164e6c9561a6174874c3b3da&v=4" width="100px;" alt="Foto do Fábio Vitor no GitHub"/><br>
        <sub>
          <b>Fábio Vitor</b>
        </sub>
      </a>
    </td>
    
  </tr>
</table>

Créditos pela página de preview: [Iuricode](https://github.com/iuricode).


## 😄 Seja um dos contribuidores<br>

Quer fazer parte desse projeto? Clique [AQUI](CONTRIBUTING.md) e leia como contribuir.

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

[⬆ Voltar ao topo](#Django_LinkDevFree)<br>
