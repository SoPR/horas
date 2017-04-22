const path = require('path');
const autoprefixer = require('autoprefixer');
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
  entry: path.join(__dirname, 'src', 'bundle.js'),
  output: {
    path: path.join(__dirname, 'public'),
    filename: 'bundle.js'
  },
  module: {
    rules: [{
      // JavaScript
      test: /\.js$/,
      use: [
        { loader: 'babel-loader', query: { presets: [['es2015']] } },
        'eslint-loader'
      ]
    }, {
       // Stylus files
      test: /.styl$/,
      use: ExtractTextPlugin.extract({
        fallback: 'style-loader',
        use: [
          { loader: 'css-loader', options: { importLoaders: 1 } },
          'stylus-loader',
          {
            loader: 'postcss-loader',
            options: {
              plugins: () => {
                return [autoprefixer({ browsers: ['last 2 versions'] })];
              }
            }
          }
        ]
      })
    }, {
      test: /\.(jpe?g|png|gif|svg)$/i,
      use: [
        'file-loader?name=./img/[name].[ext]',
        {
          loader: 'image-webpack-loader',
          query: {
            bypassOnDebug: true,
            progressive: true,
            optipng: { optimizationLevel: 7 },
            gifsicle: { interlaced: false }
          }
        }
      ]
    }]
  },
  plugins: [
    new ExtractTextPlugin(path.join('css', 'app.css'))
  ]
};
