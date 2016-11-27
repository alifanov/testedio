var webpack = require('webpack');
require('es6-promise').polyfill();
var extractTextPlugin = require("extract-text-webpack-plugin");
// var svgoConfig = require('./config/svgo');
var path = require('path')

var extractStyles = new extractTextPlugin('styles.css');

var config = {
    context: __dirname + '/app',

    entry: {
        main: ['./app.js'],
    },

    output: {
        path: __dirname + '/public/assets',
        publicPath: '/assets/',
        filename: '[name].js'
    },

    // devtool: 'cheap-module-eval-source-map',
    devtool: 'cheap-source-map',

    resolve: {
        // extensions: ['', '.js', '.styl', '.css'],
        modulesDirectories: ['node_modules'],
    },

    module: {
        // preLoaders: [
        //     {
        //         test: /\.js$/,
        //         loader: "source-map-loader"
        //     }
        // ],
        loaders: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                query: {
                    presets: ['es2015', 'react', 'stage-0']
                },
            },
            {
                test: /react-icons\/(.)*(.js)$/,
                loader: 'babel',
                // include: 'node_modules/react-icons',
                query: {
                    presets: ['es2015', 'react']
                },
            },
            // {
            //     test: /\.styl$/,
            //     include: /styles/,
            //     loader: extractStyles.extract('style', 'css!autoprefixer!stylus')
            // },
            {
                test: /\.css$/,
                loader: extractStyles.extract('style', 'css!autoprefixer')
            },
            {
                test: /\.(ttf|eot|svg|woff|png)\?*[a-z0-9]*$/,
                loader: 'file?name=[path][name].[ext]'
            },
            // {
            //     test: /.*\.svg$/,
            //     loader: 'svgo?' + svgoConfig
            // }
        ]
    },

    plugins: [
        extractStyles,
        // new webpack.optimize.DedupePlugin(),
        // new webpack.optimize.OccurenceOrderPlugin(),
        // new webpack.optimize.UglifyJsPlugin({
        //     compress: {
        //         warnings: false
        //     }
        // }),
    ]
};

module.exports = config;