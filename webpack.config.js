const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  entry: {
    home: './src/home/home.js', 
    login: './src/login/login.js'
  },
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist'),
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
  ],
  mode: 'development',
  devServer: {
    static: {
        directory: path.join(__dirname, 'dist'), // Serve content from the "dist" directory
    },
    compress: true, // Enable gzip compression
    port: 5500, // You can specify any port you want
    open: true, // Automatically open the browser
    historyApiFallback: true, // Enable support for single-page applications,
    hot: true,
  },
};