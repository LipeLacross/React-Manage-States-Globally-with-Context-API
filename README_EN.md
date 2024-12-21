## 🌐 [Portuguese Version of README](README.md)

# Meteora

Meteora is an e-commerce application built with React, utilizing a component-based architecture and the context API to manage the shopping cart state. The project is designed to offer a shopping experience with product categories, image carousels, and a functional shopping cart.

## 🔨 Project Features

- **Shopping Cart:** Add, remove, and update product quantities in the cart.
- **Product Categories:** Display of different categories such as bags, shoes, t-shirts, etc.
- **Image Carousel:** Show promotional and product banners.
- **Purchase Summary:** Displays the summary of the purchase in the cart with item details and total value.
- **Conveniences and News:** Section to show benefits and news on the site.

### Visual Example of the Project

![chrome-capture-2024-12-21 (1)](https://github.com/user-attachments/assets/18c699b5-a22c-45d0-bcd9-0569fa7e847e)

## ✔️ Techniques and Technologies Used

- **React.js:** The main library used to build the interface.
- **Vite:** A build tool for fast development with React.
- **Context API:** For global state management (shopping cart).
- **Bootstrap:** CSS framework for quick and responsive styling.
- **JavaScript (ES6):** For logic and interactions in the frontend.
- **JSON:** Used for mocking data such as products, categories, and conveniences.

## 📁 Project Structure

- **public/**
  - **favicon.ico:** The website's favicon.
  - **index.html:** The main HTML file that loads the project.
  - **assets/:** Images, icons, and other static resources.
  - **vite.svg:** Vite logo.
  
- **src/**
  - **App.jsx:** The main component that organizes the application.
  - **components/:** Contains reusable components like buttons, products, categories, etc.
  - **context/:** Contains the context for managing the shopping cart.
  - **hooks/:** Custom hooks for manipulating the cart.
  - **mocks/:** JSON files with mock data (products, categories).
  - **pages/:** Main pages like Home and Cart.
  - **reducers/:** Reducer functions to handle the cart state.
  - **utils/:** Utility functions, such as currency formatting.
  - **App.css:** Main styles for the application.
  - **index.css:** Global styles.

## 🛠️ Running the Project Locally

To run the project locally, follow the steps below:

1. **Make sure Node.js is installed**:
   - [Node.js](https://nodejs.org/) is required to run the project. You can check if it's already installed by running:

   ```bash
   node -v
   ```

- If it's not installed, download and install the recommended version.

2. **Clone the Repository**:
    - Copy the repository URL and run the following command in your terminal:

   ```bash
   git clone <REPOSITORY_URL>
   ```

3. **Install Dependencies**:
    - Navigate to the project directory and install the dependencies using the command:

   ```bash
   npm install
   ```

4. **Run the Project**:
    - After installing the dependencies, start the project with:

   ```bash
   npm run dev
   ```

    - The application will be available at [http://localhost:3000](http://localhost:3000).

## 🌐 Deploy

To deploy the application, follow the steps below:

1. **Build the Project**:
    - Use the following command to create an optimized production build:

   ```bash
   npm run build
   ```

2. **Host the Project**:
    - You can host the project on various platforms like [Vercel](https://vercel.com/), [Netlify](https://www.netlify.com/), or a server of your choice.
    - If using Vercel, simply connect your repository to Vercel, and it will automatically deploy the app.

3. **Access the Online Version**:
    - After deployment, you will receive a URL where you can access the live version of your project.
