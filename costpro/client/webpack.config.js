const path = require('path');

const CLIENT_PATH = path.resolve(__dirname);
const BUILD_PATH = path.join(path.resolve('../'), '/static/emit');
const APP_PATH = path.join(CLIENT_PATH, '/src/Table.jsx');
const TEST_PATH = path.join(CLIENT_PATH, '/src/test.jsx');



module.exports = {
    mode: 'development',
    entry: {
        dashboard: APP_PATH,
        test: TEST_PATH
    },
    output: {
        path: BUILD_PATH,
        filename: '[name].bundle.js',
        publicPath: '/assets/'
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
            },
            {
                test: /\.(png|jpg|gif)$/,
                loader: 'file-loader',
            }
        ]
    },
    resolve: {
        alias: {
            src: path.resolve(__dirname, 'src/')
        }
    }
}