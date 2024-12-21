## 🌐 [English Version of README](README_EN.md)

# Meteora

Meteora é um e-commerce desenvolvido com React, utilizando uma arquitetura baseada em componentes e contexto para gerenciar o estado do carrinho de compras. O projeto é estruturado para oferecer uma experiência de compra com categorias de produtos, carrosséis de imagens e um carrinho de compras funcional.

## 🔨 Funcionalidades do Projeto

- **Carrinho de Compras:** Adição, remoção e atualização de quantidades de produtos no carrinho.
- **Categorias de Produtos:** Apresentação de diferentes categorias como bolsas, calçados, camisetas, etc.
- **Carrossel de Imagens:** Exibição de banners promocionais e de produtos.
- **Resumo de Compra:** Exibe o resumo da compra no carrinho com detalhes dos itens e valor total.
- **Facilidades e Novidades:** Seção para mostrar vantagens e novidades no site.

### Exemplo Visual do Projeto

![chrome-capture-2024-12-21 (1)](https://github.com/user-attachments/assets/890ac68d-dc26-4aed-981a-88ce386697cd)

## ✔️ Técnicas e Tecnologias Utilizadas

- **React.js:** Biblioteca principal para construção da interface.
- **Vite:** Ferramenta de build e desenvolvimento rápido para projetos em React.
- **Context API:** Para gerenciamento de estado global (carrinho de compras).
- **Bootstrap:** Framework CSS para estilos rápidos e responsivos.
- **JavaScript (ES6):** Para lógica de interação e funcionalidades no frontend.
- **JSON:** Utilizado para mock de dados como produtos, categorias e facilidades.

## 📁 Estrutura do Projeto

- **public/**
  - **favicon.ico:** Ícone do site.
  - **index.html:** Arquivo HTML principal que carrega o projeto.
  - **assets/:** Imagens, ícones e outros recursos estáticos.
  - **vite.svg:** Logo do Vite.
  
- **src/**
  - **App.jsx:** Componente principal que organiza a aplicação.
  - **components/:** Contém componentes reutilizáveis como botões, produtos, categorias, etc.
  - **context/:** Contém o contexto de gerenciamento do carrinho de compras.
  - **hooks/:** Hooks personalizados para manipulação do carrinho.
  - **mocks/:** Arquivos JSON com dados fictícios (produtos, categorias).
  - **pages/:** Páginas principais como Home e Carrinho.
  - **reducers/:** Funções de manipulação do estado do carrinho.
  - **utils/:** Funções utilitárias, como formatação de moeda.
  - **App.css:** Estilos principais da aplicação.
  - **index.css:** Estilos globais.

## 🛠️ Abrir e rodar o projeto

Para iniciar o projeto localmente, siga os passos abaixo:

1. **Certifique-se de que o Node.js está instalado**:
   - O [Node.js](https://nodejs.org/) é necessário para rodar o projeto. Você pode verificar se já o tem instalado com:

   ```bash
   node -v
   ```

- Se não estiver instalado, baixe e instale a versão recomendada.

2. **Clone o Repositório**:
    - Copie a URL do repositório e execute o comando abaixo no terminal:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

3. **Instale as Dependências**:
    - Navegue até o diretório do projeto e instale as dependências utilizando o comando:

   ```bash
   npm install
   ```

4. **Execute o Projeto**:
    - Após a instalação das dependências, inicie o projeto com:

   ```bash
   npm run dev
   ```

    - A aplicação estará disponível em [http://localhost:3000](http://localhost:3000).

## 🌐 Deploy

Para realizar o deploy da aplicação, siga os passos abaixo:

1. **Construa o Projeto**:
    - Utilize o comando para gerar uma versão otimizada para produção:

   ```bash
   npm run build
   ```

2. **Hospede o Projeto**:
    - Você pode hospedar o projeto em diversas plataformas como [Vercel](https://vercel.com/), [Netlify](https://www.netlify.com/), ou em um servidor de sua escolha.
    - Caso use o Vercel, basta conectar seu repositório ao Vercel e ele irá automaticamente realizar o deploy.

3. **Acesse a versão online**:
    - Após o deploy, você receberá uma URL onde poderá acessar a versão online do seu projeto.
