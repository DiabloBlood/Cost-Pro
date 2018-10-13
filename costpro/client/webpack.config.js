const path = require('path');

module.exports = {
    mode: 'development',
    entry: __dirname + '/src_test/test2.jsx',
    output: {
        path: path.resolve('../') + '/static/src_test',
        filename: 'test.bundle.js'
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
    }
}