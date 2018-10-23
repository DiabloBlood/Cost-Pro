const path = require('path');

module.exports = {
    mode: 'development',
    entry: {
        dashboard: __dirname + '/src/dashboard.jsx',
        test: __dirname + '/src/test.jsx'
    },
    output: {
        path: path.resolve('../') + '/static/src',
        filename: '[name].bundle.js'
    },
    module: {
        rules: [
            {
                test: /\.jsx$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                options: {
                    presets: ['@babel/preset-env', '@babel/preset-react']
                }
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            }
        ]
    },
    resolve: {
        alias: {
            src: path.resolve(__dirname, 'src/')
        }
    }
}