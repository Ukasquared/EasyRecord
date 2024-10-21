const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
// const { sign } = require('crypto');

module.exports = {
  entry: {
    home: './src/home/home.js', 
    login: './src/login/login.js',
    admin: './src/admin/admin.js',
    parent: './src/parent/parent.js',
    teacher: './src/teacher/teacher.js',
    signup: './src/signup/signup.js'
  },
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'api/dist/'),
    clean: true,
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },

      {
        test: /\.(png|jpe?g|gif|svg)$/, // Match image files
        use: [
          {
            loader: 'file-loader', // Use file-loader for images
            options: {
              name: '[name].[hash].[ext]', // Output filename pattern
              outputPath: 'images/', // Directory to save images in output
            },
          },
        ],
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/home/home.html',  // Template file for home page
      filename: 'home.html',              // Output file for home page
      chunks: ['home'],                   // Bundle for home page
    }),
    new HtmlWebpackPlugin({
      template: './src/login/login.html', // Template file for login page (optional)
      filename: 'login.html',             // Output file for login page
      chunks: ['login'],                  // Bundle for login page
    }),
    new HtmlWebpackPlugin({
      template: './src/parent/parent.html', // Template file for login page (optional)
      filename: 'parent.html',             // Output file for login page
      chunks: ['parent'],                  // Bundle for login page
    }),
    new HtmlWebpackPlugin({
      template: './src/teacher/teacher.html', // Template file for login page (optional)
      filename: 'teacher.html',             // Output file for login page
      chunks: ['teacher'],                  // Bundle for teach page
    }),
    new HtmlWebpackPlugin({
      template: './src/admin/admin.html', // Template file for login page (optional)
      filename: 'admin.html',             // Output file for login page
      chunks: ['admin'],                  // Bundle for admin page
    }),
    new HtmlWebpackPlugin({
      template: './src/signup/signup.html', // Template file for login page (optional)
      filename: 'signup.html',             // Output file for login page
      chunks: ['signup'],                  // Bundle for signup page
    }),
  ],
  mode: 'development',
  devServer: {
    static: {
        directory: path.join(__dirname, 'dist'), // Serve content from the "dist" directory
    },
    proxy: [{
      context: ['/api'], 
      target: 'http://127.0.0.1:5000',
    }],
    compress: true, // Enable gzip compression
    port: 5500, // You can specify any port you want
    open: true, // Automatically open the browser
    historyApiFallback: {
      rewrites: [
        { from: /^\/$/, to: '/home.html' },         // Root route serves home.html
      ],
    },
    hot: true,
  },
};